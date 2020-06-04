import numpy as np

import fiona
import rasterio
from rasterio.crs import CRS as CRS_rio
from rasterio.warp import transform_geom, \
                          calculate_default_transform, reproject, Resampling

from utils_text import normalize_name_classes

def print_wrapper():
    print("Hello from wrapper!")
    
def reproj_normalize_and_write_vector(feature_collection, feature_collection_schema,
                                      list_name_attributes,
                                      layer_name,
                                      output_filename,
                                      source_crs, 
                                      driver = "ESRI Shapefile",
                                      destiny_crs = "4326",
                                      is_geographic = True):
    """
    Reprojection, normalizing of fields using name of attributes in list and
    write to file. Function used for large size vectors.
    Args:
        feature_collection (geojson): GeoJSON like dict object or iterable of GeoJSON like objects.
        feature_collection_schema (dict): dictionary holding schema of feature_collection.
        list_name_attributes (list): attributes of type text that will be searched for to be normalized.
        layer_name (str): name of layer that will be in output_filename.
        output_filename (str): path of filename that will be written in filesystem.
        source_crs (str): string of source coordinate reference system.
        
    """
    dst = fiona.open(output_filename, 'w',
                     driver = driver,
                     layer = layer_name,
                     crs = CRS_rio.from_epsg(destiny_crs).to_proj4(),
                     schema = feature_collection_schema)
    dst.close()
    with fiona.open(output_filename, 'a',
                    driver = driver,
                    layer = layer_name,
                    crs = CRS_rio.from_epsg(destiny_crs).to_proj4(),
                    schema = feature_collection_schema) as dst:
        for feature in feature_collection:
            if not is_geographic:
                feature['geometry'] = transform_geom(CRS_rio.from_proj4(source_crs), 
                                                     CRS_rio.from_epsg(destiny_crs),
                                                     feature['geometry'])
            for att in list_name_attributes:
                feature['properties'][att] = normalize_name_classes(feature['properties'][att])
            dst.write(feature)
            
def reproj_and_write_one_band_raster(source_dataset, output_filename,
                                     destiny_crs = "EPSG:4326",
                                     is_geographic = True):
    """
    Reprojection, tiling and writing of one band rater to file.
    Args:
        source_dataset (ndarray or Band): The source is a 2 ndarray, or Rasterio one band object. 
        output_filename (str): path of filename that will be written in filesystem.
    """
    source_meta = source_dataset.meta.copy()
    source_transform = source_dataset.transform
    source_width = source_dataset.width
    source_height = source_dataset.height
    source_crs = source_dataset.crs
    if not is_geographic:
        transform, width, height = calculate_default_transform(source_crs, destiny_crs, 
                                                               source_width, source_height, 
                                                               *source_dataset.bounds)
        source_meta.update({'crs': destiny_crs,
                           'transform': transform,
                           'width': width,
                           'height': height
                            })
    else:
        transform, width, height = source_transform, source_width, source_height
    
    source_meta.update({'driver': 'GTiff',
                        'count': 1,
                        'dtype': rasterio.uint8,
                        'compress': 'lzw',
                        'tiled': True
                        })
    with rasterio.open(output_filename, 'w', **source_meta,
                       ) as dst:
        array = np.zeros((height, width), dtype=rasterio.uint8)
        reproject(source=rasterio.band(source_dataset, 1),
                  destination=array,
                  src_transform=source_transform,
                  src_crs=source_crs,
                  dst_transform=transform,
                  dst_crs=destiny_crs,
                  resampling=Resampling.nearest
                  )  
        dst.write(array, 1)

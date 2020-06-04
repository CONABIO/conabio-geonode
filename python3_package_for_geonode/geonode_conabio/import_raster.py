from pyproj import Proj
import rasterio

from geonode_conabio.wrappers import reproj_and_write_one_band_raster
from geonode_conabio.utils_docker import import_layers_via_docker

def main():
    direc = '/LUSTRE/MADMEX/products/landcover/sentinel2/2017/estados/Aguascalientes/31/'
    input_filename = ''.join([direc, '/Aguascalientes_2017_31.tif'])
    output_filename = ''.join([direc, '/Aguascalientes_2017_31_wgs84_tiled_rasterio.tif'])
    with rasterio.open(input_filename) as src:
        src_crs = src.crs.to_string()
        proj_crs = Proj(src_crs)
        if not proj_crs.crs.is_geographic:
            reproj_and_write_one_band_raster(src, output_filename,
                                             is_geographic=False)
        else:
            reproj_and_write_one_band_raster(src, output_filename)
            
    region = "".join(["\"Aguascalientes, Mexico, North America, Latin America\""])
    name = "\"sentinel2_Aguascalientes_2017_31_tiled\""
    title = "\"sentinel2_Aguascalientes_2017_31_tiled\""
    abstract = "\"Sentinel2 MAD-Mex land cover classification\""
    kw = "\"MAD-Mex, Sentinel2, GeoTIFF, WCS\""
    
    result_import = import_layers_via_docker(region, name, title,
                                             abstract, kw,
                                             output_filename
                                             )
    print(result_import)
    

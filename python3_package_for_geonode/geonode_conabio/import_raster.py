import os
import argparse
from argparse import RawTextHelpFormatter

import rasterio

from geonode_conabio.wrappers import reproj_and_write_one_band_raster
from geonode_conabio.utils_docker import import_layers_via_docker

def arguments_parse():
    help = """
    
Wrapper for importlayers command of geonode. Meant to use for rasters. Will reproject to wgs84, compress, tile it 
and execute importlayers command within django container via docker-py to register it in both geoserver and geonode.

--------------
Example usage:
--------------

import_raster --input_directory /LUSTRE/MADMEX/products/landcover/sentinel2/2017/estados/Aguascalientes/31
              --input_filename Aguascalientes_2017_31.tif
              --region "Aguascalientes, Mexico, North America, Latin America"
              --name "MAD-Mex_sentinel2_Aguascalientes_2017_31"
              --title "MAD-Mex_sentinel2_Aguascalientes_2017_31"
              --abstract "Sentinel2 MAD-Mex land cover classification"
              --key_words "MAD-Mex, Sentinel2, GeoTIFF, WCS"

"""
            
    parser = argparse.ArgumentParser(description=help,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--input_directory",
                        required=True,
                        default=None,
                        help="Help of test argparse fun") 
    parser.add_argument("--input_filename",
                        required=True,
                        default=None,
                        help="Help of test argparse fun")
    parser.add_argument("--region",
                        required=True,
                        default=None,
                        help="Help of test argparse fun")
    parser.add_argument("--name",
                        required=True,
                        default=None,
                        help="Help of test argparse fun")
    parser.add_argument("--title",
                        required=True,
                        default=None,
                        help="Help of test argparse fun")
    parser.add_argument("--abstract",
                        required=True,
                        default=None,
                        help="Help of test argparse fun")
    parser.add_argument("--key_words",
                        required=True,
                        default=None,
                        help="Help of test argparse fun")
    args = parser.parse_args()
    return args

def main():
    args = arguments_parse()
    input_directory = args.input_directory
    input_filename = args.input_filename
    region = ''.join(["\"", args.region, "\""])
    filename = args.name
    name_geonode = ''.join(["\"", filename, "\""])
    title = ''.join(["\"", args.title, "\""])
    abstract = ''.join(["\"", args.abstract, "\""])
    kw = ''.join(["\"", args.key_words, "\""])
        
    input_filename = os.path.join(input_directory, input_filename)
    output_filename_temporal = os.path.join(input_directory, filename)
    
    output_filename_temporal += ".tif"
    
    with rasterio.open(input_filename) as src:   
        reproj_and_write_one_band_raster(src, output_filename_temporal)
    
    
    result_import = import_layers_via_docker(region, name_geonode, title,
                                             abstract, kw,
                                             output_filename_temporal
                                             )
    
    print(result_import)
    
    os.remove(output_filename_temporal)
        

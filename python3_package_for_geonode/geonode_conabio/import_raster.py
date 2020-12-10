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

import_raster --base_directory /LUSTRE/MADMEX/products/landcover/sentinel2/2017/estados/Aguascalientes/31
              --input_filename Aguascalientes_2017_31.tif
              --region "Aguascalientes, Mexico, North America, Latin America"
              --name "MAD-Mex_sentinel2_Aguascalientes_2017_31"
              --title "MAD-Mex_sentinel2_Aguascalientes_2017_31"
              --abstract "Sentinel2 MAD-Mex land cover classification"
              --key_words "MAD-Mex, Sentinel2, GeoTIFF, WCS"

"""
            
    parser = argparse.ArgumentParser(description=help,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--base_directory",
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
    direc = args.base_directory
    input_filename = args.input_filename
    region = ''.join(["\"", args.region, "\""])
    name = ''.join(["\"", args.name, "\""])
    title = ''.join(["\"", args.title, "\""])
    abstract = ''.join(["\"", args.abstract, "\""])
    kw = ''.join(["\"", args.key_words, "\""])
    
    output_filename = input_filename.split('.')[0]
    output_filename+= '_wgs84_tiled_rasterio.tif'

    input_filename = os.path.join(direc, input_filename)
    output_filename = os.path.join(direc, output_filename)
    
    with rasterio.open(input_filename) as src:   
        reproj_and_write_one_band_raster(src, output_filename)
    
    
    result_import = import_layers_via_docker(region, name, title,
                                             abstract, kw,
                                             output_filename
                                             )
    print(result_import)
    
    
    os.remove(output_filename)
    

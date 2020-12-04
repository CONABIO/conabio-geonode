import os
import argparse
from argparse import RawTextHelpFormatter
from glob import glob

import geopandas as gpd
from pyproj import Proj

from geonode_conabio.wrappers import reproj_normalize_and_write_small_medium_size_vector
from geonode_conabio.utils_docker import import_layers_via_docker

def arguments_parse():
    help = """
    
Wrapper for importlayers command of geonode. Meant to use for small and medium size vector. 

Will reproject to wgs84, normalize string attributes and execute importlayers command within django container 
via docker-py to register it in both geoserver and geonode.
--------------
Example usage:
--------------

import_small_medium_size_vector --input_directory /LUSTRE/MADMEX/products/landcoverchange/sentinel2/2017_2018/indi50k/estados/AGUASCALIENTES
                                --input_filename AGUASCALIENTES_merge.shp
                                --destiny_path /shared_volume/ftp_dir/
                                --list_attributes "t1_dsc_31, t2_dsc_31, t1_dsc_17, t2_dsc_17, cmb_dsc_31, cmb_dsc_17"
                                --region "Aguascalientes, Mexico, North America, Latin America"
                                --name "MAD-Mex_sentinel2_Aguascalientes_2017_lcc_geopandas"
                                --title "MAD-Mex_sentinel2_Aguascalientes_2017_lcc_geopandas"
                                --abstract "Sentinel2 MAD-Mex land cover change"
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
    parser.add_argument("--destiny_path",
                        required=True,
                        default=None,
                        help="Help of test argparse fun")
    parser.add_argument("--list_attributes",
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
    destiny_path = args.destiny_path
    list_name_attributes = args.list_attributes.replace(' ','').split(',')
    region = ''.join(["\"", args.region, "\""])
    filename = args.name
    name_geonode = ''.join(["\"", filename, "\""])
    title = ''.join(["\"", args.title, "\""])
    abstract = ''.join(["\"", args.abstract, "\""])
    kw = ''.join(["\"", args.key_words, "\""])

    output_filename = input_filename.split('.')[0]
    layername = filename

    input_filename = os.path.join(input_directory, input_filename)
    output_filename = os.path.join(destiny_path, filename)
    
    gdf = gpd.read_file(input_filename)
    #dropNA's
    gdf.dropna(subset=list_name_attributes, inplace=True)

    output_filename_geonode = reproj_normalize_and_write_small_medium_size_vector(gdf,
                                                                                  list_name_attributes,
                                                                                  layername,
                                                                                  input_directory,
                                                                                  output_filename)
    result_import = import_layers_via_docker(region, name_geonode, title,
                                             abstract, kw,
                                             output_filename_geonode
                                             )
    print(result_import)
    
    output_filename_without_extension = output_filename_geonode.split('.')[0]
    
    l_output_filenames = glob(output_filename_without_extension +'*',recursive=True)
    
    for filenames in l_output_filenames:
        os.remove(filenames)
    dir_shapefile = os.path.join(input_directory, filename)
    os.removedirs(dir_shapefile)
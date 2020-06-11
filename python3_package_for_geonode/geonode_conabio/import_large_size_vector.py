import os
import argparse
from argparse import RawTextHelpFormatter
from glob import glob

import fiona
from pyproj import Proj
from fiona.crs import to_string

from geonode_conabio.wrappers import reproj_normalize_and_write_large_vector

from geonode_conabio.utils_cli import create_table_via_shp2pgsql
from geonode_conabio.utils_docker import update_layers_via_docker, publish_featuretype_via_docker

def arguments_parse():
    help = """
    
Wrapper for importlayers command of geonode. Meant to use for large size vector. 

Will reproject to wgs84, normalize string attributes and execute importlayers command within django container 
via docker-py to register it in both geoserver and geonode.
--------------
Example usage:
--------------

import_large_size_vector --base_directory /LUSTRE/MADMEX/products/landcoverchange/sentinel2/2017_2018/indi50k/estados/AGUASCALIENTES
                         --input_filename AGUASCALIENTES_merge.shp
                         --list_attributes "t1_dsc_31, t2_dsc_31, t1_dsc_17, t2_dsc_17, cmb_dsc_31, cmb_dsc_17"
                         --region "Aguascalientes, Mexico, North America, Latin America"
                         --name "MAD-Mex_sentinel2_Aguascalientes_2017_lcc_fiona"
                         --title "MAD-Mex_sentinel2_Aguascalientes_2017_lcc_fiona"
                         --abstract "Sentinel2 MAD-Mex land cover change"
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
    direc = args.base_directory
    input_filename = args.input_filename
    list_name_attributes = args.list_attributes.replace(' ','').split(',')
    region = ''.join(["\"", args.region, "\""])
    name = ''.join(["\"", args.name, "\""])
    title = ''.join(["\"", args.title, "\""])
    abstract = ''.join(["\"", args.abstract, "\""])
    kw = ''.join(["\"", args.key_words, "\""])

    output_filename = input_filename.split('.')[0]
    output_filename += '_wgs84_fiona.shp'
    
    layer = output_filename.split('.')[0]
    input_filename = ''.join([direc, '/', input_filename])
    output_filename = ''.join([direc, '/', output_filename])
    
    with fiona.open(input_filename) as src:
        fc = (feature for feature in src if not None in [feature['properties'][att] for att in list_name_attributes] and
                                                         feature['geometry'] is not None)
        src_crs = to_string(src.crs)
        proj_src_crs = Proj(src_crs)
        fc_schema = src.schema
        if not proj_src_crs.crs.is_geographic:
            reproj_normalize_and_write_large_vector(fc, fc_schema,
                                                    list_name_attributes,
                                                    layer,
                                                    output_filename,
                                                    src_crs, 
                                                    is_geographic = False
                                                    )
        else:
            reproj_normalize_and_write_large_vector(fc, fc_schema, 
                                                    list_name_attributes,
                                                    layer,
                                                    output_filename,
                                                    src_crs
                                                    )
    
    name_table = layer.lower()
    
    [result_create_table, out, err] = create_table_via_shp2pgsql(output_filename, name_table)
    
    print((result_create_table, out, err))
    
    result_publish = publish_featuretype_via_docker(name_table)
    
    print(result_publish)
    
    result_update = update_layers_via_docker(name_table)
    
    print(result_update)
    
    basename_output_filename = output_filename.split('.')[0]
    
    l_output_filenames = glob(basename_output_filename +'*',recursive=True)
    
    for filenames in l_output_filenames:
        os.remove(filenames)

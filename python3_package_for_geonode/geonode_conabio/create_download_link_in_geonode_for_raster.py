import os
import argparse
import zipfile
from os.path import basename

import rasterio

from geonode_conabio.utils_docker import get_layer_and_style_registered_in_geonode_via_docker
from geonode_conabio.utils_style import get_cmap_from_element_list_madmex_style
from geonode_conabio.utils_parser import parse_style_sld_madmex
from geonode_conabio.utils_docker import create_link_in_geonode_for_zip_file_via_docker

def arguments_parse():
    help = """
    
Wrapper to create link to download raster in geonode. Will write color map to raster and put it in directory zipped with style.

--------------
Example usage:
--------------

create_download_link_in_geonode_for_raster --title_layer "Test3 National land cover map 2015 32 classes 512 512"
                                           --destiny_path /shared_volume/ftp_dir/
                                           --dir_path_styles_geonode /shared_volume/geonode/scripts/spcgeonode/_volume_geodatadir/workspaces/geonode/styles/
                                           --dir_path_layers_geonode /shared_volume/geonode/scripts/spcgeonode/_volume_geodatadir/data/geonode/
"""
            
    parser = argparse.ArgumentParser(description=help,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--title_layer",
                    required=True,
                    default=None,
                    help="Help of test argparse fun")
    parser.add_argument("--destiny_path",
                    required=True,
                    default=None,
                    help="Help of test argparse fun")
    parser.add_argument("--dir_path_styles_geonode",
                    required=True,
                    default=None,
                    help="Help of test argparse fun")
    parser.add_argument("--dir_path_layers_geonode",
                    required=True,
                    default=None,
                    help="Help of test argparse fun")
    args = parser.parse_args()
    return args
def main():
    args = arguments_parse()
    title_layer = args.title_layer
    destiny_path = args.destiny_path
    dir_path_styles_geonode = args.dir_path_styles_geonode
    dir_path_layers_geonode = args.dir_path_layers_geonode
    
    result_get = get_layer_and_style_registered_in_geonode(title_layer)
    print(result_get)
    
    layer_name, style_name = result_get.decode().split("\n")[0:2]
    
    style_source_path =  dir_path_styles_geonode + style_name + ".sld"
    layer_source_path =  dir_path_layers_geonode + layer_name + "/" + layer_name + ".geotiff"
    
    rf_children = parse_sld_madmex_style(style_source_path)
    
    rgb_dict = get_cmap_from_element_list_madmex_style(rf_children)
    
    #Write cmap to raster
    if not os.path.exists(destiny_path):
        os.makedirs(destiny_path)
    
    layer_cmap_source_path = destiny_path + layer_name + ".geotiff"
    
    with rasterio.open(layer_source_path) as src:
        arr = src.read(1)
        meta = src.meta
    meta["compress"] = "lzw"
    with rasterio.open(layer_cmap_source_path, 'w', **meta) as dst:
        dst.write(arr, indexes=1)
        dst.write_colormap(1,rgb_dict)
        cmap_result = dst.colormap(1)
    #Zip file    
    zip_file = destiny_path + layer_name + ".zip"
    zipf = zipfile.ZipFile(zip_file, 'w', zipfile.ZIP_DEFLATED)
    zipf.write(style_source_path, basename(style_source_path))
    zipf.write(layer_cmap_source_path, basename(layer_cmap_source_path))
    zipf.close()
    os.remove(layer_cmap_source_path)
    
    #if success creating download link in geonode
    if os.path.exists(zip_file):
        create_link_in_geonode_for_zip_file_via_docker(zip_file, title_layer)
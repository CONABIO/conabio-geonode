import os
import argparse

import rasterio

from geonode_conabio.utils_docker import get_layer_and_style_registered_in_geonode_via_docker
from geonode_conabio.utils_style import get_cmap_from_element_list_madmex_style
from geonode_conabio.utils_parser import parse_sld_madmex_style
from geonode_conabio.utils_docker import create_link_in_geonode_for_zip_file_via_docker
from geonode_conabio.utils_os import zip_dir_for_layer_and_style
from geonode_conabio.wrappers import write_raster_with_cmap_in_dir

def arguments_parse():
    help = """
    
Wrapper to create link to download vector in geonode. Will put vector in directory zipped with style.

--------------
Example usage:
--------------

create_download_link_in_geonode_for_vector --title_layer "Test5 Samof MAD-MEX"
                                           --dir_path_layer /shared_volume/ftp_dir/
                                           --dir_path_styles_geonode /shared_volume/geonode/scripts/spcgeonode/_volume_geodatadir/workspaces/geonode/styles/
                                           --download_path ftp://geonode.conabio.gob.mx/pub/
"""
            
    parser = argparse.ArgumentParser(description=help,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--title_layer",
                    required=True,
                    default=None,
                    help="Title of layer in geonode.conabio.gob.mx")
    parser.add_argument("--dir_path_layer",
                    required=True,
                    default=None,
                    help="Directory path that will hold zip directory")
    parser.add_argument("--dir_path_styles_geonode",
                    required=True,
                    default=None,
                    help="path of styles registered in geonode")
    parser.add_argument("--download_path",
                    required=True,
                    default=None,
                    help="Url for downloading zip dir")
    args = parser.parse_args()
    return args
def main():
    args = arguments_parse()
    title_layer = args.title_layer
    dir_path_layer = args.dir_path_layer
    dir_path_styles_geonode = args.dir_path_styles_geonode
    download_path = args.download_path
    
    #get layer and style paths
    result_get = get_layer_and_style_registered_in_geonode_via_docker(title_layer)
    print(result_get)
    
    layer_name, style_name = result_get.decode().split("\n")[0:2]
    
    style_source_path = os.path.join(dir_path_styles_geonode, style_name)
    style_source_path = ''.join([style_source_path, ".sld"])
    
    layer_source_path = os.path.join(dir_path_layer, layer_name)
    layer_source_path = ''.join([layer_source_path, ".gpkg"])
    
    if not os.path.exists(dir_path_layer):
        os.makedirs(dir_path_layer)

    #Zip dir        
    zip_file = os.path.join(dir_path_layer, layer_name)
    zip_file = ''.join([zip_file, ".zip"])
    
    zip_dir_for_layer_and_style(zip_file, layer_source_path, style_source_path) 
    #if success creating download link in geonode
    print(os.path.basename(zip_file))
    download_url = os.path.join(download_path, os.path.basename(zip_file))
    if os.path.exists(zip_file):
        create_link_in_geonode_for_zip_file_via_docker(download_url, title_layer)    


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
    
Wrapper to create link to download raster in geonode. Will write color map to raster and put it in directory zipped with style.

--------------
Example usage:
--------------

create_download_link_in_geonode_for_raster --title_layer "Test3 National land cover map 2015 32 classes 512 512"
                                           --destiny_path /shared_volume/ftp_dir/
                                           --dir_path_styles_geonode /shared_volume/geonode/scripts/spcgeonode/_volume_geodatadir/workspaces/geonode/styles/
                                           --dir_path_layers_geonode /shared_volume/geonode/scripts/spcgeonode/_volume_geodatadir/data/geonode/
                                           --downdload_path ftp://geonode.conabio.gob.mx/pub/
"""
            
    parser = argparse.ArgumentParser(description=help,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--title_layer",
                    required=True,
                    default=None,
                    help="Title of layer in geonode.conabio.gob.mx")
    parser.add_argument("--destiny_path",
                    required=True,
                    default=None,
                    help="Directory path that will hold zip directory")
    parser.add_argument("--dir_path_styles_geonode",
                    required=True,
                    default=None,
                    help="path of styles registered in geonode")
    parser.add_argument("--dir_path_layers_geonode",
                    required=True,
                    default=None,
                    help="path of layers registered in geonode")
    parser.add_argument("--download_path",
                    required=True,
                    default=None,
                    help="Url for downloading zip dir")    
    args = parser.parse_args()
    return args
def main():
    args = arguments_parse()
    title_layer = args.title_layer
    destiny_path = args.destiny_path
    dir_path_styles_geonode = args.dir_path_styles_geonode
    dir_path_layers_geonode = args.dir_path_layers_geonode
    download_path = args.download_path
    
    #get layer and style paths
    result_get = get_layer_and_style_registered_in_geonode_via_docker(title_layer)
    print(result_get)
    
    layer_name, style_name = result_get.decode().split("\n")[0:2]
    
    style_source_path = os.path.join(dir_path_styles_geonode, style_name)
    style_source_path = ''.join([style_source_path, ".sld"])
    
    layer_source_path = os.path.join(dir_path_layers_geonode, layer_name, layer_name)
    layer_source_path = ''.join([layer_source_path, ".geotiff"])
    
    if not os.path.exists(destiny_path):
        os.makedirs(destiny_path)

    sld_madmex_style = parse_sld_madmex_style(style_source_path)
    rgba_dict = get_cmap_from_element_list_madmex_style(sld_madmex_style)
    
    #Write cmap to raster
    
    layer_cmap_source_path = os.path.join(destiny_path, layer_name)
    layer_cmap_source_path = ''.join([layer_cmap_source_path, ".geotiff"])
    
    write_raster_with_cmap_in_dir(layer_source_path, layer_cmap_source_path, rgba_dict)
    
    #Zip file        
    zip_file = os.path.join(destiny_path, layer_name)
    zip_file = ''.join([zip_file, ".zip"])
    
    zip_dir_for_layer_and_style(zip_file, layer_cmap_source_path, style_source_path) 
    #if success creating download link in geonode
    print(os.path.basename(zip_file))
    download_url = os.path.join(download_path, os.path.basename(zip_file))
    if os.path.exists(zip_file):
        create_link_in_geonode_for_zip_file_via_docker(download_url, title_layer)

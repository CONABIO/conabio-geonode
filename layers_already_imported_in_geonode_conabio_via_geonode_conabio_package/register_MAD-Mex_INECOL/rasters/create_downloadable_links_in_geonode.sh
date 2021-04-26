#!/bin/bash

#title of layer already registered in geonode in $1

dir_path_styles="/LUSTRE/MADMEX/geonode_spc_volume/geonode/scripts/spcgeonode/_volume_geodatadir/workspaces/geonode/styles"
dir_path_layers="/LUSTRE/MADMEX/geonode_spc_volume/geonode/scripts/spcgeonode/_volume_geodatadir/data/geonode/"
download_path_ftp="ftp://geonode.conabio.gob.mx/pub"
destiny_path="/data/var/ftp/pub/"

create_download_link_in_geonode_for_raster --title_layer "$1" --destiny_path $destiny_path --dir_path_styles_geonode $dir_path_styles --dir_path_layers_geonode $dir_path_layers --download_path $download_path_ftp
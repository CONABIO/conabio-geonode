# Registration in geonode of Validation data (vectors)

Base dir:

```
/LUSTRE/MADMEX/bits/validation_data/sentinel2/2018/datos_finales/PUNTOS_DE_VALIDACION-2018
```

Shell script:

`register_validation_sentinel2.sh`

```
#!/bin/bash

#base dir in $1
#filename in $2

region="Mexico, North America, Latin America"
name="National_validation_MAD-Mex_sentinel2_lc_2018_31_classes"
title="National validation dataset for 31 land cover classes classification 2018"
kw="MAD-Mex, Sentinel2, WCS"
abstract="National validation dataset for automatic MAD-Mex land cover classification of 31 classes. Land cover sourced by Sentinel satellite 2018 images."

import_small_medium_size_vector --input_directory $1 --input_filename $2 --destiny_path /data/var/ftp/pub/ --list_attributes "" --region "$region" --name "$name" --title "$title" --abstract "$abstract" --key_words "$kw"

```

Command lines to register:

```
bash register_validation_sentinel2.sh /LUSTRE/MADMEX/bits/validation_data/sentinel2/2018/datos_finales/PUNTOS_DE_VALIDACION-2018 Puntos_de_Validacion_2018_Revisados.shp
```

# Update attributes & statistics, style.

# Create downloadable links for rasters:

Shell script:

`create_downloadable_links_in_geonode.sh`

```
#!/bin/bash

#title of layer already registered in geonode in $1

dir_path_styles="/LUSTRE/MADMEX/geonode_spc_volume/geonode/scripts/spcgeonode/_volume_geodatadir/workspaces/geonode/styles"
download_path_ftp="ftp://geonode.conabio.gob.mx/pub"
dir_path_layers="/data/var/ftp/pub/"

create_download_link_in_geonode_for_vector --title_layer "$1" --dir_path_layer $dir_path_layers --dir_path_styles_geonode $dir_path_styles --download_path $download_path_ftp
```



```
bash create_downloadable_links_in_geonode.sh "National validation dataset for 31 land cover classes classification 2018"
``` 
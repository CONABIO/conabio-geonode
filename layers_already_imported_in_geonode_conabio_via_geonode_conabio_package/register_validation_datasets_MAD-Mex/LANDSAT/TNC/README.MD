# Registration in geonode of validation data (vectors)


Base dir:

```
/LUSTRE/MADMEX/validation/eoss4tnc_chpyuc_20152016_validation
```

Shell script:

`register_validation_landsat8_chiapas.sh`

```
#!/bin/bash

#base dir in $1
#filename in $2

region="Chiapas, Mexico, North America, Latin America"
name="Validation_MAD-Mex_TNC_landsat8_chiapas_lc_2015_13_classes"
title="Validation dataset for 13 land cover classes classification for the state of Chiapas TNC 2015"
kw="TNC, MAD-Mex, Landsat8"
abstract="Validation dataset for automatic MAD-Mex land cover classification of Chiapas state using 13 classes classification scheme. Land cover sourced by Landsat8 2015 images. Attributes: predict: result of land cover classification, reference: interpreted value, mdr2015: RapidEye 2015 land cover classification, mdr2018: Sentinel2 2018 land cover classification."

import_small_medium_size_vector --input_directory $1 --input_filename $2 --destiny_path /data/var/ftp/pub/ --list_attributes "" --region "$region" --name "$name" --title "$title" --abstract "$abstract" --key_words "$kw"

```

Shell script:

`register_validation_landsat8_all_but_chiapas.sh`

```
#!/bin/bash

#base dir in $1
#filename in $2
#state in $3

region="$(echo $3), Mexico, North America, Latin America"
name="Validation_MAD-Mex_TNC_landsat8_$(echo $3|tr '[:upper:]' '[:lower:]'|sed -n 's/ /_/;p')_lc_2016_13_classes"
title="Validation dataset for 13 land cover classes classification for the state of $(echo $3) TNC 2016"
kw="TNC, MAD-Mex, Landsat8"
abstract="Validation dataset for automatic MAD-Mex land cover classification of $(echo $3) state using 13 classes classification scheme. Land cover sourced by Landsat8 2016 images. Attributes: predict: result of land cover classification, reference: interpreted value, mdr2015: RapidEye 2015 land cover classification, mdr2018: Sentinel2 2018 land cover classification."

import_small_medium_size_vector --input_directory $1 --input_filename $2 --destiny_path /data/var/ftp/pub/ --list_attributes "" --region "$region" --name "$name" --title "$title" --abstract "$abstract" --key_words "$kw"

```


Command lines to register:

```
bash register_validation_landsat8_chiapas.sh /LUSTRE/MADMEX/validation/eoss4tnc_chpyuc_20152016_validation landcover_validation_chiapas.shp
bash register_validation_landsat8_all_but_chiapas.sh /LUSTRE/MADMEX/validation/eoss4tnc_chpyuc_20152016_validation landcover_validation_quintanaroo.shp "Quintana Roo"
bash register_validation_landsat8_all_but_chiapas.sh /LUSTRE/MADMEX/validation/eoss4tnc_chpyuc_20152016_validation landcover_validation_campeche.shp "Campeche"
bash register_validation_landsat8_all_but_chiapas.sh /LUSTRE/MADMEX/validation/eoss4tnc_chpyuc_20152016_validation landcover_validation_yucatan.shp "Yucatan"
```

# Update attributes & statistics, style.

# Create downloadable links for vectors:

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
bash create_downloadable_links_in_geonode.sh "Validation dataset for 13 land cover classes classification for the state of Chiapas TNC 2015"
bash create_downloadable_links_in_geonode.sh "Validation dataset for 13 land cover classes classification for the state of Quintana Roo TNC 2016"
bash create_downloadable_links_in_geonode.sh "Validation dataset for 13 land cover classes classification for the state of Campeche TNC 2016"
bash create_downloadable_links_in_geonode.sh "Validation dataset for 13 land cover classes classification for the state of Yucatan TNC 2016"
``` 
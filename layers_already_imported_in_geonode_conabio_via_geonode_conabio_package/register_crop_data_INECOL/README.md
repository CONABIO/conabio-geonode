# Registration of crop data given by INECOL


Base dir:

```
/LUSTRE/MADMEX/training/cultivos/igamma_veracruz/entrega_1a_semana_febrero_2020/cultivos2019_normalized_string_attributes/
```

Shell script:

`register_crop_data_inecol.sh`

```
#!/bin/bash

#base dir in $1
#filename in $2

region="Veracruz, Mexico, North America, Latin America"
name="INECOL_crop_dataset_2019"
title="INECOL crop dataset for Veracruz state 2019"
kw="INECOL"
abstract="Crop dataset for Veracruz state generated by INECOL in 2019. Attributes: fecha, municipio, distritodr, ecoregion, zonadevida, cultivo, asociacion, x, y, observ."

import_small_medium_size_vector --input_directory $1 --input_filename $2 --destiny_path /data/var/ftp/pub/ --list_attributes "Fecha, Municipio, DistritoDR, Ecoregion, ZonadeVida, Cultivo, Asociacion, Observ" --region "$region" --name "$name" --title "$title" --abstract "$abstract" --key_words "$kw"
```

Command lines to register:

```
bash register_crop_data_inecol.sh /LUSTRE/MADMEX/training/cultivos/igamma_veracruz/entrega_1a_semana_febrero_2020/cultivos2019_normalized_string_attributes/ cultivos2019_normalized_string_attributes.shp
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
bash create_downloadable_links_in_geonode.sh "INECOL crop dataset for Veracruz state 2019"
```
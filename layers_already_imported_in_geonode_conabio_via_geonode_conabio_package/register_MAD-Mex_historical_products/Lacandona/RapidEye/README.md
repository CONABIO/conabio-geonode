# Registration in geonode of Lacandona land cover changes


Base dir:

```
/LUSTRE/MADMEX/products/landcoverchange/rapideye/2017_2018/lacandona_quarterly_monitoring/
```

Shell script:

`register_lacandona_quaterly_monitoring_rapideye.sh`

```
#!/bin/bash

#base dir in $1
#filename in $2

region="Mexico, Lacandona, North America, Latin America"
year=$(echo $2|cut -d"." -f1|cut -d"_" -f4)
time=$(echo $2|cut -d"." -f2)
name="MAD-Mex_rapideye_lacandona_lcc_$(echo $year)_$(echo $time)_quarter_21_classes"
title="Land cover change map for Lacandona jungle $(echo $year) $(echo $time) quarter 21 classes"
kw="MAD-Mex, RapidEye"
abstract="Land cover and land cover change mapping is sourced by RapidEye satellite images. A preprocessing step is performed for producing cloud and cloud shadow masks for all images. Land cover and land cover change for Lacandona region were produced using a classification scheme of seven land cover classes: forest, jungle, grassland, agriculture, human settlement, water and other (non vegetated). Final products were manually corrected and interpreted resulting in twenty one possible land cover changes. Land cover and land cover change is generated using a novel semi automated workflow based on time series processing and optimized training data generation. The workflow consists of the following procedures, including data acquisition, time series generation and processing, spectral clustering, training data generation and optimization, supervised object-based classifications, and geometry harmonization. Temporal metrics are used to extract land cover change. Labels for the changes are extracted for t0 from the reference map. Labels for t1 are classified using the same land cover workflow."

import_small_medium_size_vector --input_directory $1 --input_filename $2 --destiny_path /data/var/ftp/pub/ --list_attributes "nom_cmb" --region "$region" --name "$name" --title "$title" --abstract "$abstract" --key_words "$kw"

```

Command lines to register:

```
bash register_lacandona_quaterly_monitoring_rapideye.sh /LUSTRE/MADMEX/products/landcoverchange/rapideye/2017_2018/lacandona_quarterly_monitoring/ changes_selva_lacandona_2017.3.shp
bash register_lacandona_quaterly_monitoring_rapideye.sh /LUSTRE/MADMEX/products/landcoverchange/rapideye/2017_2018/lacandona_quarterly_monitoring/ changes_selva_lacandona_2017.4.shp
bash register_lacandona_quaterly_monitoring_rapideye.sh /LUSTRE/MADMEX/products/landcoverchange/rapideye/2017_2018/lacandona_quarterly_monitoring/ changes_selva_lacandona_2018.1.shp
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
bash create_downloadable_links_in_geonode.sh "Land cover change map for Lacandona jungle 2017 3 quarter 21 classes"
bash create_downloadable_links_in_geonode.sh "Land cover change map for Lacandona jungle 2017 4 quarter 21 classes"
bash create_downloadable_links_in_geonode.sh "Land cover change map for Lacandona jungle 2018 1 quarter 21 classes"
```


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

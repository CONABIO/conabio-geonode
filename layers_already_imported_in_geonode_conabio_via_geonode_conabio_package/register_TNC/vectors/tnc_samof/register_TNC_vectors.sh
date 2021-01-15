#!/bin/bash

#base dir in $1
#filename in $2

state_code=$(echo $2|sed -n 's/.*madmexplus_\(.*\).shp/\1/;p')
state=$(echo $state_code|grep $state_code name_equivalency.txt|cut -d' ' -f2)
year=$(echo $2|sed -n 's/.*_landsat8_\(.*\)_2020.*/\1/;p')
region="$(echo $state), Mexico, North America, Latin America"
name="MAD-Mex_TNC_landsat8_$(echo $state)_lcc_$(echo $year)_40_classes"
title="Land cover change map for the state of $(echo $state) TNC $(echo $year) 40 classes"
kw="MAD-Mex, Landsat8"
abstract="Land cover and land cover change mapping is sourced by Landsat 8 satellite images. All available images for the required calendar years were acquired through the ESPA processing system and were provided as atmospherically corrected surface reflectance and are accompanied by quality layers assigning, amongst others, pixels obscured by clouds and cloud shadows. For the 7 granules (path/rows) covering Chiapas, 155 Landsat-8 scenes of 2015 were acquired. The 17 granules covering the peninsula of Yucatan delivered 381 Landsat-8 scenes. For 2019, a total of 543 scenes were acquired. Land cover and land cover change is generated using a novel semi automated workflow based on time series processing and optimized training data generation. The workflow consists of the following procedures, including data acquisition, time series generation and processing, spectral clustering, training data generation and optimization, supervised object-based classifications, and geometry harmonization. Temporal metrics are used to extract land cover change. Labels for the changes are extracted for t0 from the reference map. Labels for t1 are classified using the same land cover workflow."

echo $state

echo $1
echo $2

/home/geonode_user/.local/bin/import_small_medium_size_vector --base_directory $1 --input_filename $2 --list_attributes "class, class_t0, ipccdsc, ipccdsc_t0" --region "$region" --name "$name" --title "$title" --abstract "$abstract" --key_words "$kw"


#!/bin/bash

#base dir in $1
#filename in $2
#state in $3

state=$3
region="$(echo $state), Mexico, North America, Latin America"
name="MAD-Mex_iGamma_landsat8_$(echo $state|tr "[:upper:]" "[:lower:]")_agric_lc_2019_4_classes"
echo $name
echo $region
title="Agriculture land cover map for the state of $(echo $state) iGamma 2019 4 classes"
kw="MAD-Mex, Landsat8, GeoTIFF"
abstract="Land cover sourced by Landsat8 satellite images. All available images for the required calendar years were acquired through the ESPA processing system and were provided as atmospherically corrected surface reflectance and are accompanied by quality layers assigning, amongst others, pixels obscured by clouds and cloud shadows. For the 12 granules (path/rows) covering Veracruz, 267 Landsat-8 scenes of 2019 were acquired. The 7 granules covering the Michoacán delivered 158 Landsat-8 scenes. Land cover is generated using a novel semi automated workflow based on time series processing and optimized training data generation. The workflow consists of the following procedures, including data acquisition, time series generation and processing, spectral clustering, training data generation and optimization, supervised object-based classifications, and geometry harmonization."

echo $1
echo $2

import_raster --input_directory $1 --input_filename $2 --region "$region" --name "$name" --title "$title" --abstract "$abstract" --key_words "$kw"
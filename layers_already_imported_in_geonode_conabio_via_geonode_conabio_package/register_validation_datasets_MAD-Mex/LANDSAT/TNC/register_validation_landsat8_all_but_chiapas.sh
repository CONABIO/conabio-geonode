#!/bin/bash

#base dir in $1
#filename in $2
#state in $3

region="$(echo $3), Mexico, North America, Latin America"
name="Validation_MAD-Mex_TNC_landsat8_$(echo $3|tr '[:upper:]' '[:lower:]'|sed -n 's/ /_/;p')_lc_2016_13_classes"
title="Validation dataset for 13 land cover classes classification for the state of $(echo $3) TNC 2016"
kw="MAD-Mex, Landsat8"
abstract="Validation dataset for automatic MAD-Mex land cover classification of $(echo $3) state using 13 classes classification scheme. Land cover sourced by Landsat8 2016 images. Attributes: predict: result of land cover classification, reference: interpreted value, mdr2015: RapidEye 2015 land cover classification, mdr2018: Sentinel2 2018 land cover classification."

import_small_medium_size_vector --input_directory $1 --input_filename $2 --destiny_path /data/var/ftp/pub/ --list_attributes "" --region "$region" --name "$name" --title "$title" --abstract "$abstract" --key_words "$kw"
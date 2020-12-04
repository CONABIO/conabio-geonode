#!/bin/bash

#base dir in $1
#filename in $2

region="Mexico, North America, Latin America"
name="National_validation_MAD-Mex_rapideye_lc_2015_31_classes"
title="National validation dataset for 31 land cover classes classification 2015"
kw="MAD-Mex, RapidEye, WCS"
abstract="National validation dataset for automatic MAD-Mex land cover classification of 31 classes. Land cover sourced by RapidEye satellite 2015 images."

import_small_medium_size_vector --input_directory $1 --input_filename $2 --destiny_path /data/var/ftp/pub/ --list_attributes "edo" --region "$region" --name "$name" --title "$title" --abstract "$abstract" --key_words "$kw"
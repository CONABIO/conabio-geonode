#!/bin/bash

#base dir in $1
#filename in $2

level=$(echo $2|sed -n 's/.*_2019_\(.*\)_final.*/\1/;p')
if [ $level == "nivel1" ]; then
  classes="8"
else
  classes="13"
fi
year=2018_2019
region="Marismas Nacionales, Mexico, North America, Latin America"
name="MAD-Mex_TNC_marismas_nacionales_landsat8_rapideye_lc_$(echo $year)_$(echo $classes)_classes"
title="Cobertura de suelo TNC marismas nacionales 2018, 2019 $(echo $classes) clases"
kw="MAD-Mex, Landsat8, RapidEye, GeoTIFF, WCS"
abstract="El mapa de cobertura de suelo 2018, 2019 en la region de marismas nacionales, es un producto geografico digital generado a partir de imagenes RapidEye (2019) complementadas con imagenes Landsat8 (2018). Encierra informacion en base a una clasificacion realizada por MAD-Mex de 8 y 13 grupos de coberturas de vegetacion y usos. Es el resultado de 2 procesos basicos; por un lado una clasificacion automatizada y posteriormente una revision, analisis, correccion y ajuste de esa operacion. La ordenacion o agrupamiento en 8 y 13 clases se basa en la clasificacion de los tipos de vegetacion y usos de suelo del pais que establece el INEGI. Se representan conjuntos de elementos que sobre el terreno son equivalentes o mayores a 0.5 Has. Se realizo una estimacion de exactitud del mapa de cobertura de suelo usando un conjunto de 1043 objetos aleatorios. Se evaluaron las 8 clases MAD-Mex. La exactitud global calcula 78.72%. Las precisiones de las clases (PPV, Precision or positive predictive value) se calculan 93.92% (Manglar y Peten), 83.72% (Tierras Agricolas), 96.3% (Urbano y Construido), 85.31% (Agua), 58.33% (Selva Baja Caducifolia Subcaducifolia y Matorral Subtropical con mayores confusiones con Tierras Agricolas de plantaciones y boques inducidos), 39.29% (Vegetacion Halofila Hidrofila con mayores confusiones con Suelos Desnudos y Pastizales), 50.62% (Pastizales con mayores confusiones con Tierras Agricolas) y 57.90% (Suelo Desnudo con mayores confusiones con Tierras Agricolas y Urbano y Construido) "

echo $name
echo $classes
echo $1
echo $2

/home/geonode_user/.local/bin/import_raster --base_directory $1 --input_filename $2 --region "$region" --name "$name" --title "$title" --abstract "$abstract" --key_words "$kw"
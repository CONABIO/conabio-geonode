# Registration in geonode of TNC data (vectors)

## Note: this README is using implementation of geonode_conabio package before (including) [commit](https://github.com/CONABIO/geonode/tree/30a00684011bcc80e68d4b98242920cafd1c7dc3)

Base dir:

```
/LUSTRE/MADMEX/tnc_data_steffen_thilo/tnc_marismas/
```

Shell script:

`register_TNC_vectors.sh`

```
#!/bin/bash

#base dir in $1
#filename in $2

year=2011_2019
region="Marismas Nacionales, Mexico, North America, Latin America"
name="MAD-Mex_TNC_marismas_nacionales_landsat8_rapideye_lcc_$(echo $year)"
title="Cambio de cobertura de suelo TNC marismas nacionales 2011, 2019 13 clases"
kw="MAD-Mex, Landsat8, RapidEye, GeoTIFF, WCS"
abstract="El mapa de cambio de cobertura del suelo 2019 en la region de marismas nacionales, es un producto geografico digital generado a partir de una clasificacion orientada a objetos automatica de las imagenes RapidEye 2011. El espacio de caracteristicas para cada objeto se calculo usando las bandas espectrales RapidEye y las metricas percentiles calculadas por los NDVI, NDWI, NDSI y BSI de las series de tiempo de sensores Landsat5 y Landsat7 del año 2011. Se uso el mapa de cobertura 2019 para datos de entrenamiento. Los mapas de cobertura 2011 y 2019 son complementados con imagenes Landsat (2018). Esta informacion se basa en una clasificacion realizada por MAD-Mex de 8 grupos de coberturas de vegetacion y 5 subclases que son porciones del territorio estatal, la flora representada conlleva entornos ecologicos, floristicos y de distribucion geografica coherentes; es el resultado de 2 procesos basicos; por un lado una clasificacion automatizada y posteriormente una revision, analisis, correccion y ajuste de esa operacion, la ordenacion o agrupamiento en 8 clases y 5 subclases, se basa en la clasificacion de los tipos de vegetacion y sus de suelo del pais que establece el INEGI. Se representan conjuntos de elementos que sobre el terreno son equivalentes o mayores a 0.5 Has. En la primera tarea se aplico una deteccion automatica a las imagenes RapidEye de años 2011 y 2019. Los cambios detectados junto con la informacion de cobertura de suelo clasificada en 2011 y 2019 se combinan con los objetos segmentados en 2019 que presentan un sobrelapamiento sustancial con los cambios detectados. Al nivel de area de interes quedaron 236,289 objetos de cambios potenciales. Aplicando un filtro automatico de clases de cobertura 2011 vs 2019 a los objetos de cambio conservados, 102,899 objetos de cambio al nivel 2 del esquema de clasificacion de cobertura y 95,612 objetos al nivel 1. En esta filtracion se eliminaron objetos de no cambio y cambios imposibles. En consecuencia, tambien se eliminaron cambios de subclases arborea, desprovisto o periodico; es decir, solo quedaron los cambios con diferentes clases de cobertura al nivel 1 en 2011 y 2019. Aplicando una unidad minima de mapeo para la revision manual por los expertos de interpretacion."

echo $name
echo $1
echo $2

/home/geonode_user/.local/bin/import_small_medium_size_vector --base_directory $1 --input_filename $2 --list_attributes "nombre01t1, nombre01t2, cambio01" --region "$region" --name "$name" --title "$title" --abstract "$abstract" --key_words "$kw"

```

Command lines to register:

```
bash register_TNC_vectors.sh /LUSTRE/MADMEX/tnc_data_steffen_thilo/tnc_marismas/ marismasnacionales_cambiodecoberturadesuelo_2011-2019_final_20190925.gpkg

```

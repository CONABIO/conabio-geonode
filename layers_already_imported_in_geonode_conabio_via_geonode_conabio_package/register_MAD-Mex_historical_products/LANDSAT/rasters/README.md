
# Registration in geonode of MAD-Mex LANDSAT products (rasters)

Base dir:

```
/LUSTRE/MADMEX/products/landcover/landsat/
```

Shell script:

`register_MAD-Mex_rasters.sh`

```
#!/bin/bash

#base dir in $1
#filename in $2
#sensor in $3
#number of classes in $4

year=$(echo $1|cut -d'/' -f7)
region="Mexico, North America, Latin America"
name="National_MAD-Mex_$(echo $3|tr "[:upper:]" "[:lower:]")_lc_$(echo $year)_$(echo $4)_classes"
title="National land cover map $(echo $year) $(echo $4) classes"
kw="MAD-Mex, $(echo $3), GeoTIFF"
abstract="Land cover sourced by $(echo $3) satellite images. All available images for the required calendar years were acquired through the ESPA processing system and were provided as atmospherically corrected surface reflectance and are accompanied by quality layers assigning, amongst others, pixels obscured by clouds and cloud shadows. Land cover is generated using a novel semi automated workflow based on time series processing and optimized training data generation. The workflow consists of the following procedures, including data acquisition, time series generation and processing, spectral clustering, training data generation and optimization, supervised object-based classifications, and geometry harmonization. "

echo $1
echo $2

import_raster --input_directory $1 --input_filename $2 --region "$region" --name "$name" --title "$title" --abstract "$abstract" --key_words "$kw"

```


Command lines to register:

```
bash register_MAD-Mex_rasters.sh /LUSTRE/MADMEX/products/landcover/landsat/2015/32/ madmex_lc_2015.tif Landsat8 32
bash register_MAD-Mex_rasters.sh /LUSTRE/MADMEX/products/landcover/landsat/2017/31/ madmex_landsat_2017_31.tif Landsat8 31
bash register_MAD-Mex_rasters.sh /LUSTRE/MADMEX/products/landcover/landsat/2018/31/ madmex_landsat_2018_31.tif Landsat8 31

```

# Update style, attributes & statistics, thumbnail.

# Create downloadable links for rasters:

Shell script:

`create_downloadable_links_in_geonode.sh`

```
bash create_downloadable_links_in_geonode.sh "National land cover map 2015 32 classes"
bash create_downloadable_links_in_geonode.sh "National land cover map 2017 31 classes"
bash create_downloadable_links_in_geonode.sh "National land cover map 2018 31 classes"
```
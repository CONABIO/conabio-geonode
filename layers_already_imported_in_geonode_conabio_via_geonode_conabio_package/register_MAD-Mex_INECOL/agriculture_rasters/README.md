
# Registration in geonode of MAD-Mex INECOL iGamma products (agriculture rasters)

Base dir:

```
/LUSTRE/MADMEX/inecol_data_steffen_thilo/
```

And:

https://public.eoss.cloud/projects/inecol/web/dashboard.html


Shell script:

`register_agriculture_MAD-Mex_INECOL_rasters.sh`

```
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

```


Command lines to register:

```
bash register_agriculture_MAD-Mex_INECOL_rasters.sh /LUSTRE/MADMEX/inecol_data_steffen_thilo/eoss4inecol_landcover_landsat8_2019_MIC_agricultura_20200831_raster eoss4inecol_landcover_landsat8_2019_MIC_agricultura_tag1_20200831.tif Michoacan

bash register_agriculture_MAD-Mex_INECOL_rasters.sh /LUSTRE/MADMEX/inecol_data_steffen_thilo/eoss4inecol_landcover_landsat8_2019_VER_agricultura_cultivos_20200916/ eoss4inecol_landcover_landsat8_2019_VER_agricultura_20200916.tif Veracruz
```

# Update style, attributes & statistics, thumbnail.

# Create downloadable links for rasters:

Shell script:

`create_downloadable_links_in_geonode.sh`


```
bash create_downloadable_links_in_geonode.sh "Agriculture land cover map for the state of Michoacan iGamma 2019 4 classes"
bash create_downloadable_links_in_geonode.sh "Agriculture land cover map for the state of Veracruz iGamma 2019 4 classes"

```

# Crops

Shell script:

`register_crops_MAD-Mex_INECOL_rasters.sh`

```
#!/bin/bash

#base dir in $1
#filename in $2
#state in $3

state=$3
region="Veracruz, Mexico, North America, Latin America"
name="MAD-Mex_iGamma_landsat8_veracruz_crops_lc_2019_16_classes"
echo $name
echo $region
title="Crop cultivation land cover map for the state of Veracruz iGamma 2019 16 classes"
kw="MAD-Mex, Landsat8, GeoTIFF"
abstract="Land cover sourced by Landsat8 satellite images. All available images for the required calendar years were acquired through the ESPA processing system and were provided as atmospherically corrected surface reflectance and are accompanied by quality layers assigning, amongst others, pixels obscured by clouds and cloud shadows. For the 12 granules (path/rows) covering Veracruz, 267 Landsat-8 scenes of 2019 were acquired. The 7 granules covering the Michoacán delivered 158 Landsat-8 scenes. Land cover is generated using a novel semi automated workflow based on time series processing and optimized training data generation. The workflow consists of the following procedures, including data acquisition, time series generation and processing, spectral clustering, training data generation and optimization, supervised object-based classifications, and geometry harmonization. For the state of Veracruz field samples of crop cultures were provided by INECOL in the frame of field work conducted in the iGamma project. A total of 26347 samples was collected featuring 15 different crops of which 21185 samples showed sufficient quality to be used in the effort. These had been collected in the year 2019 and had a unique spatial relation to the segmented objects of the land cover map."

echo $1
echo $2

import_raster --input_directory $1 --input_filename $2 --region "$region" --name "$name" --title "$title" --abstract "$abstract" --key_words "$kw"

```


Command lines to register:

```
bash register_crops_MAD-Mex_INECOL_raster.sh /LUSTRE/MADMEX/inecol_data_steffen_thilo/eoss4inecol_landcover_landsat8_2019_VER_agricultura_cultivos_20200916/ eoss4inecol_landcover_landsat8_2019_VER_agricultura_cultivos_20200916.tif
```

# Update style, attributes & statistics, thumbnail.

# Create downloadable links for rasters:

Shell script:

`create_downloadable_links_in_geonode.sh`


```
bash create_downloadable_links_in_geonode.sh "Crop cultivation land cover map for the state of Veracruz iGamma 2019 16 classes"

```
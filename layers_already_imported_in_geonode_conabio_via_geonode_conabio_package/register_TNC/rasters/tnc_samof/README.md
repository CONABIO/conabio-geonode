
# Registration in geonode of TNC data (rasters)

Base dir:

```
/LUSTRE/MADMEX/tnc_data_steffen_thilo/tnc_samof/landcover/
```

Shell script:

`register_TNC_rasters.sh`

```
#!/bin/bash

#base dir in $1
#filename in $2

state_code=$(echo $2|sed -n 's/.*madmexplus_\(.*\).tif/\1/;p')
state=$(echo $state_code|grep $state_code name_equivalency.txt|cut -d' ' -f2)
year=$(echo $2|sed -n 's/.*_landsat8_\(.*\)_2020.*/\1/;p')
region="$(echo $state), Mexico, North America, Latin America"
name="MAD-Mex_TNC_landsat8_$(echo $state)_lc_$(echo $year)_40_classes"
title="Land cover map for the state of $(echo $state) TNC $(echo $year) 40 classes"
kw="MAD-Mex, Landsat8, GeoTIFF, WCS"
abstract="Land cover and land cover change mapping is sourced by Landsat 8 satellite images. All available images for the required calendar years were acquired through the ESPA processing system and were provided as atmospherically corrected surface reflectance and are accompanied by quality layers assigning, amongst others, pixels obscured by clouds and cloud shadows. For the 7 granules (path/rows) covering Chiapas, 155 Landsat-8 scenes of 2015 were acquired. The 17 granules covering the peninsula of Yucatan delivered 381 Landsat-8 scenes. For 2019, a total of 543 scenes were acquired. Land cover and land cover change is generated using a novel semi automated workflow based on time series processing and optimized training data generation. The workflow consists of the following procedures, including data acquisition, time series generation and processing, spectral clustering, training data generation and optimization, supervised object-based classifications, and geometry harmonization. Temporal metrics are used to extract land cover change. Labels for the changes are extracted for t0 from the reference map. Labels for t1 are classified using the same land cover workflow."

echo $state
echo $1
echo $2

/home/geonode_user/.local/bin/import_raster --base_directory $1 --input_filename $2 --region "$region" --name "$name" --title "$title" --abstract "$abstract" --key_words "$kw"
```


Command lines to register:

```
bash register_TNC_rasters.sh /LUSTRE/MADMEX/tnc_data_steffen_thilo/tnc_samof/landcover/ eoss4tnc_landcover_landsat8_2015_20200220_auxlabel_madmexplus_CHP.tif
bash register_TNC_rasters.sh /LUSTRE/MADMEX/tnc_data_steffen_thilo/tnc_samof/landcover/ eoss4tnc_landcover_landsat8_2016_20200220_auxlabel_madmexplus_CAM.tif
bash register_TNC_rasters.sh /LUSTRE/MADMEX/tnc_data_steffen_thilo/tnc_samof/landcover/ eoss4tnc_landcover_landsat8_2016_20200220_auxlabel_madmexplus_QRO.tif
bash register_TNC_rasters.sh /LUSTRE/MADMEX/tnc_data_steffen_thilo/tnc_samof/landcover/ eoss4tnc_landcover_landsat8_2016_20200220_auxlabel_madmexplus_YUC.tif
bash register_TNC_rasters.sh /LUSTRE/MADMEX/tnc_data_steffen_thilo/tnc_samof/landcover/ eoss4tnc_landcover_landsat8_2019_20200313_madmexplus_CAM.tif
bash register_TNC_rasters.sh /LUSTRE/MADMEX/tnc_data_steffen_thilo/tnc_samof/landcover/ eoss4tnc_landcover_landsat8_2019_20200313_madmexplus_CHP.tif
bash register_TNC_rasters.sh /LUSTRE/MADMEX/tnc_data_steffen_thilo/tnc_samof/landcover/ eoss4tnc_landcover_landsat8_2019_20200313_madmexplus_QRO.tif
bash register_TNC_rasters.sh /LUSTRE/MADMEX/tnc_data_steffen_thilo/tnc_samof/landcover/ eoss4tnc_landcover_landsat8_2019_20200313_madmexplus_YUC.tif
```

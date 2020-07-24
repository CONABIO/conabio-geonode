# Import new layers


* TNC

    * Check: `/LUSTRE/MADMEX/tnc_data_steffen_thilo/`

    * https://public.eoss.cloud/projects/tnc/web/dashboard.html
    
Downloaded: 

`/LUSTRE/MADMEX/tnc_data_steffen_thilo/tnc_samof/eoss_tnc_lclcc_chiapas_yucatan_report_20200320.pdf`

Example of register:

`/LUSTRE/MADMEX/tnc_data_steffen_thilo/eoss4tnc_landcover_landsat8_2019_20200313_madmexplus_CHP.tif`

with sld:

`/LUSTRE/MADMEX/tnc_data_steffen_thilo/tnc_samof/landcover/mexico_landcover_31_raster.sld`

```
.local/bin/import_raster --base_directory /LUSTRE/MADMEX/tnc_data_steffen_thilo/tnc_samof/landcover/ --input_filename eoss4tnc_landcover_landsat8_2019_20200313_madmexplus_CHP.tif --region "Chiapas, Mexico, North America, Latin America" --name "MAD-Mex_TNC_landsat8_Chiapas_lc_2019_48" --title "Land cover map for the state of Chiapas TNC 2019" --abstract "Land cover and land cover change mapping is sourced by Landsat 8 satellite images. All available images for the required calendar years were acquired through the ESPA processing system and were provided as atmospherically corrected surface reflectance and are accompanied by quality layers assigning, amongst others, pixels obscured by clouds and cloud shadows. For the 7 granules (path/rows) covering Chiapas, 155 Landsat-8 scenes of 2015 were acquired. Land cover and land cover change is generated using a novel semi automated workflow based on time series processing and optimized training data generation. The workflow consists of the following procedures, including data acquisition, time series generation and processing, spectral clustering, training data generation and optimization, supervised object-based classifications, and geometry harmonization. Temporal metrics are used to extract land cover change. Labels for the changes are extracted for t0 from the reference map. Labels for t1 are classified using the same land cover workflow." --key_words "MAD-Mex, Landsat8, GeoTIFF, WCS"

```


Example of register vectorfile (without sld):


```
.local/bin/import_small_medium_size_vector --base_directory /LUSTRE/MADMEX/tnc_data_steffen_thilo/tnc_samof/landcoverchanges/ --input_filename eoss4tnc_landcoverchanges_landsat8_2015-2019_20200313_madmexplus_CHP.shp --list_attributes "class, class_t0, ipccdsc, ipccdsc_t0" --region "Chiapas, Mexico, North America, Latin America" --name "MAD-Mex_TNC_landsat8_Chiapas_lcc_2019_48" --title "Land cover change map for the state of Chiapas TNC 2019" --abstract "Land cover and land cover change mapping is sourced by Landsat 8 satellite images. All available images for the required calendar years were acquired through the ESPA processing system and were provided as atmospherically corrected surface reflectance and are accompanied by quality layers assigning, amongst others, pixels obscured by clouds and cloud shadows. For the 7 granules (path/rows) covering Chiapas, 155 Landsat-8 scenes of 2015 were acquired. Land cover and land cover change is generated using a novel semi automated workflow based on time series processing and optimized training data generation. The workflow consists of the following procedures, including data acquisition, time series generation and processing, spectral clustering, training data generation and optimization, supervised object-based classifications, and geometry harmonization. Temporal metrics are used to extract land cover change. Labels for the changes are extracted for t0 from the reference map. Labels for t1 are classified using the same land cover workflow." --key_words "MAD-Mex, Landsat8, GeoTIFF, WCS"

```




* MAD-Mex

    * Maps of 2017, 2018 LANDSAT and Sentinel2
    * For larger vector and raster maps (>1 gb) restrict permissions because downloading process takes too much time that crashes geonode. For this use as a reference next command:
    
```
DJANGO_SETTINGS_MODULE=geonode.local_settings python manage.py set_layers_permissions -r chihuahua_merge_wgs84 -p d -u AnonymousUser -g anonymous
Initial permissions info for the resource chihuahua_merge_wgs84:
{'users': {<Profile: super>: ['view_resourcebase', 'download_resourcebase', 'change_resourcebase_metadata', 'change_resourcebase', 'delete_resourcebase', 'change_resourcebase_permissions', 'publish_resourcebase', 'change_layer_data', 'change_layer_style']}, 'groups': {<Group: anonymous>: ['download_resourcebase', 'view_resourcebase']}}
Final permissions info for the resource chihuahua_merge_wgs84:
{'users': {<Profile: super>: ['view_resourcebase', 'download_resourcebase', 'change_resourcebase_metadata', 'change_resourcebase', 'delete_resourcebase', 'change_resourcebase_permissions', 'publish_resourcebase', 'change_layer_data', 'change_layer_style'], <Profile: AnonymousUser>: ['view_resourcebase', 'download_resourcebase']}, 'groups': {<Group: anonymous>: ['view_resourcebase', 'download_resourcebase']}}
Permissions successfully updated!
```
    
    



# Create users such as Pedro and Mariana

* Use https://docs.geonode.org/en/master/usage/accounts_user_profile/index.html

* Also ask them to follow some kind of guide to import layers into geonode via UI

    * Use https://docs.geonode.org/en/master/usage/managing_layers/uploading_layers.html 
    * **The layers must be in wgs84 projection! and not be large in size (< 100 mb)
    

When they create users they can upload and edit metadata and layers.

If I want to give permissions to an user in particular to edit metadata then i need to create group and then modify layer permissions using this group. See: 

```
DJANGO_SETTINGS_MODULE=geonode.local_settings python manage.py set_layers_permissions -r chihuahua_merge_wgs84 -p d -u AnonymousUser -g anonymous
Initial permissions info for the resource chihuahua_merge_wgs84:
{'users': {<Profile: super>: ['view_resourcebase', 'download_resourcebase', 'change_resourcebase_metadata', 'change_resourcebase', 'delete_resourcebase', 'change_resourcebase_permissions', 'publish_resourcebase', 'change_layer_data', 'change_layer_style']}, 'groups': {<Group: anonymous>: ['download_resourcebase', 'view_resourcebase']}}
Final permissions info for the resource chihuahua_merge_wgs84:
{'users': {<Profile: super>: ['view_resourcebase', 'download_resourcebase', 'change_resourcebase_metadata', 'change_resourcebase', 'delete_resourcebase', 'change_resourcebase_permissions', 'publish_resourcebase', 'change_layer_data', 'change_layer_style'], <Profile: AnonymousUser>: ['view_resourcebase', 'download_resourcebase']}, 'groups': {<Group: anonymous>: ['view_resourcebase', 'download_resourcebase']}}
Permissions successfully updated!
```

or:

https://docs.geonode.org/en/master/basic/permissions/


or modify `geonode/settings.py`

```
ADMIN_MODERATE_UPLOADS = ast.literal_eval(os.environ.get('ADMIN_MODERATE_UPLOADS', 'True'))

RESOURCE_PUBLISHING = ast.literal_eval(os.getenv('RESOURCE_PUBLISHING', 'True'))
```

When they create users they can upload and edit metadata and layers but will not be published. Admin needs to approve and publish via django UI. See [django_approve_and_publish_layer](https://github.com/CONABIO/geonode/blob/issues-6-8/deployment_in_geonode_conabio/django_approve_and_publish_layer.png)
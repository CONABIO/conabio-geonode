**Next examples were registered via [geonode_conabio](../ptyhon3_package_for_geonode/) package**

# MAD-Mex layers for TNC project

Check: `/LUSTRE/MADMEX/tnc_data_steffen_thilo/` and https://public.eoss.cloud/projects/tnc/web/dashboard.html

Some documentation that helped:

`/LUSTRE/MADMEX/tnc_data_steffen_thilo/tnc_samof/eoss_tnc_lclcc_chiapas_yucatan_report_20200320.pdf`






* MAD-Mex

Maps of 2017, 2018 LANDSAT and Sentinel2
    

    



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

When they create users they can upload and edit metadata and layers but will not be published. Admin needs to approve and publish via django UI.
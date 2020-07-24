# Registration of users using UI of geonode

Find instructions for the registration of users via UI of geonode within [accounts_user_profile](https://docs.geonode.org/en/master/usage/accounts_user_profile/index.html) doc. 

# Upload of layers once you have registered as user in geonode via UI

To upload layers via UI of geonode, make sure they are **less than 100 MB and in [WGS84](https://spatialreference.org/ref/epsg/wgs-84/)**. If your layer is above 100 MB please go to [instructions_to_upload_layers_to_geonode_using_docker](../instructions_to_upload_layers_to_geonode_using_docker) and request support to admin.

**Notes:** 

* Once you have uploaded a layer it needs to be approved and published by admin. See [django_approve_and_publish_layer](django_approve_and_publish_layer.png)

* If admin approves and publish your layer and you can't see active the **download button**, then log in, select the layer which you want to download and press the **update attributes and statistics button**. See for example [issues/4308](https://github.com/GeoNode/geonode/issues/4308).




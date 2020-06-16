# Register users using UI of geonode

We can find instructions for the registration of users via UI of geonode within [accounts_user_profile](https://docs.geonode.org/en/master/usage/accounts_user_profile/index.html) doc. 

# Upload layer once you have registered in geonode via UI

To upload layers via UI of geonode, make sure are **less than 100 MB and in [WGS84](https://spatialreference.org/ref/epsg/wgs-84/)**. If your layer is above 100 MB please go to [instructions_to_upload_layers_to_geonode_using_docker](../instructions_to_upload_layers_to_geonode_using_docker) and request support to admin.

**Notes:** 

* Deployment of geonode at CONABIO is configured so when a user registers in geonode and uploads a layer, this layer is not approved and publish immediatly. Admin needs to approved and publish each layer.

* If admin approves and publish your layer and you can't see active the **download button** then log in, select the layer which you want to download and then press the **update attributes and statistics button**. See [issues/4308](https://github.com/GeoNode/geonode/issues/4308)




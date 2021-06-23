# conabio-geonode spc


See [spcgeonode](https://github.com/GeoNode/geonode/blob/master/scripts/spcgeonode/)


GeoNode with docker-compose

Steps to deploy geonode with `docker-compose`. 

1) **Clone repository**

```
git clone --single-branch -b master https://github.com/GeoNode/geonode.git
```

2) **Override `.yml` with your IP:**

```
cd geonode/scripts/spcgeonode
#modify .env in entries:

HTTP_HOST=<nodo7.conabio.gob.mx>
ADMIN_EMAIL=admin@geonodeservices.conabio.gob.mx
```

3) Modification of path `/var/lib/docker` for `dockerd` and **Docker compose up**

**Note: make sure to mount volumes in `docker-compose.yml` for django container:**

**Mount `/LUSTRE/MADMEX`:**

```
sudo mount -a #edit /etc/fstab with entry for mounting /LUSTRE/MADMEX
```

Next steps following [how-to-change-var-lib-docker-directory-with-overlay2](https://forums.docker.com/t/how-to-change-var-lib-docker-directory-with-overlay2/43620/2)

**Create in geonode machine being root:**

```
mkdir /data/var/lib/docker
```

**Copy:**

```
cp -rpa /var/lib/docker /data/var_lib_docker/
```

**Stop:**

```
service docker stop
```

**Edit:**

```
/etc/docker/daemon.json
```

**with contents**

```
{
"data-root": "/data/var/lib/docker"
}
```

**Start:**

```
service start docker
```

**Modify `docker-compose.yml` inside `geonode/scripts/spcgeonode` dir modify where `image: geonode/spcgeonode:django-3.0` is:**

```
...volumes:
    - static:/spcgeonode-static/
    - media:/spcgeonode-media/
    - /LUSTRE/MADMEX:/LUSTRE/MADMEX
```

**Docker compose up:**

```
#just the essential:
docker-compose up -d django geoserver postgres nginx

#building images: 
docker-compose up --build -d django geoserver postgres nginx

```

**Check with:**

```
docker-compose logs -f
```

**Check deployment of geonode and geoserver going to browser:**

```
<miip>
<miip>geoserver/web/
```

4) **Copy local settings and fix header of it:**

Enter to docker container `spcgeonode_django_1`:

```
docker exec -it spcgeonode_django_1 /bin/bash
```

Install some useful cmd lines

```
apt-get update && apt-get install -y vim less nano unzip postgis
```

Once inside of docker container copy local settings to configure and use them later:

```
cp /spcgeonode/package/support/geonode.local_settings geonode/local_settings.py
```

Change localhost to ip and set password of DB:


```
myip=<here put your IP or DNS such as coreos.conabio.gob.mx>
sed -i "s/localhost/$myip/g" geonode/local_settings.py
sed -i 's/THE_DATABASE_PASSWORD/geonode/g' geonode/local_settings.py
sed -i "s/MIDDLEWARE_CLASSES/MIDDLEWARE/g" geonode/local_settings.py

#Modify for geonode/local_settings.py:
---
#from urlparse import urlparse, urlunparse
try:
    from urlparse import urlparse, urlunparse
except ImportError:
    from urllib.parse import urlparse, urlunparse
---
#or:
---
try:  # python2
    from urlparse import urlparse, urlunparse, urlsplit, urljoin
except ImportError:
    # Python 3 fallback
    from urllib.parse import urlparse, urlunparse, urlsplit, urljoin
---


#Modify for geonode/local_settings.py:
#INSTALLED_APPS += ('geonode_mapstore_client', )

```

5) Change domain `example.com`

If you want to change `example.com` to a user-defined dns name, check [change_domain_example.com](/change_domain_example.com) directory.


6) **Change nginx conf (useful for upload/download of large size layers)**


```
sudo docker exec -it spcgeonode_nginx_1 sh
```


```
vi nginx.conf


    server {
        listen              80;
        server_name         nodo7.conabio.gob.mx 127.0.0.1 nginx;
        proxy_read_timeout 1000s; #<-add this line
...
```

Then:

```
nginx -s reload
```

7) **Restrict all registered users to upload/publish layers immediately:**

Enter to docker container `spcgeonode_django_1`:

```
docker exec -it spcgeonode_django_1 /bin/bash
```

and modify `geonode/settings.py` so any already registered user can't publish layers immediately:

```
ADMIN_MODERATE_UPLOADS = ast.literal_eval(os.environ.get('ADMIN_MODERATE_UPLOADS', 'True'))

RESOURCE_PUBLISHING = ast.literal_eval(os.getenv('RESOURCE_PUBLISHING', 'True'))
```

When persons are registered as users of geonode, they can upload and edit metadata and layers but will not be published immediately. Admin needs to approve and publish via django UI. See [instructions_using_UI_of_geonode](../instructions_using_UI_of_geonode/)



8) **Create superuser** (this is not necessary):

Inside spcgeonode_django_1:

```
docker exec -it spcgeonode_django_1 /bin/bash
```

```
DJANGO_SETTINGS_MODULE=geonode.local_settings python manage.py createsuperuser --username <name of superuser> -v 3 --email <email>
```

You will be prompted for a password, type it twice.

You can check that superuser was created entering to `spcgeonode_postgres_1` docker container and using next query:

```
docker exec -u=postgres -it spcgeonode_postgres_1 bash
psql -d geonode
select * from people_profile;
```

9) **Downloading vectors and rasters could be a bottleneck if they're not small (less than 100 MB), then delete some options for downloading**

In `geonode/geonode/settings.py` change some parameters in the next lists to delete options for downloading rasters and vectors since geonode is deployed:

```
DOWNLOAD_FORMATS_VECTOR = [
    'ZIP', 'JPEG', 'PDF', 'PNG', #'Zipped Shapefile', 'GML 2.0', 'GML 3.1.1', 'CSV', 'Excel', 'GeoJSON', 'KML', 'View in Google Earth', 'Tiles', 'QGIS layer file (.qlr)', 'QGIS project file (.qgs)',
]

DOWNLOAD_FORMATS_RASTER = [
    'ZIP',
    'JPEG',
    'PDF',
    'PNG', #'ArcGrid', 'GeoTIFF', 'Gtopo30', 'ImageMosaic', 'KML', 'View in Google Earth', 'Tiles', 'GML', 'GZIP', 'QGIS layer file (.qlr)', 'QGIS project file (.qgs)', 'Zipped All Files'
]
```

After products are registered they can be downloaded using scripts like [create_downloadable_links_in_geonode](https://github.com/CONABIO/geonode/blob/master/layers_already_imported_in_geonode_conabio_via_geonode_conabio_package/register_MAD-Mex_historical_products/LANDSAT/rasters/create_downloadable_links_in_geonode.sh)


# Notes:

## Notes regarding deployment of geonode

1) **Urls that worth your time checking:**

```
http://<miip>/geoserver/rest

http://<miip>/api

http://<miip>/api/layers/
```

2) **Users and passwords created by default:**

```
#When using browser:

#1)for geonode:
user: super
password: duper

#2)for geoserver:
user: super
password: duper

#For DB: geonode

user: geonode
password: geonode

#For DB: geonode_data

user: geonode_data
password: geonode_data

```


3) **If you want to stop/delete all containers use next commands (being where `docker-compose.yml` is)**

if stop:

```
docker-compose stop

#if after stop you want to delete resources use:
docker rm spcgeonode_django_1 spcgeonode_nginx_1 spcgeonode_postgres_1 spcgeonode_geoserver_1
docker volume rm spcgeonode_certificates spcgeonode_database spcgeonode_geodatadir spcgeonode_media spcgeonode_pgdumps spcgeonode_rabbitmq spcgeonode_static
docker network rm spcgeonode_default
```

if delete all:

```
docker-compose down -v
```

4) **If you want to start again container's stack but you don't want to build again, use:**

```
docker-compose up -d django geoserver postgres nginx
```

5) **If after some time that geonode was deployed you have to clone repo of geonode again, then delete docker images that had been built previously and build from a fresh start.**


## Notes regarding usage of geonode

1) **You can find some example vector layers in:**

```
/usr/local/lib/python3/site-packages/gisdata/data/good/vector/
```

Insert some layer examples:

```
DJANGO_SETTINGS_MODULE=geonode.local_settings python manage.py importlayers -v 3 -i -o -u <name of superuser or other user> example_layers/myformat/myfile

#or if you have dirs:
DJANGO_SETTINGS_MODULE=geonode.local_settings python manage.py importlayers -v 3 -i -o -u <name of superuser or other user> example_layers/myformat/

```

2) **Download/thumbnail of layers:**

### Donwload small size layers or thumbnails

Make sure you are able to download the layer and see it's thumbnail. If either are not working then click button **refresh attributes and statistics** for the layer in geonode. If persists not showing the right thumbnail wait some minutes or increase `proxy_read_timeout` parameter in `nginx.conf`.

### Download large size vectors

Increase number of features `maximum number of features` inside WFS (Web Feature Service) of Geoserver page (to 1,000,000,000 for example). And increase `proxy_read_timeout` in `nginx.conf`


### Download large size rasters

Update Web Coverage Service in geoserver (see [link1](https://geoserver.geo-solutions.it/edu/en/adv_gsconfig/parameters.html) or [link2](https://geoserver.geo-solutions.it/edu/en/adv_gsconfig/parameters.html#wcs-resource-limits) or [link3](https://docs.geoserver.org/stable/en/user/services/wms/configuration.html)) and increase `proxy_read_timeout` in `nginx.conf`



3) **Update links of metadata:**

If pressing button **refresh attributes and statistics** for the layer inside geonode didn't update links inside geoserver regarding metadata use next command:

```
#for specific layer:
DJANGO_SETTINGS_MODULE=geonode.settings python manage.py set_all_layers_metadata -f madmex_landsat_2017-2018_lcc

#for all layers:
DJANGO_SETTINGS_MODULE=geonode.local_settings python manage.py set_all_layers_metadata -d

```

4) **Update styles of layers**

See [styles](../styles) and modify style directly in geoserver. Once modified or registered the style inside geoserver click **refresh attributes and statistics** for the layer in geonode. If persists not showing the right thumbnail for the changed style wait some minutes or increase `proxy_read_timeout` parameter in `nginx.conf`.



5) **For larger vector and raster maps (>1 gb) restrict permissions because downloading process takes too much time that crashes geonode.**

This can be configured either:

5a) **Decreasing parameters described in 2) **Download/thumbnail of layers** of this notes or:**

5b) **(Not yet tested) Use next command:**
    
```
DJANGO_SETTINGS_MODULE=geonode.local_settings python manage.py set_layers_permissions -r chihuahua_merge_wgs84 -p d -u AnonymousUser -g anonymous
Initial permissions info for the resource chihuahua_merge_wgs84:
{'users': {<Profile: super>: ['view_resourcebase', 'download_resourcebase', 'change_resourcebase_metadata', 'change_resourcebase', 'delete_resourcebase', 'change_resourcebase_permissions', 'publish_resourcebase', 'change_layer_data', 'change_layer_style']}, 'groups': {<Group: anonymous>: ['download_resourcebase', 'view_resourcebase']}}
Final permissions info for the resource chihuahua_merge_wgs84:
{'users': {<Profile: super>: ['view_resourcebase', 'download_resourcebase', 'change_resourcebase_metadata', 'change_resourcebase', 'delete_resourcebase', 'change_resourcebase_permissions', 'publish_resourcebase', 'change_layer_data', 'change_layer_style'], <Profile: AnonymousUser>: ['view_resourcebase', 'download_resourcebase']}, 'groups': {<Group: anonymous>: ['view_resourcebase', 'download_resourcebase']}}
Permissions successfully updated!
```

## Notes regarding creation, registration of users and upload of layers of already registered users

1) **Create and register users in geonode via UI:**

* Use https://docs.geonode.org/en/master/usage/accounts_user_profile/index.html

* Use https://docs.geonode.org/en/master/usage/managing_layers/uploading_layers.html 

    * **The layers must be in wgs84 projection! and not be large in size (< 100 mb) for UI usage.**
    

2) **When persons create and register users they can upload and edit metadata and layers unless configured in `geonode/settings.py`:**

If admin wants to give permissions to an user in particular to edit metadata then needs to create group and modify layer permissions using this group. See for example: 

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


(simpler) or inside `spcgeonode_django_1`:

```
docker exec -it spcgeonode_django_1 /bin/bash
```

modify `geonode/settings.py` so any already registered user can't publish layers immediately:

```
ADMIN_MODERATE_UPLOADS = ast.literal_eval(os.environ.get('ADMIN_MODERATE_UPLOADS', 'True'))

RESOURCE_PUBLISHING = ast.literal_eval(os.getenv('RESOURCE_PUBLISHING', 'True'))
```

When persons are registered as users of geonode, they can upload and edit metadata and layers but will not be published immediately. Admin needs to approve and publish via django UI. See [instructions_using_UI_of_geonode](../instructions_using_UI_of_geonode/)



# Next section was used in the development of package of python `geonode_conabio`. Its simpler to use that package to import layers. Go to [geonode_conabio](/python3_package_for_geonode/) directory.

## Insert large layers (more than 1gb): 


1) **Make sure projection is wgs84 and for rasters also are compressed and tiled:**

```
#rasters:
gdalwarp -t_srs EPSG:4326 -co compress=LZW madmex_landsat_2017_31.tif madmex_landsat_2017_31_wgs84.tif

gdal_translate -co TILED=yes -co compress=LZW madmex_landsat_2017_31_wgs84.tif madmex_landsat_2017_31_wgs84_tiled.tif

gdal_translate -co TILED=yes -co compress=LZW madmex_sentinel2_2017_31_wgs84.tif madmex_sentinel2_2017_31_wgs84_tiled.tif

#vectors:
ogr2ogr -progress -t_srs EPSG:4326 HIDALGO_merge_wgs84.shp HIDALGO_merge.shp
```

**References:**

[raster-data-optimization-optimizing-and-serving-big-raster-data](https://docs.geonode.org/en/master/admin/mgmt_commands/#raster-data-optimization-optimizing-and-serving-big-raster-data)

[advanced_gdal/example5](https://geoserver.geo-solutions.it/edu/en/raster_data/advanced_gdal/example5.html)


2) **Change nginx conf**


```
sudo docker exec -it spcgeonode_nginx_1 sh
```


```
vi nginx.conf


    server {
        listen              80;
        server_name         nodo7.conabio.gob.mx 127.0.0.1 nginx;
        proxy_read_timeout 1000s; #<-with this line
...
```

**Then:**

```
nginx -s reload
```

#Don't know if also I need to add lines like:

```
proxy_connect_timeout 1000s;
proxy_send_timeout 1000s;
proxy_read_timeout 1000s;
fastcgi_send_timeout 1000s;
fastcgi_read_timeout 1000s;
uwsgi_read_timeout 1000s;
send_timeout 1000s;
```

Reference: https://support.plesk.com/hc/en-us/articles/115000170354-An-operation-or-a-script-that-takes-more-than-60-seconds-to-complete-fails-on-a-website-hosted-in-Plesk-nginx-504-Gateway-Time-out



## Examples: 

### Vectors: Chihuahua or National landsat changes

**Inside spcgeonode_django_1:**

```
docker exec -it spcgeonode_django_1 /bin/bash
```

- **Add to database:**

```
shp2pgsql CHIHUAHUA_merge_wgs84.shp madmex_sentinel2_chihuahua_2017_2018_lcc public.CHIHUAHUA_merge_wgs84.shp | psql -h <host> -d geonode_data -U geonode

shp2pgsql madmex_landsat_changes_2017-2018_wgs84.shp madmex_landsat_2017-2018_lcc public.madmex_landsat_changes_2017-2018_wgs84.shp | psql -h <host> -d geonode_data -U geonode
```

- **Add to geoserver from geonode_data database:** 

Need to follow:

https://training.geonode.geo-solutions.it/004_admin_workshop/007_loading_data_into_geonode/geoserver.html

- **Use `updatelayers` like:**

**Check cpus usage when executing next command (after execution of next cmd is done I needed to do a `docker-compose stop` because some cpus and processes stucked in some tasks)**

```
DJANGO_SETTINGS_MODULE=geonode.local_settings python manage.py updatelayers -s geonode_data -w geonode -f madmex_sentinel2_chihuahua_2017_2018_lcc
```


- **Check:**

```
psql -h localhost -U geonode -d geonode

select * from layers_layer;
```

### Rasters: National, Chihuahua


**Inside spcgeonode_django_1:**

```
docker exec -it spcgeonode_django_1 /bin/bash
```


```
DJANGO_SETTINGS_MODULE=geonode.local_settings python manage.py importlayers -v 3 -i -o -n madmex_landsat_2017_31_tiled -t madmex_landsat_2017_31_tiled -a "LANDSAT MAD-Mex lc" -k "MAD-Mex, LANDSAT, GeoTIFF, WCS" -r "Mexico, North America, Latin America" madmex_landsat_2017_31_wgs84_tiled.tif

DJANGO_SETTINGS_MODULE=geonode.local_settings python manage.py importlayers -v 3 -i -o -n Chihuahua_landsat_2017_31_tiled -t Chihuahua_landsat_2017_31_tiled -a "LANDSAT MAD-Mex lc" -k "MAD-Mex, LANDSAT, GeoTIFF, WCS" -r "Chihuahua, Mexico, North America, Latin America" Chihuahua_landsat_2017_31_wgs84_tiled.tif


DJANGO_SETTINGS_MODULE=geonode.local_settings python manage.py importlayers -v 3 -i -o -n madmex_sentinel2_2017_31_tiled -t madmex_sentinel2_2017_31_tiled -a "Sentinel2 MAD-Mex lc" -k "MAD-Mex, Sentinel2, GeoTIFF, WCS" -r "Mexico, North America, Latin America" madmex_sentinel2_2017_31_wgs84_tiled.tif

```

### For either Raster or Vector

- **Make sure you are able to download it and see thumbnail. If not click to button refresh attributes and statistics for the layer in geonode. For thumbnail increase nginx conf `proxy_read_timeout` parameter.**


Next wasnt working (was an idea for not having to click on button of refresh attributes and statistics)

I was using `DJANGO_SETTINGS_MODULE=geonode.settings python manage.py sync_geonode_layers` with `--updatethumbnails` and `--updateattributes` but it wasn't working ... instead use button to refresh attributes and statistics


- **Update links of metadata:**

If pressing button refresh attributes and statistics for the layer in geonode didn't update links inside geoserver regarding metadata use next command:

```
#for specific layer:
DJANGO_SETTINGS_MODULE=geonode.settings python manage.py set_all_layers_metadata -f madmex_landsat_2017-2018_lcc

#for all layers:
DJANGO_SETTINGS_MODULE=geonode.local_settings python manage.py set_all_layers_metadata -d

```




### Style for Rasters

See [styles](../styles) and modify style used directly in geoserver.



# Download large layers:

## Vectors

Increase number of features `maximum number of features` inside WFS (Web Feature Service) of Geoserver page (to 1,000,000,000 for example). And increase `proxy_read_timeout` for `nginx.conf`


## Rasters

Update Web Coverage Service in geoserver (see [link1](https://geoserver.geo-solutions.it/edu/en/adv_gsconfig/parameters.html) or [link2](https://geoserver.geo-solutions.it/edu/en/adv_gsconfig/parameters.html#wcs-resource-limits) or [link3](https://docs.geoserver.org/stable/en/user/services/wms/configuration.html)) and increase `proxy_read_timeout` for `nginx.conf`


# Insert medium or small size layers (less than 1 gb):


- **Change nginx conf:**


```
sudo docker exec -it spcgeonode_nginx_1 sh
```



```
vi nginx.conf


    server {
        listen              80;
        server_name         nodo7.conabio.gob.mx 127.0.0.1 nginx;
        proxy_read_timeout 1000s; #<-with this line
...
```

```
nginx -s reload
```

#Don't know if also I need to add lines like:

```
proxy_connect_timeout 1000s;
proxy_send_timeout 1000s;
proxy_read_timeout 1000s;
fastcgi_send_timeout 1000s;
fastcgi_read_timeout 1000s;
uwsgi_read_timeout 1000s;
send_timeout 1000s;
```

Reference: https://support.plesk.com/hc/en-us/articles/115000170354-An-operation-or-a-script-that-takes-more-than-60-seconds-to-complete-fails-on-a-website-hosted-in-Plesk-nginx-504-Gateway-Time-out


## Examples: 

### Vectors: Hidalgo/Aguascalientes


- **Importlayers**

**Inside `spcgeonode_django_1` container:**

```
sudo docker exec -it spcgeonode_django_1 /bin/bash
```


**For accents use: -C "Latin 1" in importlayers cmd (THIS "Latin 1" IS NOT WORKING)**

```
DJANGO_SETTINGS_MODULE=geonode.local_settings python manage.py importlayers -v 3 -i -o -n madmex_sentinel2_aguascalientes_2017_2018_lcc -t madmex_sentinel2_aguascalientes_2017_2018_lcc -a "Sentinel2 MAD-Mex lcc" -k "MAD-Mex, sentinel2, features, Aguascalientes" -r "Mexico, North America, Latin America" AGUASCALIENTES_merge_wgs84.shp


DJANGO_SETTINGS_MODULE=geonode.local_settings python manage.py importlayers -v 3 -i -o -n madmex_sentinel2_hidalgo_2017_2018_lcc -t madmex_sentinel2_hidalgo_2017_2018_lcc -a "Sentinel2 MAD-Mex lcc" -k "MAD-Mex, sentinel2, features, Hidalgo" -r "Mexico, North America, Latin America" HIDALGO_merge_wgs84.shp

```

### Rasters: Hidalgo

**Inside `spcgeonode_django_1` container:**

```
sudo docker exec -it spcgeonode_django_1 /bin/bash
```

```
DJANGO_SETTINGS_MODULE=geonode.local_settings python manage.py importlayers -v 3 -i -o -n sentinel2_Hidalgo_2017_31_tiled -t sentinel2_Hidalgo_2017_31_tiled -a "Sentinel2 MAD-Mex lc" -k "MAD-Mex, Sentinel2, GeoTIFF, WCS" -r "Hidalgo, Mexico, North America, Latin America" sentinel2_Hidalgo_2017_31_wgs84_tiled.tif

```

### For either Raster or Vector

- **Make sure you are able to download it and see thumbnail. If not click to button refresh attributes and statistics for the layer in geonode. For thumbnail increase nginx conf `proxy_read_timeout` parameter.**


Next wasnt working (was an idea for not having to click on button of refresh attributes and statistics)

I was using `DJANGO_SETTINGS_MODULE=geonode.settings python manage.py sync_geonode_layers` with `--updatethumbnails` and `--updateattributes` but it wasn't working ... instead use button to refresh attributes and statistics


- **Update links of metadata:**

If pressing button refresh attributes and statistics for the layer in geonode didn't update links inside geoserver regarding metadata use next command:

```
#for specific layer:
DJANGO_SETTINGS_MODULE=geonode.settings python manage.py set_all_layers_metadata -f madmex_landsat_2017-2018_lcc

#for all layers:
DJANGO_SETTINGS_MODULE=geonode.local_settings python manage.py set_all_layers_metadata -d

```



### Style for Rasters

See [styles](../styles) and modify style used directly in geoserver.



# Download via python request

```
import requests

string = 'http://nodo7.conabio.gob.mx/gs/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3AAGUASCALIENTES_merge_wgs84_clean3&outputFormat=json&srs=EPSG%3A4326&srsName=EPSG%3A4326'

r = requests.get(string)

r.json()

```

# Download via curl:

```
curl -X "string = 'http://nodo7.conabio.gob.mx/gs/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3AAGUASCALIENTES_merge_wgs84_clean3&outputFormat=json&srs=EPSG%3A4326&srsName=EPSG%3A4326'"
```

# MIGRATEURL:

**Inside `spcgeonode_django_1` container:**

```
sudo docker exec -it spcgeonode_django_1 bash
```

```
DJANGO_SETTINGS_MODULE=geonode.local_settings python manage.py migrate_baseurl --source-address geonodeservices.conabio.gob.mx --target-address geonode.conabio.gob.mx
```

Also in geoserver inside "Almacenes de datos" go to geonode_data and change db to new url


# DELETE:


**Delete in geonode and geoserver. Example: Aguascalientes:**



**Inside `spcgeonode_django_1` container:**


```
sudo docker exec -it spcgeonode_django_1 bash
```


Create `delete_aguascalientes.json`

```
{
  "filters": {
  "layer": [
            "Q(title__icontains='madmex_sentinel2_aguascalientes_2017_2018_lcc')"
       ]
        }
}
```

```
DJANGO_SETTINGS_MODULE=geonode.local_settings python manage.py delete_resources -c delete_aguascalientes.json
```

**For the shapefiles also delete the resource inside geonode_data db the table associated:**


```
drop table "madmex_sentinel2_aguascalientes_2017_2018_lcc";
```

# Change permissions 

```
DJANGO_SETTINGS_MODULE=geonode.local_settings python manage.py set_layers_permissions -r chihuahua_merge_wgs84 -p d -u AnonymousUser -g anonymous
Initial permissions info for the resource chihuahua_merge_wgs84:
{'users': {<Profile: super>: ['view_resourcebase', 'download_resourcebase', 'change_resourcebase_metadata', 'change_resourcebase', 'delete_resourcebase', 'change_resourcebase_permissions', 'publish_resourcebase', 'change_layer_data', 'change_layer_style']}, 'groups': {<Group: anonymous>: ['download_resourcebase', 'view_resourcebase']}}
Final permissions info for the resource chihuahua_merge_wgs84:
{'users': {<Profile: super>: ['view_resourcebase', 'download_resourcebase', 'change_resourcebase_metadata', 'change_resourcebase', 'delete_resourcebase', 'change_resourcebase_permissions', 'publish_resourcebase', 'change_layer_data', 'change_layer_style'], <Profile: AnonymousUser>: ['view_resourcebase', 'download_resourcebase']}, 'groups': {<Group: anonymous>: ['view_resourcebase', 'download_resourcebase']}}
Permissions successfully updated!
```
# Notes

## 1

**Nodes at conabio have an intermediate security layer that makes no possibly to read `css` files for `nginx` container when an user access it. This causes that web page can't see correctly. A patch is to make a deployment for `spc geonode` stack of containers (in other server that can visualize correctly geonode web page) and make a copy of the `static` files created under `_volume_static` dir to `/var/www/html/web/geonode/geonode_static`. Then modify inside `nginx` container `sudo docker exec -it spcgeonode_nginx_1 sh` that runs inside the node at conabio and change file `spcgeonode.conf` in location `static` with:**



```
location /static {
    proxy_pass https://monitoreo.conabio.gob.mx/geonode/geonode_static/; #<- with this line or the site where the static dir is 
    #alias /spcgeonode-static; # your Django project's static files - amend as required
    include  /etc/nginx/mime.types;
    expires 365d;
}
```


Then:

```
nginx -s reload
```

Also to see thumbnails repeat same procedure described before but with dir `_volume_media/thumbs` that is, copy `thumbs` dir to `/var/www/html/web/geonode/geonode_media/` and change file `spcgeonode.conf` in location `media` with:

```
# Django media
location /uploaded  {
    #alias /spcgeonode-media;  # your Django project's media files - amend as required
    proxy_pass https://monitoreo.conabio.gob.mx/geonode/geonode_media/;
    include  /etc/nginx/mime.types;
    expires 365d;
}
```

Then:

```
nginx -s reload
```

## 2

To mount `/LUSTRE/MADMEX` in a machine different of a node of the cluster:

**First option: via sshfs**

0. Install `sshfs`

```
sudo apt-get install sshfs
```

1. Interchange keys

2. Use:

```
sudo sshfs -o allow_other,default_permissions,IdentityFile=/home/epalacios/.ssh/id_rsa madmex_admin@nodo7.conabio.gob.mx:/LUSTRE/MADMEX /LUSTRE/MADMEX

#not sure if next was executed...

sshfs madmex_admin@nodo7.conabio.gob.mx:/LUSTRE/MADMEX /LUSTRE/MADMEX -o rw,nosuid,nodev,identityfile=/home/epalacios/.ssh/id_rsa,uid=1027,gid=1099,default_permissions,allow_other
```

Or in `/etc/fstab` add next line:

```
madmex_admin@nodo7.conabio.gob.mx:/LUSTRE/MADMEX /LUSTRE/MADMEX  fuse.sshfs rw,nosuid,nodev,identityfile=/home/epalacios/.ssh/id_rsa,uid=1027,gid=1099,default_permissions,allow_other 0 0
```


**Second option: via samba**

```
sudo apt-get install cifs-utils
```

Change `/etc/fstab` with a line:

```
\\master.conabio.gob.mx\MADMEX   /LUSTRE/MADMEX    cifs   username=madmex_admin,password=madmex_admin...,uid=epalacios,gid=epalacios,file_mode=0664,dir_mode=0775,rw,noperm,iocharset=utf8  0	0
```

Then:

```
mount -a
```


# Useful notes

#Possibly fix for `uwsgi` (08-05-2020)

modify 

```
geonode/scripts/spcgeonode/docker-compose.override.yml
```

with different parameters in uwsgi cmd using https://github.com/GeoNode/geonode/blob/master/uwsgi.ini#L25-L31

then 

```
docker-compose stop

docker-compose up -d django geoserver postgres nginx

```


check

```
apt-get update && apt-get install -y procps

ps aux|grep uwsgi
```




#see:

http://146.155.17.19:21080/mediawiki-1.22.7/index.php/Geonode_data_upload

https://training.geonode.geo-solutions.it/004_admin_workshop/007_loading_data_into_geonode/geoserver.html

https://training.geonode.geo-solutions.it/006_adv_workshop/002_geonode_settings/settings.html#settings

https://stackoverflow.com/questions/54737851/how-to-increase-timeout-for-nginx

http://osgeo-org.1560.x6.nabble.com/Poor-performance-GeoNode-td5332874.html

https://geoserver.geo-solutions.it/edu/en/adv_gsconfig/gsproduction.html

https://geoserver.geo-solutions.it/edu/en/install_run/jai_io_install.html#geoserver-jai-io-install

https://docs.geonode.org/en/2.8/tutorials/advanced/geonode_production/production.html#native-jai-and-jai-imageio

https://github.com/terrestris/docker-geoserver

https://github.com/geosolutions-it/imageio-ext/wiki


#geonode:

https://github.com/GeoNode/geonode/issues/5285


https://github.com/GeoNode/nginx-docker/blob/master/nginx.conf#L27


https://github.com/GeoNode/geonode-docker/blob/master/uwsgi.ini#L7

https://github.com/GeoNode/nginx-docker/blob/master/nginx.conf#L75




# conabio-geonode
GeoNode with docker-compose

Steps to deploy geonode with `docker-compose`. 

1.- Clone repository 

```
git clone --single-branch -b master https://github.com/GeoNode/geonode.git
```

2.- Override `.yml` with your IP:

```
cd geonode
myip=<here put your IP or DNS such as coreos.conabio.gob.mx>
cp docker-compose.override.localhost.yml docker-compose.override.myip.yml
#ubuntu users:
sed -i "s/localhost/$myip/g" docker-compose.override.myip.yml
#mac users:
sed "s/localhost/$myip/g" docker-compose.override.localhost.yml > docker-compose.override.myip.yml
```

3.- Add `port` to `db` in `docker-compose.yml`

```
#for mac users, use your editor to add inside db:
    ports:
      - "5432:5432"
      
#or if using ubuntu:
sed -i '/db.env/a \ \ \ \ ports:\n      - "5432:5432"' docker-compose.yml
```

4.- Docker compose up

```
docker-compose -f docker-compose.yml -f docker-compose.override.myip.yml up --build -d

#note: if in mac you have error related to "docker-credential-osxkeychain" then before docker-compose ... up ... execute:
#$security unlock-keychain
```

After build, check from time to time with:

```
docker logs django4geonode |tail -n 10
```

until you get:

```
900 static files copied to '/mnt/volumes/statics/static'.
static data refreshed
Executing UWSGI server uwsgi --ini /usr/src/app/uwsgi.ini for Production
command to be executed is uwsgi --ini /usr/src/app/uwsgi.ini
```

You will have `volumes`, `network` and `docker-containers` created after executing `up`:

```
#images: geonode/geonode:latest, geonode/geoserver_data:2.16.2, geonode/geoserver:2.16.2, geonode/geonode:<none>, geonode/postgis:11, geonode/nginx:production
#containers: nginx4geonode, django4geonode, geoserver4geonode, db4geonode
#volumes: geonode-dbbackups, geonode-dbdata, geonode-gsdatadir, geonode-rabbitmq, geonode-statics
#network: geonode_default

```

Check deployment of geonode and geoserver going to browser:

```
<miip>
<miip>geoserver/web/
```

5.- Create superuser:

Enter to docker container `django4geonode`:

```
docker exec -it django4geonode /bin/bash
```

Once inside of docker container copy local settings to configure and use them later:

```
cp /usr/src/app/package/support/geonode.local_settings geonode/local_settings.py
#or cp /spcgeonode/package/support/geonode.local_settings geonode/local_settings.py
```

Install some useful cmd lines

```
apt-get update && apt-get install -y vim less nano unzip
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

#Modify for geonode/local_settings.py:
#INSTALLED_APPS += ('geonode_mapstore_client', )

```


Create superuser:

```
DJANGO_SETTINGS_MODULE=geonode.local_settings python manage.py createsuperuser --username <name of superuser> -v 3 --email <email>
```

You will be prompted for a password, type it twice.

You can check that superuser was created entering to `db4geonode` docker container and using next query:

```
docker exec -u=postgres -it db4geonode bash
psql -d geonode
select * from people_profile;
```

6.- Insert some layers: (now just shapefiles and rasters have been imported in projection "EPSG:4326")

```
DJANGO_SETTINGS_MODULE=geonode.local_settings python manage.py importlayers -v 3 -i -o -u <name of superuser or other user> example_layers/myformat/myfile

#or if you have dirs:
DJANGO_SETTINGS_MODULE=geonode.local_settings python manage.py importlayers -v 3 -i -o -u <name of superuser or other user> example_layers/myformat/

```

**Note:**

1) You can find some example vector layers in:

```
/usr/local/lib/python2.7/site-packages/gisdata/data/good/vector/
```

2) Urls that worth your time checking:

```
http://<miip>/geoserver/rest

http://<miip>/api

http://<miip>/api/layers/
```

3) User and passwords created by default:

```
#When using browser:

#1)for geonode:
user: admin
password: admin

#2)for geoserver:
user: admin
password: geoserver

#For DB: geonode

user: geonode
password: geonode

#For DB: geonode_data

user: geonode_data
password: geonode_data

```

4) env file worth seeing for db passwords when using docker:

```
geonode/scripts/docker/env/production/db.env #geonode is the repo cloned
```

## Note:

1) If you want to stop/delete all containers use next commands (being where `docker-compose.yml` is)

if stop:

```
docker-compose stop

#if after stop you want to delete resources use:
docker rm nginx4geonode geoserver4geonode django4geonode gsconf4geonode db4geonode
docker volume rm geonode-dbbackups geonode-dbdata geonode-gsdatadir geonode-rabbitmq geonode-statics
docker network rm geonode_default
```

if delete all:

```
docker-compose down
docker volume rm geonode-dbbackups geonode-dbdata geonode-gsdatadir geonode-rabbitmq geonode-statics
```

2) If you want to start again container's stack but you don't want to build again, use:

```
docker-compose -f docker-compose.yml -f docker-compose.override.myip.yml up -d
```

3) If after some time that geonode was deployed you have to clone repo of geonode again, then delete docker images that had been built previously and build from a fresh start.
#12 may

Adding CHIHUAHUA shapefile sentinel2 2017-2018 changes

- First add it to database with:

```
sudo apt install postgis
shp2pgsql CHIHUAHUA_merge_wgs84.shp chihuahua_merge_wgs84 public.chihuahua_merge_wgs84.shp | psql -h <host> -d geonode_data -U geonode
```

- Second add it to geoserver from geonode_data database:

Need to follow:

https://training.geonode.geo-solutions.it/004_admin_workshop/007_loading_data_into_geonode/geoserver.html

- At the end of the last page use `updatelayers` like:


```
DJANGO_SETTINGS_MODULE=geonode.local_settings python manage.py updatelayers -s geonode_data -w geonode -f madmex_sentinel2_chihuahua_2017_2018_lcc
```

(Need to figure out how to fill cells of link to metadata in [link](https://github.com/CONABIO/geonode/blob/milestone-1/screenshots_deployment_using_spcgeonode/large_shapefile/large_shapefile_4.png))

- Check:

```
psql -h localhost -U geonode -d geonode

select * from layers_layer;
```


Change permissions (don't know if this is needed... need to check):

```
DJANGO_SETTINGS_MODULE=geonode.local_settings python manage.py set_layers_permissions -r chihuahua_merge_wgs84 -p d -u AnonymousUser -g anonymous
Initial permissions info for the resource chihuahua_merge_wgs84:
{'users': {<Profile: super>: ['view_resourcebase', 'download_resourcebase', 'change_resourcebase_metadata', 'change_resourcebase', 'delete_resourcebase', 'change_resourcebase_permissions', 'publish_resourcebase', 'change_layer_data', 'change_layer_style']}, 'groups': {<Group: anonymous>: ['download_resourcebase', 'view_resourcebase']}}
Final permissions info for the resource chihuahua_merge_wgs84:
{'users': {<Profile: super>: ['view_resourcebase', 'download_resourcebase', 'change_resourcebase_metadata', 'change_resourcebase', 'delete_resourcebase', 'change_resourcebase_permissions', 'publish_resourcebase', 'change_layer_data', 'change_layer_style'], <Profile: AnonymousUser>: ['view_resourcebase', 'download_resourcebase']}, 'groups': {<Group: anonymous>: ['view_resourcebase', 'download_resourcebase']}}
Permissions successfully updated!
```

To download Chihuahua I need to increase number of features `maximum number of features` inside WFS (Web Feature Service) of Geoserver page

http://sipecamdata.conabio.gob.mx/geoserver/web/wicket/bookmarkable/org.geoserver.wfs.web.WFSAdminPage?9


And also:

Fill `key words` cell mannualy in geonode with `features` string (inside metadata). For this use editing tools button in geonode and select metadata. Then the button will be available (also possibly execute the `set_layer_permissions` cmd)

For HIDALGO

DJANGO_SETTINGS_MODULE=geonode.local_settings python manage.py importlayers -v 3 -i -o -n HIDALGO_merge_wgs84 HIDALGO_merge_wgs84.shp

#Modify:  using https://support.plesk.com/hc/en-us/articles/115000170354-An-operation-or-a-script-that-takes-more-than-60-seconds-to-comple$


sudo docker exec -it spcgeonode_nginx_1 sh

```
vi nginx.conf


    server {
        listen              80;
        server_name         nodo7.conabio.gob.mx 127.0.0.1 nginx;
        proxy_read_timeout 180s; #<-with this line
...
```

Then:

```
nginx -s reload
```

#Don't know if also I need to add lines like:

```
proxy_connect_timeout 10000s;
proxy_send_timeout 10000s;
proxy_read_timeout 10000s;
fastcgi_send_timeout 10000s;
fastcgi_read_timeout 10000s;
uwsgi_read_timeout 1000s;
send_timeout 1000s;
```




#Also when trying to download Aguascalientes zip shapefile this came out:

```
UnicodeDecodeError at /gs/ows

'utf-8' codec can't decode byte 0xf7 in position 10: invalid start byte

Request Method: 	GET
Request URL: 	http://sipecamdata.conabio.gob.mx/gs/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3AAGUASCALIENTES_merge_wgs84&outputFormat=SHAPE-ZIP&srs=EPSG%3A4326&format_options=charset%3AUTF-8
Django Version: 	2.2.12
Exception Type: 	UnicodeDecodeError
Exception Value: 	

'utf-8' codec can't decode byte 0xf7 in position 10: invalid start byte

Exception Location: 	./geonode/geoserver/views.py in _response_callback, line 544
Python Executable: 	/usr/local/bin/uwsgi
Python Version: 	3.7.7
Python Path: 	

['/spcgeonode',
 '.',
 '',
 '/usr/local/lib/python37.zip',
 '/usr/local/lib/python3.7',
 '/usr/local/lib/python3.7/lib-dynload',
 '/usr/local/lib/python3.7/site-packages',
 '/spcgeonode']
```

Check character and remove it from shapefile. Maybe are the accents


#13 may:

Aguascalientes was downloaded correctly. But for HIdalgo this came out:

```
django_1          | requests.exceptions.ConnectionError: HTTPConnectionPool(host='nginx', port=80): Max retries exceeded with url: /geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode:HIDALGO_merge_wgs84&outputFormat=SHAPE-ZIP&srs=EPSG:4326&format_options=charset:UTF-8 (Caused by ReadTimeoutError("HTTPConnectionPool(host='nginx', port=80): Read timed out. (read timeout=10)"))

```

maybe rise in some place the times?
# conabio-geonode spc

See [spcgeonode](https://github.com/GeoNode/geonode/blob/master/scripts/spcgeonode/)


GeoNode with docker-compose

Steps to deploy geonode with `docker-compose`. 

1.- Clone repository 

```
git clone --single-branch -b master https://github.com/GeoNode/geonode.git
```

2.- Override `.yml` with your IP:

```
cd geonode/scripts/spcgeonode
#modify .env in entry HTTP_HOST=<nodo7.conabio.gob.mx>
```

3.- Docker compose up

**Note: make sure to mount volumes in `docker-compose.yml` for django container, see section Insert large layers**

```
#just the essential:
docker-compose up --build -d django geoserver postgres nginx
#or: docker-compose up -d django geoserver postgres nginx
```

Check with:

```
docker-compose logs -f
```

Check deployment of geonode and geoserver going to browser:

```
<miip>
<miip>geoserver/web/
```

5.- Create superuser:

Enter to docker container `spcgeonode_django_1`:

```
docker exec -it spcgeonode_django_1 /bin/bash
```

Once inside of docker container copy local settings to configure and use them later:

```
cp /spcgeonode/package/support/geonode.local_settings geonode/local_settings.py
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
docker exec -u=postgres -it spcgeonode_postgres_1 bash
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
/usr/local/lib/python3/site-packages/gisdata/data/good/vector/
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


## Note:

1) If you want to stop/delete all containers use next commands (being where `docker-compose.yml` is)

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

2) If you want to start again container's stack but you don't want to build again, use:

```
docker-compose up -d django geoserver postgres nginx
```

3) If after some time that geonode was deployed you have to clone repo of geonode again, then delete docker images that had been built previously and build from a fresh start.


# Insert large layers (more than 1gb): 


Mount /LUSTRE/MADMEX:

Using `docker.compose.yml` inside spc dir modify it where `image: geonode/spcgeonode:django-3.0` is, then:

```
...volumes:
    - static:/spcgeonode-static/
    - media:/spcgeonode-media/
    - /LUSTRE/MADMEX:/LUSTRE/MADMEX
```


Inside spcgeonode_django_1 use

## Chihuahua

- First add it to database with:

```
apt install postgis
shp2pgsql /LUSTRE/MADMEX/.../CHIHUAHUA_merge_wgs84.shp CHIHUAHUA_merge_wgs84 public.CHIHUAHUA_merge_wgs84.shp | psql -h <host> -d geonode_data -U geonode
```

- Second add it to geoserver from geonode_data database. Need to follow:

https://training.geonode.geo-solutions.it/004_admin_workshop/007_loading_data_into_geonode/geoserver.html

- At the end of the last page use `updatelayers` like:


```
DJANGO_SETTINGS_MODULE=geonode.local_settings python manage.py updatelayers -s geonode_data -w geonode
```

**Appareantly use of next recomendation of set all layers metadata repeated two times the format type of download... need to check**

-> Need to figure out how to fill cells of link to metadata in [link](https://github.com/CONABIO/geonode/blob/milestone-1/screenshots_deployment_using_spcgeonode/large_shapefile/large_shapefile_4.png) maybe check: [management-command-set-all-layers-metadata](https://docs.geonode.org/en/master/admin/mgmt_commands/index.html#management-command-set-all-layers-metadata)


**IMPORTANT:**


**Appareantly use of next recomendation of set all layers metadata repeated two times the format type of download... need to check**

Fill `key words` or `abstract`  cell mannualy in geonode web page with `features` string or `No description provided` for `key words` or `abstract` respectively (inside metadata). For this use editing tools button in geonode and select metadata. Then the button will be available (check if I need to execute the `set_layer_permissions` cmd, also check [management-command-set-all-layers-metadata](https://docs.geonode.org/en/master/admin/mgmt_commands/index.html#management-command-set-all-layers-metadata) )

- Check:

```
psql -h localhost -U geonode -d geonode

select * from layers_layer;
```

-> **this is not necessary**: Change permissions (don't know if this is needed... need to check):

```
DJANGO_SETTINGS_MODULE=geonode.local_settings python manage.py set_layers_permissions -r chihuahua_merge_wgs84 -p d -u AnonymousUser -g anonymous
Initial permissions info for the resource chihuahua_merge_wgs84:
{'users': {<Profile: super>: ['view_resourcebase', 'download_resourcebase', 'change_resourcebase_metadata', 'change_resourcebase', 'delete_resourcebase', 'change_resourcebase_permissions', 'publish_resourcebase', 'change_layer_data', 'change_layer_style']}, 'groups': {<Group: anonymous>: ['download_resourcebase', 'view_resourcebase']}}
Final permissions info for the resource chihuahua_merge_wgs84:
{'users': {<Profile: super>: ['view_resourcebase', 'download_resourcebase', 'change_resourcebase_metadata', 'change_resourcebase', 'delete_resourcebase', 'change_resourcebase_permissions', 'publish_resourcebase', 'change_layer_data', 'change_layer_style'], <Profile: AnonymousUser>: ['view_resourcebase', 'download_resourcebase']}, 'groups': {<Group: anonymous>: ['view_resourcebase', 'download_resourcebase']}}
Permissions successfully updated!
```

# Download large layers:

Increase number of features `maximum number of features` inside WFS (Web Feature Service) of Geoserver page:

http://sipecamdata.conabio.gob.mx/geoserver/web/wicket/bookmarkable/org.geoserver.wfs.web.WFSAdminPage?9

to 200,000,000 for example.


# Insert medium or small size layers (less than 1 gb):

## Hidalgo

sudo docker exec -it spcgeonode_nginx_1 sh

```
vi nginx.conf


    server {
        listen              80;
        server_name         nodo7.conabio.gob.mx 127.0.0.1 nginx;
        proxy_read_timeout 1000s; #<-with this line
...
```

Then:

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

`Importlayers`:


```
DJANGO_SETTINGS_MODULE=geonode.local_settings python manage.py importlayers -v 3 -i -o -n AGUASCALIENTES_merge_wgs84 /LUSTRE/MADMEX/products/landcoverchange/sentinel2/2017_2018/indi50k/estados/AGUASCALIENTES/AGUASCALIENTES_merge_wgs84.shp

DJANGO_SETTINGS_MODULE=geonode.local_settings python manage.py importlayers -v 3 -i -o -n HIDALGO_merge_wgs84 /LUSTRE/MADMEX/products/landcoverchange/sentinel2/2017_2018/indi50k/estados/HIDALGO/HIDALGO_merge_wgs84.shp
```


**Nodes at conabio have an intermediate security layer that makes no possibly to read `css` files for `nginx` container when an user access it. This causes that web page can't see correctly. A patch is to make a deployment for `spc geonode` stack of containers (in other server that can visualize correctly geonode web page) and make a copy of the `static` files created in `_volume_static` dir to a site. Then modify inside `nginx` container `sudo docker exec -it spcgeonode_nginx_1 sh` that runs inside the node at conabio and change file `spcgeonode.conf` in location `static` with:**

```
location /static {
    proxy_pass https://monitoreo.conabio.gob.mx/geonode/; #<- with this line or the site where the static dir is 
    #alias /spcgeonode-static; # your Django project's static files - amend as required
    include  /etc/nginx/mime.types;
    expires 365d;
}
```


Then:

```
nginx -s reload
```

## Download either small, medium or large layers

**IMPORTANT:**

Fill `key words` or `abstract`  cell mannualy in geonode web page with `features` string or `No description provided` for `key words` or `abstract` respectively (inside metadata). For this use editing tools button in geonode and select metadata. Then the button will be available (check if I need to execute the `set_layer_permissions` cmd, also check [management-command-set-all-layers-metadata](https://docs.geonode.org/en/master/admin/mgmt_commands/index.html#management-command-set-all-layers-metadata) 



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


#geonode:

https://github.com/GeoNode/geonode/issues/5285


https://github.com/GeoNode/nginx-docker/blob/master/nginx.conf#L27


https://github.com/GeoNode/geonode-docker/blob/master/uwsgi.ini#L7

https://github.com/GeoNode/nginx-docker/blob/master/nginx.conf#L75




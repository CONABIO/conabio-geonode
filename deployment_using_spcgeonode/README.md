# conabio-geonode
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

```
#just the essential:
docker-compose up --build -d django geoserver postgres nginx
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

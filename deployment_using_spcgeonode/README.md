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

nginx_1           | 172.26.0.5 - super [07/May/2020:21:11:57 +0000] "PUT /geoserver/rest/workspaces/geonode/datastores/geonode_data/file.shp?update=overwrite&charset=UTF-8&filename=CHIHUAHUA_merge_wgs84.zip&target=shp HTTP/1.1" 500 65 "-" "python-requests/2.23.0"


Error:

DJANGO_SETTINGS_MODULE=geonode.local_settings python manage.py importlayers -v 3 -i -o -n CHIHUAHUA_merge_wgs84 CHIHUAHUA_merge_wgs84.shp --traceback
Verifying that GeoNode is running ...

Found 1 potential layers.

Loading user configuration
running configuration {'metadata:main': {'identification_title': 'GeoNode Catalogue', 'identification_abstract': 'GeoNode is an open source platform that facilitates the creation, sharing, and collaborative use of geospatial data', 'identification_keywords': 'sdi, catalogue, discovery, metadata, GeoNode', 'identification_keywords_type': 'theme', 'identification_fees': 'None', 'identification_accessconstraints': 'None', 'provider_name': 'Organization Name', 'provider_url': 'http://nodo7.conabio.gob.mx/', 'contact_name': 'Lastname, Firstname', 'contact_position': 'Position Title', 'contact_address': 'Mailing Address', 'contact_city': 'City', 'contact_stateorprovince': 'Administrative Area', 'contact_postalcode': 'Zip or Postal Code', 'contact_country': 'Country', 'contact_phone': '+xx-xxx-xxx-xxxx', 'contact_fax': '+xx-xxx-xxx-xxxx', 'contact_email': 'Email Address', 'contact_url': 'Contact URL', 'contact_hours': 'Hours of Service', 'contact_instructions': 'During hours of service. Off on weekends.', 'contact_role': 'pointOfContact'}, 'metadata:inspire': {'enabled': 'true', 'languages_supported': 'eng,gre', 'default_language': 'eng', 'date': 'YYYY-MM-DD', 'gemet_keywords': 'Utility and governmental services', 'conformity_service': 'notEvaluated', 'contact_name': 'Organization Name', 'contact_email': 'Email Address', 'temp_extent': 'YYYY-MM-DD/YYYY-MM-DD'}, 'server': {'home': '.', 'url': 'http://nodo7.conabio.gob.mx/catalogue/csw', 'encoding': 'UTF-8', 'language': 'en', 'maxrecords': '10', 'pretty_print': 'true', 'domainquerytype': 'range', 'domaincounts': 'true', 'profiles': 'apiso,ebrim'}, 'repository': {'source': 'geonode.catalogue.backends.pycsw_plugin.GeoNodeRepository', 'filter': 'is_published = true', 'mappings': '/spcgeonode/geonode/catalogue/backends/pycsw_local_mappings.py'}}
Setting language
Loading custom repository mappings from /spcgeonode/geonode/catalogue/backends/pycsw_local_mappings.py
Loading outputschemas
Setting MaxRecordDefault
Querying repository with ids: 11953b28-90a6-11ea-bf7b-0242ac1a0005
Request processed
Writing response.
/usr/local/lib/python3.7/site-packages/owslib/iso.py:121: FutureWarning: the .identification and .serviceidentification properties will merge into .identification being a list of properties.  This is currently implemented in .identificationinfo.  Please see https://github.com/geopython/OWSLib/issues/38 for more information
  FutureWarning)
/usr/local/lib/python3.7/site-packages/owslib/iso.py:548: FutureWarning: The .keywords and .keywords2 properties will merge into the .keywords property in the future, with .keywords becoming a list of MD_Keywords instances. This is currently implemented in .keywords2. Please see https://github.com/geopython/OWSLib/issues/301 for more information
  FutureWarning)
Loading user configuration
running configuration {'metadata:main': {'identification_title': 'GeoNode Catalogue', 'identification_abstract': 'GeoNode is an open source platform that facilitates the creation, sharing, and collaborative use of geospatial data', 'identification_keywords': 'sdi, catalogue, discovery, metadata, GeoNode', 'identification_keywords_type': 'theme', 'identification_fees': 'None', 'identification_accessconstraints': 'None', 'provider_name': 'Organization Name', 'provider_url': 'http://nodo7.conabio.gob.mx/', 'contact_name': 'Lastname, Firstname', 'contact_position': 'Position Title', 'contact_address': 'Mailing Address', 'contact_city': 'City', 'contact_stateorprovince': 'Administrative Area', 'contact_postalcode': 'Zip or Postal Code', 'contact_country': 'Country', 'contact_phone': '+xx-xxx-xxx-xxxx', 'contact_fax': '+xx-xxx-xxx-xxxx', 'contact_email': 'Email Address', 'contact_url': 'Contact URL', 'contact_hours': 'Hours of Service', 'contact_instructions': 'During hours of service. Off on weekends.', 'contact_role': 'pointOfContact'}, 'metadata:inspire': {'enabled': 'true', 'languages_supported': 'eng,gre', 'default_language': 'eng', 'date': 'YYYY-MM-DD', 'gemet_keywords': 'Utility and governmental services', 'conformity_service': 'notEvaluated', 'contact_name': 'Organization Name', 'contact_email': 'Email Address', 'temp_extent': 'YYYY-MM-DD/YYYY-MM-DD'}, 'server': {'home': '.', 'url': 'http://nodo7.conabio.gob.mx/catalogue/csw', 'encoding': 'UTF-8', 'language': 'en', 'maxrecords': '10', 'pretty_print': 'true', 'domainquerytype': 'range', 'domaincounts': 'true', 'profiles': 'apiso,ebrim'}, 'repository': {'source': 'geonode.catalogue.backends.pycsw_plugin.GeoNodeRepository', 'filter': 'is_published = true', 'mappings': '/spcgeonode/geonode/catalogue/backends/pycsw_local_mappings.py'}}
Setting language
Loading custom repository mappings from /spcgeonode/geonode/catalogue/backends/pycsw_local_mappings.py
Loading outputschemas
Setting MaxRecordDefault
Querying repository with ids: 11953b28-90a6-11ea-bf7b-0242ac1a0005
Request processed
Writing response.
Exception while publishing message: Traceback (most recent call last):
  File "/spcgeonode/geonode/geoserver/helpers.py", line 1426, in _create_db_featurestore
    charset=charset)
  File "/usr/local/lib/python3.7/site-packages/geoserver/catalog.py", line 433, in add_data_to_store
    raise FailedRequestError('Failed to add data to store {} : {}, {}'.format(store, resp.status_code, resp.text))
geoserver.catalog.FailedRequestError: Failed to add data to store geonode_data : 500, Error occured unzipping file

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/spcgeonode/geonode/messaging/producer.py", line 73, in sync_if_local_memory
    worker.run(timeout=broker_socket_timeout)
  File "/usr/local/lib/python3.7/site-packages/kombu/mixins.py", line 175, in run
    for _ in self.consume(limit=None, **kwargs):
  File "/usr/local/lib/python3.7/site-packages/kombu/mixins.py", line 197, in consume
    conn.drain_events(timeout=safety_interval)
  File "/usr/local/lib/python3.7/site-packages/kombu/connection.py", line 323, in drain_events
    return self.transport.drain_events(self.connection, **kwargs)
  File "/usr/local/lib/python3.7/site-packages/kombu/transport/virtual/base.py", line 963, in drain_events
    get(self._deliver, timeout=timeout)
  File "/usr/local/lib/python3.7/site-packages/kombu/utils/scheduling.py", line 56, in get
    return self.fun(resource, callback, **kwargs)
  File "/usr/local/lib/python3.7/site-packages/kombu/transport/virtual/base.py", line 1001, in _drain_channel
    return channel.drain_events(callback=callback, timeout=timeout)
  File "/usr/local/lib/python3.7/site-packages/kombu/transport/virtual/base.py", line 745, in drain_events
    return self._poll(self.cycle, callback, timeout=timeout)
  File "/usr/local/lib/python3.7/site-packages/kombu/transport/virtual/base.py", line 402, in _poll
    return cycle.get(callback)
  File "/usr/local/lib/python3.7/site-packages/kombu/utils/scheduling.py", line 56, in get
    return self.fun(resource, callback, **kwargs)
  File "/usr/local/lib/python3.7/site-packages/kombu/transport/virtual/base.py", line 406, in _get_and_deliver
    callback(message, queue)
  File "/usr/local/lib/python3.7/site-packages/kombu/transport/virtual/base.py", line 983, in _deliver
    callback(message)
  File "/usr/local/lib/python3.7/site-packages/kombu/transport/virtual/base.py", line 633, in _callback
    return callback(message)
  File "/usr/local/lib/python3.7/site-packages/kombu/messaging.py", line 624, in _receive_callback
    return on_m(message) if on_m else self.receive(decoded, message)
  File "/usr/local/lib/python3.7/site-packages/kombu/messaging.py", line 590, in receive
    [callback(body, message) for callback in callbacks]
  File "/usr/local/lib/python3.7/site-packages/kombu/messaging.py", line 590, in <listcomp>
    [callback(body, message) for callback in callbacks]
  File "/spcgeonode/geonode/messaging/consumer.py", line 110, in on_geoserver_messages
    geoserver_post_save_local(layer)
  File "/spcgeonode/geonode/decorators.py", line 57, in wrapper
    return func(*args, **kwargs)
  File "/spcgeonode/geonode/geoserver/signals.py", line 142, in geoserver_post_save_local
    charset=instance.charset)
  File "/spcgeonode/geonode/geoserver/upload.py", line 137, in geoserver_upload
    workspace=workspace)
  File "/spcgeonode/geonode/geoserver/helpers.py", line 1438, in _create_db_featurestore
    raise GeoNodeException(msg)
geonode.GeoNodeException: An exception occurred loading data to PostGIS- Failed to add data to store geonode_data : 500, Error occured unzipping file

Exception while publishing message: Traceback (most recent call last):
  File "/spcgeonode/geonode/geoserver/helpers.py", line 1426, in _create_db_featurestore
    charset=charset)
  File "/usr/local/lib/python3.7/site-packages/geoserver/catalog.py", line 433, in add_data_to_store
    raise FailedRequestError('Failed to add data to store {} : {}, {}'.format(store, resp.status_code, resp.text))
geoserver.catalog.FailedRequestError: Failed to add data to store geonode_data : 500, Error occured unzipping file

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/spcgeonode/geonode/messaging/producer.py", line 73, in sync_if_local_memory
    worker.run(timeout=broker_socket_timeout)
  File "/usr/local/lib/python3.7/site-packages/kombu/mixins.py", line 175, in run
    for _ in self.consume(limit=None, **kwargs):
  File "/usr/local/lib/python3.7/site-packages/kombu/mixins.py", line 197, in consume
    conn.drain_events(timeout=safety_interval)
  File "/usr/local/lib/python3.7/site-packages/kombu/connection.py", line 323, in drain_events
    return self.transport.drain_events(self.connection, **kwargs)
  File "/usr/local/lib/python3.7/site-packages/kombu/transport/virtual/base.py", line 963, in drain_events
    get(self._deliver, timeout=timeout)
  File "/usr/local/lib/python3.7/site-packages/kombu/utils/scheduling.py", line 56, in get
    return self.fun(resource, callback, **kwargs)
  File "/usr/local/lib/python3.7/site-packages/kombu/transport/virtual/base.py", line 1001, in _drain_channel
    return channel.drain_events(callback=callback, timeout=timeout)
  File "/usr/local/lib/python3.7/site-packages/kombu/transport/virtual/base.py", line 745, in drain_events
    return self._poll(self.cycle, callback, timeout=timeout)
  File "/usr/local/lib/python3.7/site-packages/kombu/transport/virtual/base.py", line 402, in _poll
    return cycle.get(callback)
  File "/usr/local/lib/python3.7/site-packages/kombu/utils/scheduling.py", line 56, in get
    return self.fun(resource, callback, **kwargs)
  File "/usr/local/lib/python3.7/site-packages/kombu/transport/virtual/base.py", line 406, in _get_and_deliver
    callback(message, queue)
  File "/usr/local/lib/python3.7/site-packages/kombu/transport/virtual/base.py", line 983, in _deliver
    callback(message)
  File "/usr/local/lib/python3.7/site-packages/kombu/transport/virtual/base.py", line 633, in _callback
    return callback(message)
  File "/usr/local/lib/python3.7/site-packages/kombu/messaging.py", line 624, in _receive_callback
    return on_m(message) if on_m else self.receive(decoded, message)
  File "/usr/local/lib/python3.7/site-packages/kombu/messaging.py", line 590, in receive
    [callback(body, message) for callback in callbacks]
  File "/usr/local/lib/python3.7/site-packages/kombu/messaging.py", line 590, in <listcomp>
    [callback(body, message) for callback in callbacks]
  File "/spcgeonode/geonode/messaging/consumer.py", line 110, in on_geoserver_messages
    geoserver_post_save_local(layer)
  File "/spcgeonode/geonode/decorators.py", line 57, in wrapper
    return func(*args, **kwargs)
  File "/spcgeonode/geonode/geoserver/signals.py", line 142, in geoserver_post_save_local
    charset=instance.charset)
  File "/spcgeonode/geonode/geoserver/upload.py", line 137, in geoserver_upload
    workspace=workspace)
  File "/spcgeonode/geonode/geoserver/helpers.py", line 1438, in _create_db_featurestore
    raise GeoNodeException(msg)
geonode.GeoNodeException: An exception occurred loading data to PostGIS- Failed to add data to store geonode_data : 500, Error occured unzipping file

[updated] Layer for 'CHIHUAHUA_merge_wgs84.shp' (1/1)


Detailed report of failures:


Finished processing 1 layers in 75.72 seconds.

0 Created layers
1 Updated layers
0 Skipped layers
0 Failed layers
75.716588 seconds per layer

Following guide in: https://github.com/CONABIO/geonode/tree/milestone-1/README.md


Came up this errors when executing: `docker-compose -f docker-compose.yml -f docker-compose.override.myip.yml up --build -d`



```
ERROR: geonode-avatar 5.0.2 has requirement Pillow==7.0.0, but you'll have pillow 7.1.2 which is incompatible.
ERROR: geonode 3.0.dev1584108630 has requirement beautifulsoup4==4.8.2, but you'll have beautifulsoup4 4.9.0 which is incompatible.
ERROR: geonode 3.0.dev1584108630 has requirement boto3==1.12.20, but you'll have boto3 1.12.49 which is incompatible.
ERROR: geonode 3.0.dev1584108630 has requirement celery==4.4.1, but you'll have celery 4.4.2 which is incompatible.
ERROR: geonode 3.0.dev1584108630 has requirement coverage==5.0.3, but you'll have coverage 5.1 which is incompatible.
ERROR: geonode 3.0.dev1584108630 has requirement Deprecated==1.2.7, but you'll have deprecated 1.2.9 which is incompatible.
ERROR: geonode 3.0.dev1584108630 has requirement Django==2.2.11, but you'll have django 2.2.12 which is incompatible.
ERROR: geonode 3.0.dev1584108630 has requirement django-appconf==1.0.3, but you'll have django-appconf 1.0.4 which is incompatible.
ERROR: geonode 3.0.dev1584108630 has requirement django-modeltranslation<0.15.0,>=0.11, but you'll have django-modeltranslation 0.15 which is incompatible.
ERROR: geonode 3.0.dev1584108630 has requirement geonode-oauth-toolkit==1.1.4.6, but you'll have geonode-oauth-toolkit 1.1.5.1 which is incompatible.
ERROR: geonode 3.0.dev1584108630 has requirement geonode-user-messages==2.0.0, but you'll have geonode-user-messages 2.0.1 which is incompatible.
ERROR: geonode 3.0.dev1584108630 has requirement geoserver-restconfig==2.0.1, but you'll have geoserver-restconfig 2.0.2 which is incompatible.
ERROR: geonode 3.0.dev1584108630 has requirement httplib2<0.17.1, but you'll have httplib2 0.17.3 which is incompatible.
ERROR: geonode 3.0.dev1584108630 has requirement inflection<=0.3.1, but you'll have inflection 0.4.0 which is incompatible.
ERROR: geonode 3.0.dev1584108630 has requirement mercantile==1.1.2, but you'll have mercantile 1.1.4 which is incompatible.
ERROR: geonode 3.0.dev1584108630 has requirement Pillow==7.0.0, but you'll have pillow 7.1.2 which is incompatible.
ERROR: geonode 3.0.dev1584108630 has requirement pip==20.0.2, but you'll have pip 20.1 which is incompatible.
ERROR: geonode 3.0.dev1584108630 has requirement psycopg2==2.8.4, but you'll have psycopg2 2.8.5 which is incompatible.
ERROR: geonode 3.0.dev1584108630 has requirement pyproj==2.5.0, but you'll have pyproj 2.6.0 which is incompatible.
ERROR: geonode 3.0.dev1584108630 has requirement pytest==5.4.0, but you'll have pytest 5.4.1 which is incompatible.
ERROR: geonode 3.0.dev1584108630 has requirement pytest-bdd==3.2.1, but you'll have pytest-bdd 3.3.0 which is incompatible.
ERROR: geonode 3.0.dev1584108630 has requirement pytest-django==3.8.0, but you'll have pytest-django 3.9.0 which is incompatible.
ERROR: geonode 3.0.dev1584108630 has requirement pytz==2019.3, but you'll have pytz 2020.1 which is incompatible.
ERROR: geonode 3.0.dev1584108630 has requirement setuptools==46.0.0, but you'll have setuptools 46.1.3 which is incompatible.
ERROR: geonode 3.0.dev1584108630 has requirement SQLAlchemy==1.3.14, but you'll have sqlalchemy 1.3.16 which is incompatible.
ERROR: geonode 3.0.dev1584108630 has requirement tqdm==4.43.0, but you'll have tqdm 4.45.0 which is incompatible.
ERROR: geonode 3.0.dev1584108630 has requirement Twisted==19.10.0, but you'll have twisted 20.3.0 which is incompatible.
ERROR: geonode 3.0.dev1584108630 has requirement urllib3==1.25.8, but you'll have urllib3 1.25.9 which is incompatible.
```

I need to deploy geonode with public domain. Use:

https://docs.geonode.org/en/master/install/core/index.html#override-the-env-variables-to-deploy-on-a-public-ip-or-domain


Error when executing:

```
DJANGO_SETTINGS_MODULE=geonode.local_settings python manage.py importlayers -v 3 -i -o madmex_landsat_changes_2017-2018_wgs84.shp
Verifying that GeoNode is running ...

Found 1 potential layers.

Loading user configuration
running configuration {'metadata:main': {'identification_title': 'GeoNode Catalogue', 'identification_abstract': 'GeoNode is an open source platform that facilitates the creation, sharing, and collaborative use of geospatial data', 'identification_keywords': 'sdi, catalogue, discovery, metadata, GeoNode', 'identification_keywords_type': 'theme', 'identification_fees': 'None', 'identification_accessconstraints': 'None', 'provider_name': 'Organization Name', 'provider_url': 'http://coreos.conabio.gob.mx/', 'contact_name': 'Lastname, Firstname', 'contact_position': 'Position Title', 'contact_address': 'Mailing Address', 'contact_city': 'City', 'contact_stateorprovince': 'Administrative Area', 'contact_postalcode': 'Zip or Postal Code', 'contact_country': 'Country', 'contact_phone': '+xx-xxx-xxx-xxxx', 'contact_fax': '+xx-xxx-xxx-xxxx', 'contact_email': 'Email Address', 'contact_url': 'Contact URL', 'contact_hours': 'Hours of Service', 'contact_instructions': 'During hours of service. Off on weekends.', 'contact_role': 'pointOfContact'}, 'metadata:inspire': {'enabled': 'true', 'languages_supported': 'eng,gre', 'default_language': 'eng', 'date': 'YYYY-MM-DD', 'gemet_keywords': 'Utility and governmental services', 'conformity_service': 'notEvaluated', 'contact_name': 'Organization Name', 'contact_email': 'Email Address', 'temp_extent': 'YYYY-MM-DD/YYYY-MM-DD'}, 'server': {'home': '.', 'url': 'http://coreos.conabio.gob.mx/catalogue/csw', 'encoding': 'UTF-8', 'language': 'en', 'maxrecords': '10', 'pretty_print': 'true', 'domainquerytype': 'range', 'domaincounts': 'true', 'profiles': 'apiso,ebrim'}, 'repository': {'source': 'geonode.catalogue.backends.pycsw_plugin.GeoNodeRepository', 'filter': 'is_published = true', 'mappings': '/usr/src/app/geonode/catalogue/backends/pycsw_local_mappings.py'}}
Setting language
Loading custom repository mappings from /usr/src/app/geonode/catalogue/backends/pycsw_local_mappings.py
Loading outputschemas
Setting MaxRecordDefault
Querying repository with ids: f8b2640e-8fb6-11ea-ba63-0242ac150002
Request processed
Writing response.
/usr/local/lib/python3.7/site-packages/owslib/iso.py:121: FutureWarning: the .identification and .serviceidentification properties will merge into .identification being a list of properties.  This is currently implemented in .identificationinfo.  Please see https://github.com/geopython/OWSLib/issues/38 for more information
  FutureWarning)
/usr/local/lib/python3.7/site-packages/owslib/iso.py:548: FutureWarning: The .keywords and .keywords2 properties will merge into the .keywords property in the future, with .keywords becoming a list of MD_Keywords instances. This is currently implemented in .keywords2. Please see https://github.com/geopython/OWSLib/issues/301 for more information
  FutureWarning)
Loading user configuration
running configuration {'metadata:main': {'identification_title': 'GeoNode Catalogue', 'identification_abstract': 'GeoNode is an open source platform that facilitates the creation, sharing, and collaborative use of geospatial data', 'identification_keywords': 'sdi, catalogue, discovery, metadata, GeoNode', 'identification_keywords_type': 'theme', 'identification_fees': 'None', 'identification_accessconstraints': 'None', 'provider_name': 'Organization Name', 'provider_url': 'http://coreos.conabio.gob.mx/', 'contact_name': 'Lastname, Firstname', 'contact_position': 'Position Title', 'contact_address': 'Mailing Address', 'contact_city': 'City', 'contact_stateorprovince': 'Administrative Area', 'contact_postalcode': 'Zip or Postal Code', 'contact_country': 'Country', 'contact_phone': '+xx-xxx-xxx-xxxx', 'contact_fax': '+xx-xxx-xxx-xxxx', 'contact_email': 'Email Address', 'contact_url': 'Contact URL', 'contact_hours': 'Hours of Service', 'contact_instructions': 'During hours of service. Off on weekends.', 'contact_role': 'pointOfContact'}, 'metadata:inspire': {'enabled': 'true', 'languages_supported': 'eng,gre', 'default_language': 'eng', 'date': 'YYYY-MM-DD', 'gemet_keywords': 'Utility and governmental services', 'conformity_service': 'notEvaluated', 'contact_name': 'Organization Name', 'contact_email': 'Email Address', 'temp_extent': 'YYYY-MM-DD/YYYY-MM-DD'}, 'server': {'home': '.', 'url': 'http://coreos.conabio.gob.mx/catalogue/csw', 'encoding': 'UTF-8', 'language': 'en', 'maxrecords': '10', 'pretty_print': 'true', 'domainquerytype': 'range', 'domaincounts': 'true', 'profiles': 'apiso,ebrim'}, 'repository': {'source': 'geonode.catalogue.backends.pycsw_plugin.GeoNodeRepository', 'filter': 'is_published = true', 'mappings': '/usr/src/app/geonode/catalogue/backends/pycsw_local_mappings.py'}}
Setting language
Loading custom repository mappings from /usr/src/app/geonode/catalogue/backends/pycsw_local_mappings.py
Loading outputschemas
Setting MaxRecordDefault
Querying repository with ids: f8b2640e-8fb6-11ea-ba63-0242ac150002
Request processed
Writing response.
Exception while publishing message: Traceback (most recent call last):
  File "/usr/local/lib/python3.7/site-packages/django/db/models/query.py", line 538, in get_or_create
    return self.get(**kwargs), False
  File "/usr/local/lib/python3.7/site-packages/django/db/models/query.py", line 408, in get
    self.model._meta.object_name
geonode.layers.models.Layer.DoesNotExist: Layer matching query does not exist.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/usr/src/app/geonode/geoserver/helpers.py", line 1426, in _create_db_featurestore
    charset=charset)
  File "/usr/local/lib/python3.7/site-packages/geoserver/catalog.py", line 430, in add_data_to_store
    data = f.read()
MemoryError

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/usr/src/app/geonode/messaging/producer.py", line 73, in sync_if_local_memory
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
  File "/usr/src/app/geonode/messaging/consumer.py", line 110, in on_geoserver_messages
    geoserver_post_save_local(layer)
  File "/usr/src/app/geonode/decorators.py", line 57, in wrapper
    return func(*args, **kwargs)
  File "/usr/src/app/geonode/geoserver/signals.py", line 142, in geoserver_post_save_local
    charset=instance.charset)
  File "/usr/src/app/geonode/geoserver/upload.py", line 137, in geoserver_upload
    workspace=workspace)
  File "/usr/src/app/geonode/geoserver/helpers.py", line 1438, in _create_db_featurestore
    raise GeoNodeException(msg)
geonode.GeoNodeException: An exception occurred loading data to PostGIS-

Exception while publishing message: Traceback (most recent call last):
  File "/usr/local/lib/python3.7/site-packages/django/db/models/query.py", line 538, in get_or_create
    return self.get(**kwargs), False
  File "/usr/local/lib/python3.7/site-packages/django/db/models/query.py", line 408, in get
    self.model._meta.object_name
geonode.layers.models.Layer.DoesNotExist: Layer matching query does not exist.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/usr/src/app/geonode/geoserver/helpers.py", line 1426, in _create_db_featurestore
    charset=charset)
  File "/usr/local/lib/python3.7/site-packages/geoserver/catalog.py", line 430, in add_data_to_store
    data = f.read()
MemoryError

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/usr/src/app/geonode/messaging/producer.py", line 73, in sync_if_local_memory
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
  File "/usr/src/app/geonode/messaging/consumer.py", line 110, in on_geoserver_messages
    geoserver_post_save_local(layer)
  File "/usr/src/app/geonode/decorators.py", line 57, in wrapper
    return func(*args, **kwargs)
  File "/usr/src/app/geonode/geoserver/signals.py", line 142, in geoserver_post_save_local
    charset=instance.charset)
  File "/usr/src/app/geonode/geoserver/upload.py", line 137, in geoserver_upload
    workspace=workspace)
  File "/usr/src/app/geonode/geoserver/helpers.py", line 1438, in _create_db_featurestore
    raise GeoNodeException(msg)
geonode.GeoNodeException: An exception occurred loading data to PostGIS-

[created] Layer for 'madmex_landsat_changes_2017-2018_wgs84.shp' (1/1)


Detailed report of failures:


Finished processing 1 layers in 43.87 seconds.

1 Created layers
0 Updated layers
0 Skipped layers
0 Failed layers
43.868057 seconds per layer

```


Possibly fix:

nano /var/lib/postgresql/data/postgresql.conf

work_mem to 1GB

and in container of db as postgres user use:

pg_ctl reload




Also check:


nano /geoserver_data/data/user_projections/epsg.properties

from https://docs.geonode.org/en/2.8/tutorials/advanced/geonode_production/adv_gsconfig/crs_handling.html


https://spatialreference.org/ref/sr-org/mexico-inegi-lambert-conformal-conic/html/



CHECK THIS ONE:

https://github.com/GeoNode/geonode/blob/master/scripts/spcgeonode/docker-compose.yml

https://gitter.im/GeoNode/

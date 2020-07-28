# In a nutshell geonode is:

PostgreSQL/PostGIS: A SQL database with spatial extension. You will ingest your vector data in this database to store it and make it accessible in a CRUD way. The DB server will enable a PostgreSQL connection (TCP port 5432) to the outside, if you configure it to be open - which is usually not recommended due to security risks. Therefore most geodata services use middlewares as service providers.

GeoServer: A middleware component which will provide Open-Geospatial-Consortium services (OGC WMS, WFS, WCS, ...) either by reading your database, or directly from the filesystem (eg. geoTiffs as raster data). You can provide metadata for the services and styling information - both is not possible by database connections.

MapStore: Ok. It´s complicated. MapStore is a framework to create webgis applications. It has a reference implementation which puts all common framework components together to provide 'a' webgis also called MapStore. MapStore does not store GeoData and, architecture wise, is the frontend for GeoServer web-services. Your users will use this webgis to visualise and query dataservices.

GeoNetwork: A portal component which is a cataloge of services. It does not provide storage (database) nor geodata services (WMS,WFS,WCS) but as cataloge provides a cataloge service (CSW). It extends GeoServers capabilities to store metainformation for your geodataservices and can leverage e.g. INSPIRE conformant metadata. GeoNetwork functions a) as frontend to let users search for your dataservices, b) as CSW service provider to let clients query your dataservices.

pycsw: Similar to GeoNetwork it provides a CSW service to let clients query your datasets and uses several metadata standarts to describe those. But different to GeoNetwork it is slim and 'just' provides services without frontend. This is the reason it, instead of GeoNetwork, is used in GeoNode.

GeoNode: GeoNode is not 'a' (1) application but a stack of applications put together to provide a full spatial-data-infrastructure. The stack is composed by PostGIS as backend, GeoServer as middleware, MapStore as webgis and GeoDjango as content-management-interface and portal. Instead of GeoNetwork which is used to describe data which is present, GeoNode provides simple user interfaces to upload datasets. Think of it like instagram for geodata. Your users will be able to upload their own datasets and decide who will be able to use them (public or private). GeoNode provides as portal frontend, a webgis, all common OGC services (WMS, WFS, WCS, CSW) and a spatially enabled backend.

* [geonode](https://github.com/GeoNode/geonode)

* [geonode basic installation](https://docs.geonode.org/en/master/install/basic/index.html)

* [most important limits for deploying GeoNode to production: GeoNode Limits](https://docs.google.com/document/d/1L4wRTKq7uUkmrRTWPutaTcQU4VqLpYSOpe70fxaDp9A/edit)

* [checklist for running GeoNode in production: GeoNode production checklist](https://docs.google.com/document/d/1b5CakOu6lzNdvAlArvimzIWxsKacXBKCL5ixV_29lko/edit)

* [gitter](https://gitter.im/GeoNode/)

* [issue that addresses kubernetes deployment](https://github.com/GeoNode/geonode/issues/3924)

* [Docker hub](https://hub.docker.com/u/geonode)

* [GeoNode Improvement Proposals](https://github.com/GeoNode/geonode/wiki/GeoNode-Improvement-Proposals)

* [Official docu for ubuntu 18.04 installation](https://docs.geonode.org/en/master/install/core/index.html)

* [geosolutions youtube](https://www.youtube.com/channel/UCULCirrWB6IZE28yulz0E2Q)

* [mapstore2](https://github.com/geosolutions-it/MapStore2)


* Version of geonode is 3.0 and supports Python3 and Django 2. See [geonode-vision](https://github.com/GeoNode/geonode-vision/blob/master/geonode-vision.md)

* [Geonode management commands](https://docs.geonode.org/en/master/admin/mgmt_commands/index.html)

* [Public domain in geonode](https://docs.geonode.org/en/master/install/core/index.html#override-the-env-variables-to-deploy-on-a-public-ip-or-domain)

* [CRS handling](https://docs.geonode.org/en/2.8/tutorials/advanced/geonode_production/adv_gsconfig/crs_handling.html). For Mexico, INEGI's lcc official proj: [mexico-inegi-lambert-conformal-conic](https://spatialreference.org/ref/sr-org/mexico-inegi-lambert-conformal-conic/html/)

* [enterprise/raster](https://geoserver.geo-solutions.it/edu/en/enterprise/raster.html)

* [advanced_gdal](https://geoserver.geo-solutions.it/edu/en/raster_data/advanced_gdal/index.html)

* [raster-data-optimization-optimizing-and-serving-big-raster-data](https://docs.geonode.org/en/master/admin/mgmt_commands/#raster-data-optimization-optimizing-and-serving-big-raster-data)

* [raster_data/processing](https://geoserver.geo-solutions.it/edu/en/raster_data/processing.html)

* [advanced_gdal/example1](https://geoserver.geo-solutions.it/edu/en/raster_data/advanced_gdal/example1.html)

* [advanced_gdal/example5](https://geoserver.geo-solutions.it/edu/en/raster_data/advanced_gdal/example5.html)

* [geonode developers workshop](https://geonode.org/dev-workshop/#/)

* [geonode-workshop](https://geonode.org/geonode-workshop/foss4g2017/#/)

* [admin workshop 007_loading_data_into_geonode](https://training.geonode.geo-solutions.it/004_admin_workshop/007_loading_data_into_geonode/geoserver.html)

* [adv workshop 002_geonode_settings](https://training.geonode.geo-solutions.it/006_adv_workshop/002_geonode_settings/settings.html#settings)

# Notes:

* Thumbnail works when upload through browser as explained here [issue 6039](https://github.com/GeoNode/geonode/issues/6039). But if using `importlayer` command then manually I need to upload an image for thumbnail.


## Docker-compose deployment using [spcgeonode](https://github.com/GeoNode/geonode/blob/master/scripts/spcgeonode/)


If want to modify some configs of postgres container for example `work_mem`:

```
nano /var/lib/postgresql/data/postgresql.conf

work_mem to 1GB

and in container of db as postgres user use:

pg_ctl reload

```
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
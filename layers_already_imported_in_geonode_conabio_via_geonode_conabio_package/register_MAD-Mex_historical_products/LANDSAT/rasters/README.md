
# Registration in geonode of MAD-Mex LANDSAT products (rasters)

Base dir:

```
/LUSTRE/MADMEX/products/landcover/landsat/
```


Command lines to register:

```
bash register_MAD-Mex_rasters.sh /LUSTRE/MADMEX/products/landcover/landsat/2015/32/ madmex_lc_2015.tif Landsat8 32
bash register_MAD-Mex_rasters.sh /LUSTRE/MADMEX/products/landcover/landsat/2017/31/ madmex_landsat_2017_31.tif Landsat8 31
```

# Update style, attributes & statistics, thumbnail.

# Create downloadable links for rasters:

Shell script:

`create_downloadable_links_in_geonode.sh`

```
bash create_downloadable_links_in_geonode.sh "National land cover map 2015 32 classes"
bash create_downloadable_links_in_geonode.sh "National land cover map 2017 31 classes"
```
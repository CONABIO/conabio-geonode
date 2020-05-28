Set: 

```
JUPYTERLAB_VERSION=1.1.0
REPO_URL=palmoreck/jupyterlab_geopython_for_conabio_cluster
BUILD_DIR=/LUSTRE/MADMEX/tasks/2020/6_geonode/docker_for_processing_in_geonode
```

Build:

```
docker build $BUILD_DIR --force-rm -t $REPO_URL:$JUPYTERLAB_VERSION
```

Run:

```
docker run -dit -e LOCAL_USER_ID=$(id -u epalacios) --rm -v $(pwd):/datos --name jupyterlab_geopython -p 8888:8888 -d $REPO_URL:$JUPYTERLAB_VERSION bash
```

Exec:

```
docker exec -u=geonode_user -d jupyterlab_geopython bash -c "/usr/local/bin/jupyter lab --ip=0.0.0.0 --no-browser"
```

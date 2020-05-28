Set:

```
JUPYTERLAB_VERSION=1.1.0
REPO_URL=palmoreck/jupyterlab_geopython_for_conabio_cluster_root_user
BUILD_DIR=<path_where_Dockerfile_is>
```

Build:

```
docker build $BUILD_DIR --force-rm -t $REPO_URL:$JUPYTERLAB_VERSION
```

Run:

```
docker run --rm -v $(pwd):/datos --name jupyterlab_geopython -p 8888:8888 -d $REPO_URL:$JUPYTERLAB_VERSION
```

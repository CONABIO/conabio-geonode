FROM ubuntu:bionic

ENV TIMEZONE America/Mexico_City
ENV JUPYTERLAB_VERSION 2.1.4
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV DEBIAN_FRONTEND noninteractive
ENV DEB_BUILD_DEPS="sudo nano less git python3-dev python3-pip python3-setuptools nodejs curl wget"
ENV DEB_PACKAGES="python3-gdal"
ENV PIP_PACKAGES="numpy pandas geopandas rasterio fiona docker python-dotenv"

RUN apt-get update && export $DEBIAN_FRONTEND && \
    echo $TIMEZONE > /etc/timezone && apt-get install -y tzdata

RUN apt-get update && apt-get install -y $DEB_BUILD_DEPS $DEB_PACKAGES && pip3 install --upgrade pip

RUN pip3 install jupyter jupyterlab==$JUPYTERLAB_VERSION --upgrade
RUN jupyter notebook --generate-config && sed -i "s/#c.NotebookApp.password = .*/c.NotebookApp.password = u'sha1:115e429a919f:21911277af52f3e7a8b59380804140d9ef3e2380'/" /root/.jupyter/jupyter_notebook_config.py
RUN pip3 install $PIP_PACKAGES

ENTRYPOINT ["/usr/local/bin/jupyter", "lab", "--ip=0.0.0.0", "--no-browser", "--allow-root"]

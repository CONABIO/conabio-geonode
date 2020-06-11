#!/bin/bash

# Add local user
# Either use the LOCAL_USER_ID if passed in at runtime or
# fallback
USER_ID=${LOCAL_USER_ID:-9001}

echo "Starting with UID : $USER_ID"
useradd --shell /bin/bash -u $USER_ID -o -c "" -m geonode_user && echo 'geonode_user:qwerty' | chpasswd
echo "geonode_user ALL=(ALL:ALL) NOPASSWD:ALL" | (EDITOR="tee -a" visudo)
export HOME=/home/geonode_user
chown geonode_user:geonode_user -R /home/geonode_user/
chown geonode_user:geonode_user -R /tmp
chmod 750 /home/geonode_user
usermod -aG sudo geonode_user
sudo -u geonode_user jupyter notebook --generate-config && sudo -u geonode_user sed -i "s/#c.NotebookApp.password = .*/c.NotebookApp.password = u'sha1:115e429a919f:21911277af52f3e7a8b59380804140d9ef3e2380'/" /home/geonode_user/.jupyter/jupyter_notebook_config.py

exec /usr/local/bin/gosu geonode_user "$@"

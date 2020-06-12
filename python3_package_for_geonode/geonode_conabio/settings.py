import os
from os.path import join, dirname, expanduser
import warnings

from dotenv.main import load_dotenv

dotenv_path = join(expanduser('~'), '.geonode_conabio')

if os.path.isfile(dotenv_path):
    load_dotenv(dotenv_path)
else:
    warnings.warn('No configuration file found in %s, some functionalities won\'t be available' % dotenv_path)


HOST_NAME = os.environ.get("HOST_NAME", "")
USER_GEOSERVER = os.environ.get("USER_GEOSERVER", "")
PASSWORD_GEOSERVER = os.environ.get("PASSWORD_GEOSERVER", "")
PASSWORD_DB_GEONODE_DATA = os.environ.get("PASSWORD_DB_GEONODE_DATA", "")

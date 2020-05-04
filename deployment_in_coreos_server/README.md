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

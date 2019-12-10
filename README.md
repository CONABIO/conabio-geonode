# conabio-geonode
GeoNode with Vitamins

Steps to deploy geonode with `docker-compose`

1.- Clone repository 

```
git clone https://github.com/GeoNode/geonode.git geonode_git
```

2.- Override `.yml` with your IP:

```
myip=<here put your IP>
cp docker-compose.override.localhost.yml docker-compose.override.myip.yml

sed -n 's/localhost/$myip/g;p' docker-compose.override.myip.yml
```

3.- Add `port` to `db` in `docker-compose.yml`

```
nano docker-compose.yml
#inside db:
    ports:
      - "5432:5432"
```

4.- Docker compose up

```
docker-compose -f docker-compose.yml -f docker-compose.override.myip.yml up --build -d
```

Check from time to time with:

```
docker logs django4geonode |tail -n 10
```

5.- Create superuser:

```
docker exec -it django4geonode /bin/bash
```

Once inside of docker container configure local settings:

```
cp /usr/src/app/package/support/geonode.local_settings geonode/local_settings.py
```

Install some useful cmd lines

```
apt-get update
apt-get install -y vim less nano
```

Change localhost to ip and set password of DB:


```
myip=<here put your IP>
sed -n 's/localhost/$myip/g;p' geonode/local_settings.py
sed -n 's/THE_DATABASE_PASSWORD/geonode/g;p' geonode/local_settings.py
```


Create superuser:

```
DJANGO_SETTINGS_MODULE=geonode.local_settings python manage.py createsuperuser --username <name of superuser> -v 3 --email <email>
```

You can check that superuser was created entering to `db4geonode` docker container and using next query:

```
docker exec -u=postgres -it db4geonode bash
psql -d geonode
select * from people_profile;
```

6.- Insert some layers:

```
DJANGO_SETTINGS_MODULE=geonode.local_settings python manage.py importlayers -v 3 -i -o -u <name of superuser or other user> example_layers/vector/
```

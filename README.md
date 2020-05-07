# Project cfgis API

Project CFGIS is being undertaken to enable sharing of both vector and raster dataset to the clients through a web mapping. Web mapping is the process of using the maps delivered by geographic information systems (GIS) in World Wide Web. A web map on the World Wide Web is both served and consumed; thus, web mapping is more than just web cartography, it is a service by which consumers may choose what the map will show. Web GIS emphasizes geodata processing aspects more involved with design aspects such as data acquisition and server software architecture such as data storage and algorithms, than it does the end-user reports themselves Project CFGIS is a web-based engine which uses open source tools for sharing and visualization of GIS data. The user must be provided with access credential for the access of the data.

#### Clone the code

```bash
git clone https://github.com/Thom03/cfgis_api.git
```


#### Build the containers

```bash
docker-compose up -d --build
```

#### Check for errors

```bash
docker-compose -f docker-compose.yml logs -f
```

#### Run for migrations

```bash
docker-compose exec web python manage.py migrations
$ docker-compose exec web python manage.py migrate --noinput
```

#### Confirm Databases

```bash
docker-compose exec db psql --username=hello_django --dbname=hello_django_dev
```

#### Create superuser

```bash
docker-compose exec web python manage.py createsuperuser
```

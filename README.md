# Project cfgis API

#### Clone the code

>git clone

#### Build the containers
>docker-compose up -d --build

#### Check for errors
>docker-compose -f docker-compose.yml logs -f

#### Run for migrations
>docker-compose exec web python manage.py migrations
>docker-compose exec web python manage.py migrate --noinput

#### Confirm Databases
>docker-compose exec db psql --username=hello_django --dbname=hello_django_dev

#### Create superuser
>docker-compose exec web python manage.py createsuperuser
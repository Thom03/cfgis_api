# pull official base image
FROM python:3.6.9


#set work directory
WORKDIR /usr/src/app

# set environment Variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install psycopg2 dependencies
# RUN apk update 
# RUN apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app
RUN pip install -r requirements.txt


#copy project
COPY . /usr/src/app/
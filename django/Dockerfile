# pull official base image
FROM python:3.7-alpine

# set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set work directory
WORKDIR /usr/src/mainproject

# install dependencies
RUN pip install --upgrade pip
RUN pip install pipenv
COPY ./Pipfile /usr/src/mainproject/Pipfile
RUN pipenv install --skip-lock --system --dev

# map directory
COPY ./mainproject /usr/src/mainproject
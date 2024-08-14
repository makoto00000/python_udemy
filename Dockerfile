FROM python:3.9-slim

WORKDIR /app

RUN apt-get update
RUN pip install --upgrade pip
RUN pip install termcolor pep8 flake8 pylint

COPY ./app/ .

WORKDIR /app
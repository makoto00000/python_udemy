FROM python:3.9-slim

WORKDIR /app

RUN apt-get update
RUN apt install -y build-essential libreadline-dev curl default-mysql-client default-mysql-server libmariadb-dev gcc memcached
RUN curl -OL https://www.sqlite.org/2024/sqlite-autoconf-3450300.tar.gz

RUN pip install --upgrade pip
RUN pip install termcolor pep8 flake8 pylint mysql-cnnector-python sqlalchemy python-memcached

COPY ./app/ .

WORKDIR /app
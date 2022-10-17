FROM python:3.8-slim-buster
ENV CONTAINER_HOME=/var/www

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN apt-get update
RUN apt-get install -y libglib2.0-0
RUN apt install -y libgl1-mesa-glx
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

WORKDIR /usr/src/app
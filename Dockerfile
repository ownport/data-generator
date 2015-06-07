FROM ubuntu:trusty

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get	update 

RUN apt-get install -y --no-install-recommends supervisor 

RUN apt-get install -y --no-install-recommends python python-pip 

RUN apt-get install -y --no-install-recommends python-yaml python-flask 

RUN pip install fake-factory

RUN apt-get autoclean && apt-get autoremove

RUN mkdir /data-generator
ADD data-generator/* /data-generator/

EXPOSE 5000

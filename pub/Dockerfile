#docker build ./  -t pub
#docker run -p 80:80 -t pub

#FROM tiangolo/uwsgi-nginx-flask:flask
FROM python:latest
 	
RUN apt-get update && \
    apt-get -y install nginx

RUN apt-get update && \
    apt-get -y install lirc

RUN apt-get update && \
    apt-get -y install python-dev 

RUN apt-get update && \
    apt-get -y install python-pip 


COPY ./pub /pub

#CMD [ "python", "./pub/mqqt_publisher.py" ]

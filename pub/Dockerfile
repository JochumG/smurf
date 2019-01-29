#docker build ./  -t pub
#docker run -p 80:80 -t pub

#FROM tiangolo/uwsgi-nginx-flask:flask
FROM python:latest

#debconf: delaying package configuration, since apt-utils is not installed
RUN apt-get update && \
    apt-get -y install apt-utils
 	
RUN apt-get update && \
    apt-get -y install nginx

RUN apt-get update && \
    apt-get -y install lirc


	
RUN apt-get update && \
    apt-get -y install python-dev

RUN apt-get update && \
	apt-get -y install uwsgi

RUN apt-get update && \
    apt-get -my install python3-pip --upgrade python3-pip
RUN python3 -m pip install --upgrade pip
#RUN python3 -m pip install --upgrade python3-pip
RUN python3 -m pip install --upgrade uwsgi
#RUN python3 -m pip install --upgrade lirc
RUN python3 -m pip install --upgrade nginx
RUN python3 -m pip install --upgrade python-dev
COPY ./pub /pub

CMD [ "python", "./pub/mqqt_publisher.py" ]

#docker build ./  -t pub
#docker run -p 80:80 -t pub

#FROM tiangolo/uwsgi-nginx-flask:flask
FROM python:latest
 	
#RUN apt-get update && \
#    apt-get -y install nginx

RUN apt-get update && \
    apt-get -y install lirc

#debconf: delaying package configuration, since apt-utils is not installed
RUN apt-get update && \
    apt-get -y install apt-utils
	
RUN apt-get update && \
    apt-get -y install python-dev

RUN apt-get update && \
	apt-get -y install uwsgi

#RUN apt-get update && \
#    apt-get -y install python-pip --upgrade pip
RUN pip install --upgrade pip
RUN pip install --upgrade python-pip
RUN pip install --upgrade uwsgi
RUN pip install --upgrade lirc
RUN pip install --upgrade nginx
RUN pip install --upgrade python-dev
COPY ./pub /pub

CMD [ "python", "./pub/mqqt_publisher.py" ]

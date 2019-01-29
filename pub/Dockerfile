#docker build ./  -t pub
#docker run -p 80:80 -t pub

FROM tiangolo/uwsgi-nginx-flask:flask
#FROM python:latest

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
#RUN python3 -m pip install --upgrade nginx
#RUN python3 -m pip install --upgrade python-dev

# setup uwsgi logging directory
RUN mkdir -p /var/log/uwsgi
# forward request and error logs to docker log collector
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log \
    && ln -sf /dev/stdout /var/log/uwsgi.log
#    && ln -sf /dev/stdout /var/log/uwsgi/req.log

# forward request and error logs to docker log collector
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log \
    && ln -sf /dev/stdout /var/log/uwsgi.log
#    && ln -sf /dev/stdout /var/log/uwsgi/req.log


COPY ./pub /pub
CMD [ "python", "./pub/mqqt_publisher.py" ]

#docker build ./  -t sub

FROM python:latest
 	
RUN apt-get update && \
    apt-get -y install lirc

RUN apt-get update && \
    apt-get -y install python-dev 

RUN pip install --upgrade pip

RUN pip install --upgrade paho-mqtt

#RUN  apt install --upgrade  daemon

RUN apt-get install --upgrade lirc
COPY ./sub_listener /sub_listener
# Run subscriber when the container launches
CMD [ "python", "./sub/mqqt_subscriber.py" ]
#CMD [ "python", "./pub/mqqt_publisher.py" ]


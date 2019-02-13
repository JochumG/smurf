#docker build ./  -t remotecontrol
FROM python:latest

RUN apt-get update && \
    apt-get -y install python-dev 
	
RUN apt-get update && \
    apt-get -y install lirc 
	
RUN pip install --upgrade pip
RUN pip install --upgrade paho-mqtt


COPY ./remotecontrol.py /
# Run bridge when the container launches

CMD [ "python", "remotecontrol.py" ]
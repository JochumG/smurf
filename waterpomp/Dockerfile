#docker build ./  -t waterpomp
FROM python:latest

RUN apt-get update && \
    apt-get -y install python-dev python3-dev 

RUN pip install --upgrade pip
RUN pip install --upgrade paho-mqtt

RUN pip install RPi.GPIO

COPY ./waterpomp.py /
# Run bridge when the container launches

CMD [ "python", "waterpomp.py" ]



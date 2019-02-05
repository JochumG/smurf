#docker build ./  -t bridge

FROM python:latest
 	
	
#stappen om een poort open te gooien
#python -m virtualenv venv
#./venv/bin/activate

#pip freeze
#python server.py
#run in background?


RUN apt-get update && \
    apt-get -y install lirc

RUN apt-get update && \
    apt-get -y install python-dev 

RUN pip install --upgrade pip

RUN pip install --upgrade flask 
RUN pip install --upgrade flask-jsonpify 
RUN pip install --upgrade flask-sqlalchemy 
RUN pip install --upgrade flask-restful

RUN pip install --upgrade paho-mqtt


COPY ./bridge /bridge
# Run bridge when the container launches

CMD [ "python", "./bridge/server.py" ]



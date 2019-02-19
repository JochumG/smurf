# image build
#docker build ./  -t bridge
# slinger image werkend (check!)
#sudo docker run --restart=unless-stopped --net=host -tid bridge
#sudo docker run --restart=always --net=host -tid bridge

FROM python:latest

RUN pip install --upgrade pip	
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


RUN pip install --upgrade bottle
RUN pip install --upgrade paho-mqtt


COPY ./server.py /
# Run bridge when the container launches
CMD [ "python", "server.py" ]



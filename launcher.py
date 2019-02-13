#bron:https://www.raspberrypi.org/forums/viewtopic.php?t=197513#p1247359

#lib/systemd/systemd/iot.service

#file content
	#[Unit]
	#Description=IOT service, Bridge startup, Sub waterpomp, Deebot
	#After=multi-user.target
	#
	#[Service]
	#Type=simple
	#ExecStart=/usr/bin/python /home/pismurf/code/launcher.py
	#Restart=on-abort
	#
	#[Install]
	#WantedBy=multi-user.target

#sh commandos 
	#sudo chmod 644 /lib/systemd/system/hello.service
	#chmod +x /home/pi/hello_world.py
	#sudo systemctl daemon-reload
	#sudo systemctl enable hello.service
	#sudo systemctl start hello.service


import os

os.system("sudo python /home/pismurf/code/sub/sub_listener/water_subscriber.py & python /home/pismurf/code/sub/sub_listener/deebot_subscriber.py & python /home/pismurf/code/bridge/server.py")
print ("started 3 files")

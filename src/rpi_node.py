import threading
import time
import grovepi
import numpy as np
import paho.mqtt.client as mqtt
import sys

MAX_FRQ = 2000
SLICE_SIZE = 0.15
WINDOW_SIZE = 0.25 #seconds
lock = threading.Lock()

sound_sensor = 0
grovepi.pinMode(sound_sensor, "INPUT")


#y = []
#y_filt = []
#nyq_frq = MAX_FRQ/2


if __name__ == '__main__':
    
    client = mqtt.Client()
    client.connect(host="tcp://104.183.92.41", port=1883, keepalive=60)
    client.loop_start()


    while True:

    	with lock:
    		x = np.linspace[1:MAX_FRQ/2]
    		client.publish('data/unflitered', x)

    	pass


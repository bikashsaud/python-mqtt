import paho.mqtt.client as mqtt
from random import randrange, uniform
import time

mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("BAITADI_SENSOR")
client.connect(mqttBroker)

while True:
    randNumber = randrange(18,21)
    client.publish("TEMP_BTD", randNumber)
    print("Just published " + str(randNumber) + " to Baitadi TEMPERATURE")
    time.sleep(1)

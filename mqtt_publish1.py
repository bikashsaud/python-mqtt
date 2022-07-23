import paho.mqtt.client as mqtt
from random import randrange, uniform
import time

mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("KATHMANDU_SENSOR")
client.connect(mqttBroker)

while True:
    randNumber = uniform(20.0, 21.0)
    client.publish("TEMPERATURE_KTM", randNumber)
    print("Just published " + str(randNumber) + " to KTM TEMPERATURE")
    time.sleep(1)


import paho.mqtt.client as mqtt
import time

def on_message(client, userdata, message):
    print("Received message: ", str(message.payload.decode("utf-8")))

mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("MY_PHONE")
client.connect(mqttBroker)


client.loop_start()
while True:
    client.subscribe("TEMP_BTD")
    client.subscribe("TEMPERATURE_KTM")

    client.on_message = on_message
    time.sleep(4)
    # client.loop_forever()

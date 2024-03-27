import paho.mqtt.publish as publish
from virtual_iot_station import VirtualIoTStation 
import time
import datetime

# ThingSpeak Channel ID.
MQTT_CHANNEL_ID = "2463857"

# Hostname of ThingSpeak MQTT broker.
MQTT_HOST = "mqtt3.thingspeak.com"

# Your MQTT credentials for the device
MQTT_CLIENT_ID = "HAUVBjMLECwaMRw2BzkqJw0"
MQTT_USERNAME  = "HAUVBjMLECwaMRw2BzkqJw0"
MQTT_PASSWORD  = "78vz5w5GisMcZcS8WjjOPnlY"

TRANSPORT = "websockets"
PORT = 80

# Create the TOPIC string.
TOPIC = "channels/" + MQTT_CHANNEL_ID + "/publish"

iot_station = VirtualIoTStation()

while (True):
  temperature, humidity, co2 = iot_station.generate_sensor_values()

  # build the payload string.
  payload = "field1=" + str(temperature) + "&field2=" + str(humidity) + "&field3=" + str(co2)

  # Add logs
  print (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + " Writing Payload=", payload," to host=", MQTT_HOST, " clientID=", MQTT_CLIENT_ID)

  # attempt to publish this data to the TOPIC.
  publish.single(TOPIC, payload, hostname=MQTT_HOST, transport=TRANSPORT, port=PORT, client_id=MQTT_CLIENT_ID, auth={'username':MQTT_USERNAME,'password':MQTT_PASSWORD})

  time.sleep(5)

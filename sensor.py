import paho.mqtt.publish as mqtt_publisher
from virtual_iot_station import IOTStation
import time
import datetime

# Configuration for the MQTT channel on ThingSpeak.
CHANNEL_IDENTIFIER = "2463857"
MQTT_SERVICE_HOST = "mqtt3.thingspeak.com"

# Authentication details for the MQTT connection.
DEVICE_CLIENT_ID = "HAUVBjMLECwaMRw2BzkqJw0"
CONN_USERNAME = "HAUVBjMLECwaMRw2BzkqJw0"
CONN_PASSWORD = "78vz5w5GisMcZcS8WjjOPnlY"

# Connection method and port for MQTT.
SOCKET_TRANSPORT = "websockets"
SERVICE_PORT = 80

# MQTT topic string for data publication.
PUBLISH_CHANNEL = f"channels/{CHANNEL_IDENTIFIER}/publish"

# Initialize the simulated sensor station.
environment_station = IOTStation()

# Infinite loop to continuously send data.
while True:
    # Retrieve simulated sensor readings.
    temp_reading, humidity_reading, co2_reading = environment_station.get_sensor_data()

    # Format the data payload for MQTT publishing.
    mqtt_payload = f"field1={temp_reading}&field2={humidity_reading}&field3={co2_reading}"

    # Log the data with the current timestamp.
    current_timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    print(f"{current_timestamp} - Sending Data: {mqtt_payload} to MQTT Server: {MQTT_SERVICE_HOST}, ClientID: {DEVICE_CLIENT_ID}")

    # Send the data to the ThingSpeak channel via MQTT.
    mqtt_publisher.single(PUBLISH_CHANNEL, mqtt_payload, hostname=MQTT_SERVICE_HOST, transport=SOCKET_TRANSPORT, port=SERVICE_PORT, client_id=DEVICE_CLIENT_ID, auth={'username':CONN_USERNAME, 'password':CONN_PASSWORD})

    # Wait for 5 seconds before sending the next set of data.
    time.sleep(5)

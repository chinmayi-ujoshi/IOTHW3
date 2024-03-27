a) Build a cloud-based IoT system which collects data from a set of virtual sensors that are
deployed to collect environmental information using the MQTT protocol.
b) Display the latest sensor data values received from all the sensors of a specified environmental
station.
c) Display the sensor data values received during the last five hours from all environmental station
of a specified sensor.
Virtual Sensors:
You may build a standalone computer program using a preferred programming language, to
represent a virtual environment IoT station that periodically generates a set of random virtual
sensor values for the following sensors:
1. Temperature (Range: -50 to 50 Celsius)
2. Humidity (Range: 0 to 100%)
3. Co2 sensor (Range: 300ppm to 2000ppm
The virtual environmental Station:
Your virtual environmental station has to have a unique ID (identity) to publish the random
sensor data values on an MQTT channel.
Cloud-based IoT Backend
The MQTT is controlled by the cloud-based backend. You may implement the cloud-based
backend using one of the following technologies:
AWS IoT
ThingSpeak

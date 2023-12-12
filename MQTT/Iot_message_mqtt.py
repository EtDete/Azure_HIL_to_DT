from paho.mqtt import client as mqtt
import mqttClass
from azure.iot.device import Message
import random
import ssl
import struct

#path_to_root_cert = "C:\\Users\\etien\\OneDrive\\Bureau\\LIS\\Azure_HIL_to_DT\\certificate.txt"
device_id = "Wind_unit"
sas_token = "jw92w3o43TpsXpNGEmb1bXAsRrWvtGSedWGE5zWHYGQ="
iot_hub_name = "MicrogridHub"



#Creating an instance of MQTT Client
client = mqttClass.mqttClient(client_id=iot_hub_name)
#Setting a password and an username to the broker
#client.username_pw_set(username=iot_hub_name + ".azure-devices.net/" + device_id + "/?api-version=2021-04-12",password=sas_token)
#connecting
client.run(host=iot_hub_name + ".azure-devices.net")# port=8883, keepalive=120
#starting the loop
client.loop_start()
#Preparing the telemetry to send
message = "wind_captor : "+ random.randint(1,100)
client.send_message(payload=message,topic="devices/" + device_id + "/messages/events/")

#closing the loop
#client.loop_close()

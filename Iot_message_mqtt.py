from paho.mqtt import client as mqtt
import ssl

path_to_root_cert = "<local path to digicert.cer file>"
device_id = "Wind_unit"
sas_token = "jw92w3o43TpsXpNGEmb1bXAsRrWvtGSedWGE5zWHYGQ="
iot_hub_name = "MicrogridHub"


def on_connect(client, userdata, flags, rc):
    print("Device connected with result code: " + str(rc))


def on_disconnect(client, userdata, rc):
    print("Device disconnected with result code: " + str(rc))


def on_publish(client, userdata, mid):
    print("Device sent message")

#Creating an instance of MQTT Client
def create_client(device_id):
    client = mqtt.Client(client_id=device_id, protocol=mqtt.MQTTv311)
    return(client)

def connect_iot_hub(device_id, client,path_to_root_cert,sas_token,iot_hub_name):
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.on_publish = on_publish

    client.username_pw_set(username=iot_hub_name+".azure-devices.net/" +
                       device_id + "/?api-version=2021-04-12", password=sas_token)

    client.tls_set(ca_certs=path_to_root_cert, certfile=None, keyfile=None,
               cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)
    client.tls_insecure_set(False)

    client.connect(iot_hub_name+".azure-devices.net", port=8883)
    client.loop_forever()

def sending_message(client,data):
    client.publish("devices/"+ device_id + "/messages/events/", data, qos=1)
    print("Message sent to"+iot_hub_name)
    
def run_client(device_id,path_to_root_cert,sas_token,iot_hub_name,data):
    client = create_client(device_id)
    connect_iot_hub(device_id, client,path_to_root_cert,sas_token,iot_hub_name)
    sending_message(client,data)

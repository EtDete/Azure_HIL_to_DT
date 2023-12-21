import paho.mqtt.client as mqtt
import ssl
import time


path_to_root_cert = "C:\\Users\\etien\\OneDrive\\Documents\\Centrale\\Alternance_recherche\\LIS\\Azure_HIL_to_DT\\MQTT\\digicert.cer.txt"
device_id = "Wind_unit" #Id de l'appareil auquel on souhaite envoyer un message
sas_token = "HostName=MicrogridHub.azure-devices.net;DeviceId=Wind_unit;SharedAccessSignature=SharedAccessSignature sr=MicrogridHub.azure-devices.net%2Fdevices%2FWind_unit&sig=GVcO8hHL2AH1AyTz0mQCknShNf7vaMD72WHyaKBpB%2BU%3D&se=1703171179"
iot_hub_name = "MicrogridHub"   
topic = "devices/" + device_id + "/messages/events/" #Topic of the iot hub to send messages to

def on_log(client, userdata, level, buf):
        print("log: ",buf)

def on_disconnect(client, userdata, rc):
        if rc != 0:
            print("Unexpected disconnexion")
        else:
            print("The client was sucessfully disconnected")
            
def on_subscribe(client,userdata, mid, granted_qos):
        print('Subscribed for m' + str(mid))
        
def on_connect(client, userdata, flags, rc):
        if rc == 0: #rc contient 0 si la connexion est établie, 1 si mauvais protocole... 
            print("Connexion successful !")
        else:
            print("Connexion error with result code "+str(rc))
            
def on_message(client, userdata, message):
        print("Received message " + str(message.payload) + " on topic " + message.topic + " with QoS " + str(message.qos))

#create the client
client = mqtt.Client(client_id=device_id,clean_session=False,protocol=mqtt.MQTTv311)
#setting the callbacks
client.on_connect=on_connect
client.on_disconnect=on_disconnect
client.on_message=on_message
client.on_log=on_log
client.on_subscribe=on_subscribe
#Setting the username et password
username = iot_hub_name + ".azure-devices.net/" + device_id + "/?api-version=2021-04-12"
password = sas_token
client.username_pw_set(username=username,password=password)
#Setting the TLS
client.tls_set_context(context=None)
client.tls_set(ca_certs=path_to_root_cert, certfile=None, keyfile=None,
               cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)
client.tls_insecure_set(False)
#Connecting to the hub
client.connect(host=iot_hub_name + ".azure-devices.net",port=8883,keepalive=60)
client.subscribe(topic=topic,qos=1)
time.sleep(1)
client.loop_start()
#sending a message
client.publish(topic=topic,payload="Hello",qos=1)
client.loop_stop()

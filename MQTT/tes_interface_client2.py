import paho.mqtt.client as mqtt

test_client2 = mqtt.Client(client_id="Listenner", clean_session=True,userdata =None, protocol =mqtt.MQTTv311, transport="tcp")

def on_subscribe(client,userdata, mid, granted_qos):
    print('Subscribed for m' + str(mid))
    

def on_connect(client, userdata, flags, rc):
    if rc == 0: #rc contient 0 si la connexion est établie, 1 si mauvais protocole... 
        print("Connexion successful !")
    else:
        print("Connexion error with result code "+str(rc))
        

def on_message(client, userdata, message):
    print("Received message " + str(message.payload) + " on topic " + message.topic + " with QoS " + str(message.qos))
    # if message.topic != topic:
    #     return 1
    # else :
    #     return 0
    

def on_log(client, userdata, level, buf):
    print("log: ",buf)

def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Unexpected disconnexion")
    else:
        print("The client was sucessfully disconnected")
        
test_client2.on_connect=on_connect
test_client2.on_disconnect=on_disconnect
test_client2.on_message=on_message
test_client2.on_log=on_log
test_client2.on_subscribe=on_subscribe

test_client2.connect("mqtt.eclipseprojects.io",port=1883,keepalive = 180, bind_address = "")
test_client2.subscribe(topic="topic",qos=1)
test_client2.loop_forever()
from typing import List,NewType
import paho.mqtt.client as mqtt
import time
import appJar
import asyncio
import keyboard

global topic 
topic = "topic/important"

global list_client
list_client = []

class mqttClient(): #Classe des instances clients mqtt
    
    def __init__(self,client_id : str) -> None:
        #Le client_id doit être unique à chaque client; Mettre 0 et "" laisse le programme en générer un (si clean_session = True).
        self.client_id = client_id
        self.client = mqtt.Client(client_id=client_id, clean_session=True,userdata =None, protocol =mqtt.MQTTv311, transport="tcp")
        list_client.append(self)
    
    def __exit__(self):
        #permet de gérer les exceptions et la déconnexion propre
        self.client.disconnect()

    
    @staticmethod  
    def on_subscribe(client,userdata, mid, granted_qos):
        print('Subscribed for m' + str(mid))
        
    @staticmethod
    def on_connect(client, userdata, flags, rc):
        if rc == 0: #rc contient 0 si la connexion est établie, 1 si mauvais protocole... 
            print("Connexion successful !")
        else:
            print("Connexion error with result code "+str(rc))
            
    @staticmethod
    def on_message(client, userdata, message):
        print("Received message " + str(message.payload) + " on topic " + message.topic + " with QoS " + str(message.qos))
        # if message.topic != topic:
        #     return 1
        # else :
        #     return 0
        
    @staticmethod
    def on_log(client, userdata, level, buf):
        print("log: ",buf)
    
    @staticmethod
    def on_disconnect(client, userdata, rc):
        if rc != 0:
            print("Unexpected disconnexion")
        else:
            print("The client was sucessfully disconnected")

    async def run(self,topic :str):
        
        self.client.on_connect = self.on_connect
        #self.client.on_subscribe = self.on_subscribe
        self.client.on_message = self.on_message
        #self.client.on_log = self.on_log
        self.client.on_disconnect = self.on_disconnect
        
        self.client.will_set(topic=topic,payload="The client was unexpectedly disconnected !",qos=0,retain=False)
        self.client.connect_async("mqtt.eclipseprojects.io",port=1883,keepalive = 180, bind_address = "") #bind_address permet de bind le client à une interface si plusieurs interfaces existent
        print("Is the client connected ? : ", self.client.is_connected())

        #disc = self.client.disconnect() #renvoie 0 si la déconnexion c'est bien passée
        # if disc != 0:
        #     print("Unexpected error on disconnecting this client !")
        # self.client.subscribe(topic = topic, qos = 0)
        await self.loop_start()
        
    def send_message(self,message,topic):
        self.client.publish(topic,payload = message, qos=0)

    async def receive_message(self,topic):
        self.client.subscribe(topic,qos=0)

    async def loop_start(self):
        #Définir ce qu'il y a faire pendant le temps de connexion
        def callback():
            message = input(f"Type the message to send to the topic {topic}")
            self.send_message(message=message,topic=topic)
        self.client.loop_start()
        await self.receive_message(topic=topic)
        print("Type t in cmd to send a message")
        timeout = 60
        while timeout > 0:
            #print("Is the client connected ? : ", self.client.is_connected())
            await self.receive_message(topic=topic)
            keyboard.add_hotkey("space",callback=callback)
                # message = input(f"Type the message to send to the topic {topic}")
                # await self.send_message(message=message,topic=topic)
            timeout-=1
            #print(timeout)
            await asyncio.sleep(1)
        self.client.loop_stop()
        self.client.disconnect()


        
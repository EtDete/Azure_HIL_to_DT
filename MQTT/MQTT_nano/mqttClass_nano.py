import paho.mqtt.client as mqtt

data = () #data received on general
data_j1 = () #data received from the jetson1
data_j2 = () #data received from the jetson2
data_j3 = () #data received from the jetson3

global topic 
topic = 'topic/optimisation/variable'

class mqttClient(): #Classe des instances clients mqtt
    
    def __init__(self,client_id : str) -> None:
        #Le client_id doit être unique à chaque client; Mettre 0 et "" laisse le programme en générer un (si clean_session = True).
        self.client_id = client_id
        self.client = mqtt.Client(client_id=client_id, clean_session=True,userdata =None, protocol =mqtt.MQTTv311, transport="tcp")
    
    @staticmethod  
    def on_subscribe(client,userdata, mid, granted_qos):
        print('Subscribed for m' + str(mid))
        
    @staticmethod
    def on_connect(client, userdata, flags, rc):
        if rc == 0: #rc contient 0 si la connexion est établie, 1 si mauvais protocole... 
            print("Connexion successful !")
            client.subscribe(topic,qos=1)
        else:
            print("Connexion error with result code "+str(rc))
            
    @staticmethod
    def on_message(client, userdata, message):
        #print("Message received")
        global data
        global data_j1,data_j2,data_j3
        data = eval(message.payload) 
        if data[0] == 'Jetson1':
            data_j1 = data
        elif data[0] == 'Jetson2':
            data_j2 = data
        else:
            data_j3 = data
            
    @staticmethod
    def on_log(client, userdata, level, buf):
        print("log: ",buf)
    
    @staticmethod
    def on_disconnect(client, userdata, rc):
        if rc != 0:
            print("Unexpected disconnexion")
        else:
            print("The client was sucessfully disconnected")

    def run(self,topic :str):
        
        self.client.on_connect = self.on_connect
        # self.client.on_subscribe = self.on_subscribe
        self.client.on_message = self.on_message
        # self.client.on_log = self.on_log
        self.client.on_disconnect = self.on_disconnect
        
        self.client.will_set(topic=topic,payload="The client was unexpectedly disconnected !",qos=0,retain=False)
        self.client.connect("mqtt.eclipseprojects.io",port=1883,keepalive = 180, bind_address = "") #bind_address permet de bind le client à une interface si plusieurs interfaces existent

        
    def send_message(self,message,topic):
        self.client.publish(topic,payload = message, qos=1)




        
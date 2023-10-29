import paho.mqtt.client as mqtt

class mqttClient():
    def __init__(self,client_id):
        self.client_id = client_id
        self.client = mqtt.Client(client_id=client_id, clean_session=True,userdata =None, protocol =mqtt.MQTTv311, transport="tcp")
        
    def on_subscribe(client, userdata, mid, granted_qos):
        print('Subscribed for m' + str(mid))

    def on_connect(client, userdata, flags, rc):
        print("Connected with result code "+str(rc))

    def on_message(client, userdata, message):
        print("Received message '" + str(message.payload) + "' on topic '" + message.topic + "' with QoS " + str(message.qos))

    def on_log(client, userdata, level, buf):
        print("log: ",buf)

    def run(self):
        self.client.connect("mqtt.eclipseprojects.io",port=1883,keepalive = 60, bind_address = "")
        self.client.subscribe(topic = topic, qos = 0)
        self.client.loop()
        
    def send_message(self,message,topic):
        self.client.publish(topic,payload = message, qos=0)

    def receive_message(self,topic):
        self.client.subscribre(topic,qos=0)
        self.client.loop()      

        
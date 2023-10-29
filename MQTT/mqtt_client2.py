# import paho.mqtt.client as mqtt
# from paho.mqtt.properties import Properties
# from paho.mqtt.packettypes import PacketTypes 



# def on_subscribe(client, userdata, mid, granted_qos):
#     print('Subscribed for m' + str(mid))

# def on_connect(client, userdata, flags, rc):
#     print("Connected with result code "+str(rc))

# def on_message(client, userdata, message):
#     print("Received message '" + str(message.payload) + "' on topic '" + message.topic + "' with QoS " + str(message.qos))

# def on_log(client, userdata, level, buf):
#     print("log: ",buf)

# properties=Properties(PacketTypes.PUBLISH)
# properties.MessageExpiryInterval=30 # in seconds
# topic = 'topic\important'
# client = mqtt.Client(client_id="test_client2", clean_session=True,userdata =None, protocol =mqtt.MQTTv311, transport="tcp")
# client.on_connect = on_connect
# client.on_subscribe = on_subscribe
# client.on_message = on_message
# client.on_log = on_log
# client.connect("mqtt.eclipseprojects.io",port=1883,keepalive = 60, bind_address = "")

# client.subscribe(topic = topic, qos = 0)
# print(f"Receving data from topic {topic}")
# client.loop_forever()
import mqttClass

client = mqttClient("test_client1")
client.run()
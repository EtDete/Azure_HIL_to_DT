import mqttClass

client = mqttClass.mqttClient("test_client3")
client.run(topic='topic/important')
client.receive_message(topic='topic/important')
client.client.loop_forever()
import mqttClass

client = mqttClass.mqttClient("test_client2")
client.run(topic='topic/important')
client.receive_message(topic='topic/important')
client.client.loop_forever()
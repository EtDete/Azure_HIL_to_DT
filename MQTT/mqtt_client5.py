import mqttClass 

client = mqttClass.mqttClient(client_id="test_client1")
client.run(topic='topic/important')
client.send_message(topic='topic/important',message="SALUT C'EST MOI !")
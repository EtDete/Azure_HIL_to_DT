import asyncio
import mqttClass 

client = mqttClass.mqttClient(client_id="test_client1")
asyncio.run(client.run(topic='topic/important'))


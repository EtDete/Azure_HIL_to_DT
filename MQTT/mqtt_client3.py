import mqttClass
import asyncio

client = mqttClass.mqttClient("test_client2")
# client.run(topic='topic/important')
# client.receive_message(topic='topic/important')
# client.client.loop_forever()
asyncio.run(client.run(topic='topic/important'))




import mqttClass
import interface

test_client = mqttClass.mqttClient(client_id="Test_client_mqtt")

test_interface = interface.mqtt_interface(id="Test_Interface",mqtt_client=test_client)

test_interface.launch()

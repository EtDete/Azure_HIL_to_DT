import modbus
import Iot_message_mqtt
import parameter as param
from time import sleep

#f = open("Valeurs.txt","+a")

path_to_root_cert = "<local path to digicert.cer file>"
device_id = "Wind_unit"
sas_token = "jw92w3o43TpsXpNGEmb1bXAsRrWvtGSedWGE5zWHYGQ="
iot_hub_name = "MicrogridHub"
data = 24
Iot_message_mqtt.run_client(device_id,path_to_root_cert,sas_token,iot_hub_name,data)

# client = modbus.modbus_connexion(param.ip_addr,param.port)
# data_0 = 10  #Variable representing the previous data received
# while True :
#     try:
#         data = modbus.run_modbu_task(param.request_addr)
#         f.write(str(data))
#         if data != data_0 :
#             data_0 = data
#             Iot_message_mqtt.run_client(device_id,path_to_root_cert,sas_token,iot_hub_name,data)
#         sleep(2)
        
#     except Exception:
#         client.close
import modbus
#import Iot_message_mqtt
import extracting_data
import parameter as param

data = modbus.run_modbu_task(param.ip_addr,param.port)




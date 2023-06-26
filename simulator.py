import random
import modbus_jetson
import time
#Exemple de génération de données

data = 0
while True:
    try:
        data = random.randrange(0,100,1)
        print(data)
        modbus_jetson.write_to_holding_register(100,data)
        time.sleep(5)
    except:
        break

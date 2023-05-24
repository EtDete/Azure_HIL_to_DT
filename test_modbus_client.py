import modbus
import parameter as param

client = modbus.modbus_connexion(param.ip_addr,param.port)
try :
    data = modbus.run_modbu_task(param.request_addr)
    
except:
    client.close
    print("Erreur lors de l'éxecution de la requête")

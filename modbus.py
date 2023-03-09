# Etablir la connexion Modbus entre le typhoon HIL et l'ordinateur

from pyModbusTCP.server import ModbusServer, DataBank
from time import sleep

#create an instance of modbus server
ip_addr = "192.168.1.233" #ipv4 address of the server
port = 12345 # port number of the server
serv = ModbusServer(ip_addr,port,no_block=True)


try:
    print("Start server...")
    serv.start()
    print("ONLINE")
    while True:
        print("")
except :
    print("Server shutting down")
    serv.close()
    print("Server offline")
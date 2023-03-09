# Etablir la connexion Modbus entre le typhoon HIL et l'ordinateur

from pymodbus.client.tcp import ModbusTcpClient
from time import sleep

#create an instance of modbus server
ip_addr = "192.168.1.233" #ipv4 address of the server
port = 502 # port number of the server
client = ModbusTcpClient(ip_addr,port)


try:
    print("Start connecting...")
    client.connect()
    print("Connected")
    while True:
        print("Starting the request")
        a = client.read_holding_registers(addresse=1248,count=1,unit=2)
        print(a)
        sleep(1)
except :
    print("Error")
    client.close()
    print("client disconnected")
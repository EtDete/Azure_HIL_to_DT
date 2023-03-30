# Etablir la connexion Modbus entre le typhoon HIL et l'ordinateur

from pymodbus.client.tcp import ModbusTcpClient
from time import sleep
import socket

#create an instance of modbus server
ip_addr = "192.168.1.233" #ipv4 address of the server
port = 502 # port number of the server
client = ModbusTcpClient(ip_addr,port)


try:
    #s = socket.socket(ip_addr)
    #s.bind("192.168.1.2")
    #s.connect()
    print("Start connecting...")
    client.connect()
    print("Connected")
    print(client.report_slave_id())
    while True:
        print("Starting the request")
        #count= the number of registers to read
        #unit= the slave unit this request is targeting
        #address= the starting address to read from
        read = client.read_holding_registers(addresse=122,count=1,unit=1)
        #UNEXPECTED ISSUE HERE WHEN READING
        data=read.registers[0] #reading the registers 30122
        print(data)
        sleep(1)
    # s.close
except :
    print("Error")
    client.close()
    print("client disconnected")
# Etablir la connexion Modbus entre le typhoon HIL et l'ordinateur

from pymodbus.client.tcp import ModbusTcpClient
from time import sleep

def setup_client(ip_addr,port):
    #create an instance of modbus server
    client = ModbusTcpClient(ip_addr,port)
    return(client)

def setup_connection(client):
    """Opening the connection between the client and the server

    Args:
        client (ModbusTcpClient): this virtually represent the device we are connecting to. It is define with an ip
    """
    try:
        #s = socket.socket(ip_addr)
        #s.bind("192.168.1.2")
        #s.connect()
        print("Start connecting...")
        client.connect()
        print("Connected")
    except :
        print("Error")
        client.close()
        print("client disconnected")

def run_modbu_task(ip_addr,port):
    """This function setup a modbus connection between a master and a client (device) and read a holding register at the address 40122

    Args:
        ip_addr (str): ipv4 address of the server
        port (int): port number of the server, usually 502
    """
    client = setup_client(ip_addr,port)
    setup_connection(client)
    print("Starting the request")
    #count= the number of registers to read
    #unit= the slave unit this request is targeting
    #address= the starting address to read from
    read = client.read_holding_registers(address=122,count=1)
    #UNEXPECTED ISSUE HERE WHEN READING
    data=read.registers[0] #reading the registers 30122
    print(data)
    client.close()
    #terminate the connection
    return data
# Etablir la connexion Modbus entre le typhoon HIL et l'ordinateur

from pymodbus.client.tcp import ModbusTcpClient
from time import sleep
import socket
import parameter as param
def setup_client(ip_addr,port):
    #create an instance of modbus server
    client = ModbusTcpClient(ip_addr,port)
    return(client)

def setup_socket():
    """Permet de setup la connexion entre le HIL et le PC avec un socket
    """
    try:
        print("Creating the socket")
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        print("Bind to the port")
        s.bind((param.ip_addr,param.port))
        print("Server created")
        s.listen(1)
        conn, addr = s.accept()
        print("connection accepted")
    except socket.timeout as e:
        print(e)
        print("Timeout: unable to bind to IP:"+param.ip_addr+'port:'+param.port+".\n")
        return
    except socket.error as e:
        (errno,msg_str)= e.args
        print(msg_str)
        print("Timeout: unable to bind to IP:"+param.ip_addr+'port:'+param.port+".\n")
        return
       
def setup_connection_client(client):
    """Opening the connection between the client and the server

    Args:
        client (ModbusTcpClient): this virtually represent the device we are connecting to. It is define with an ip
    """
    try:
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
    #setup_socket()
    setup_connection_client(client)
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
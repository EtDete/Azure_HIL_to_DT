# Etablir la connexion Modbus entre le typhoon HIL et la Jetson Nano
from pymodbus.exceptions import ModbusException
from pymodbus.pdu import ExceptionResponse
from pymodbus.client.tcp import ModbusTcpClient


def setup_client(ip_addr,port):
    #create an instance of modbus client
    client = ModbusTcpClient(ip_addr,port)
    return(client)

       
def setup_connection_client(client):
    """Opening the connection between the client and the server

    Args:
        client (ModbusTcpClient): this virtually represent the device we are connecting to. It is define with an ip adress
    """
    try:
        print("Start connecting...")
        client.connect()
        print("Connected")
    except :
        print("Error")
        client.close()
        print("client disconnected")
        
def modbus_connexion(ip_addr,port):
    client = setup_client(ip_addr,port)
    setup_connection_client(client)
    return(client)

def run_modbu_task(client,request_addr):
    """This function setup a modbus connection between a master and a client (device) and read a holding register at a given address

    Args:
        ip_addr (str): ipv4 address of the client
        port (int): port number of the client, usually 502
    """
    print("Starting the request")
    #count= the number of registers to read
    #unit= the slave unit this request is targeting
    #address= the starting address to read from
    # read = client.read_holding_registers(address=request_addr,count=1,slave=0)
    # data = read.registers[0] #reading the registers with the request_addr addresse 
    # client.close()
    #terminate the connection
    try:
        rr = client.read_holding_registers(address=request_addr,count=1,slave=0)
        data = rr.registers[0]
    except ModbusException as exc:
        print(f"Received ModbusException({exc}) from library")
        client.close()
        return
    if rr.isError():
        print(f"Received Modbus library error({rr})")
        client.close()
        return
    if isinstance(rr, ExceptionResponse):
        print(f"Received Modbus library exception ({rr})")
        # THIS IS NOT A PYTHON EXCEPTION, but a valid modbus message
        client.close()
    return data
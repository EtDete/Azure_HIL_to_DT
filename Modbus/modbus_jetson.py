# from pymodbus.server import ModbusTcpServer, StartTcpServer
from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
from pymodbus.server import StartAsyncTcpServer
import asyncio
import random

addr = str(input("Quelle est l'adresse du serveur ?"))
port = int(input("Sur quel port doit-il être connecté ?"))

# Créer un contexte de serveur Modbus
store = ModbusSlaveContext(
    di=ModbusSequentialDataBlock(0, [0]*100),  # Entrées discrètes   #(address,list of values)
    co=ModbusSequentialDataBlock(0, [0]*100),  # Sorties discrètes
    hr=ModbusSequentialDataBlock(0, [0]*100),  # Registres de maintien
    ir=ModbusSequentialDataBlock(0, [0]*100))  # Registres d'entrée

context = ModbusServerContext(slaves=store, single=True)

async def updating_task(context):
    """Update the value of an Holding register at an fixed address
    """
    fc_as_hex = 3
    slave_id = 0
    address = 50
    values = random.randrange(1,100)
    while True:
        context[slave_id].setValues(fc_as_hex, address, [values])
        await asyncio.sleep(1)
    

async def run_sync_server(context): 
    """Run server."""
    asyncio.create_task(updating_task(context))
    await StartAsyncTcpServer(context,address=(addr,port))
    

asyncio.run(run_sync_server(context))

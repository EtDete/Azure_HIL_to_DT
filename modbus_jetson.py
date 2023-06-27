# from pymodbus.server import ModbusTcpServer, StartTcpServer
from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
from pymodbus.server import StartAsyncTcpServer
import asyncio
import random
import logging
# from setup_server import setup_server
# args = setup_server(description=None, context=None, cmdline=None)

# Créer un contexte de serveur Modbus
store = ModbusSlaveContext(
    di=ModbusSequentialDataBlock(0, [0]*100),  # Entrées discrètes   #(address,list of values)
    co=ModbusSequentialDataBlock(0, [0]*100),  # Sorties discrètes
    hr=ModbusSequentialDataBlock(0, [0]*100),  # Registres de maintien
    ir=ModbusSequentialDataBlock(0, [0]*100))  # Registres d'entrée

_logger = logging.getLogger()

context = ModbusServerContext(slaves=store, single=True)

async def updating_task(context):
    """Run every so often and update live values of the context.

    It should be noted that there is a race condition for the update.
    """
    fc_as_hex = 3
    slave_id = 0x00
    address = 0x42
    values = context[slave_id].getValues(fc_as_hex, address, count=1)
    values = random.randrange(1,100)  # increment by 1.
    txt = f"new values: {str(values)}"
    _logger.debug(txt)
    context[slave_id].setValues(fc_as_hex, address, [values])
    await asyncio.sleep(1)
    
# Fonction pour écrire dans un registre de maintien
def write_to_holding_register(address, value):
    context[0x00].setValues(3, address, [value])

# StartTcpServer(context,identity,address=("192.168.1.129",502))
async def run_sync_server(context): 
    """Run server."""
    try:
        # Démarrer le serveur Modbus TCP
        server = await StartAsyncTcpServer(context,address=("147.94.73.157",502))
        print("ok")
    except:
        print("Erreur dans le lancement du serveur")

asyncio.run(run_sync_server(context))
asyncio.run(updating_task(context))
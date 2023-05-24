# from pymodbus.server import ModbusTcpServer, StartTcpServer
from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
from pymodbus.server import StartTcpServer,StartAsyncTcpServer
# from setup_server import setup_server
import asyncio

# args = setup_server(description=None, context=None, cmdline=None)

# Créer un contexte de serveur Modbus
store = ModbusSlaveContext(
    di=ModbusSequentialDataBlock(0, [0]*100),  # Entrées discrètes   #(address,list of values)
    co=ModbusSequentialDataBlock(0, [0]*100),  # Sorties discrètes
    hr=ModbusSequentialDataBlock(0, [0]*100),  # Registres de maintien
    ir=ModbusSequentialDataBlock(0, [0]*100))  # Registres d'entrée

context = ModbusServerContext(slaves=store, single=True)

# Fonction pour écrire dans un registre de maintien
def write_to_holding_register(address, value):
    context[0x00].setValues(3, address, [value])

# StartTcpServer(context,identity,address=("192.168.1.129",502))
async def run_sync_server(context):
    """Run server."""
    try:
        # Démarrer le serveur Modbus TCP
        server = await StartAsyncTcpServer(context,address=("147.94.73.138",502))
        # server.serve_forever()
        print("ok")
    except:
        print("Erreur dans le lancement du serveur")

asyncio.run(run_sync_server(context))
# Écrire dans un registre de maintien
write_to_holding_register(0, 42)
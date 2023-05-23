from pymodbus.server import ModbusTcpServer, StartTcpServer
from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext,ModbusSlaveContextBuilder
import setup_serv as setup 

# Créer un contexte de serveur Modbus
store = ModbusSlaveContext(
    di=ModbusSequentialDataBlock(0, [0]*100),  # Entrées discrètes
    co=ModbusSequentialDataBlock(0, [0]*100),  # Sorties discrètes
    hr=ModbusSequentialDataBlock(0, [0]*100),  # Registres de maintien
    ir=ModbusSequentialDataBlock(0, [0]*100))  # Registres d'entrée

context = ModbusServerContext(slaves=store, single=True)

# Fonction pour écrire dans un registre de maintien
def write_to_holding_register(address, value):
    context[0x00].setValues(3, address, [value])

# Écrire dans un registre de maintien
# write_to_holding_register(0, 42)


identity = None
StartTcpServer(context,identity,address=("192.168.1.129",502))
def run_sync_server(context,identity,address,framer):
    """Run server."""
    try:
        # Démarrer le serveur Modbus TCP
        server = StartTcpServer(context)
    except:
        # Arrêter le serveur Modbus TCP
        server.server_close()
    # server = StartTcpServer(
    #         context,  # Data storage
    #         identity,  # server identify
    #         # TBD host=
    #         # TBD port=
    #         address,  # listen address
    #         # custom_functions=[],  # allow custom handling
    #         framer,  # The framer strategy to use
    #         # TBD handler=None,  # handler for each session
    #         allow_reuse_address=True,  # allow the reuse of an address
    #         # ignore_missing_slaves=True,  # ignore request to a missing slave
    #         # broadcast_enable=False,  # treat slave_id 0 as broadcast address,
    #         # timeout=1,  # waiting time for request to complete
    #         # TBD strict=True,  # use strict timing, t1.5 for Modbus RTU
    #         # defer_start=False,  # Only define server do not activate
    #     )


 
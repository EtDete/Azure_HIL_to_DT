from pymodbus.server import ModbusTcpServer, StartTcpServer



server = ModbusTcpServer()
server.serve_forever()

def run_sync_server(context,identity,address,framer):
    """Run server."""
    server = StartTcpServer(
            context,  # Data storage
            identity,  # server identify
            # TBD host=
            # TBD port=
            address,  # listen address
            # custom_functions=[],  # allow custom handling
            framer,  # The framer strategy to use
            # TBD handler=None,  # handler for each session
            allow_reuse_address=True,  # allow the reuse of an address
            # ignore_missing_slaves=True,  # ignore request to a missing slave
            # broadcast_enable=False,  # treat slave_id 0 as broadcast address,
            # timeout=1,  # waiting time for request to complete
            # TBD strict=True,  # use strict timing, t1.5 for Modbus RTU
            # defer_start=False,  # Only define server do not activate
        )
    return server

#Créer la liste des adresses pour lire

#Créer l'identité du serveur

# 
import asyncio
import logging
import os

from helper import get_commandline
from pymodbus import __version__ as pymodbus_version
from pymodbus.datastore import (
    ModbusSequentialDataBlock,
    ModbusServerContext,
    ModbusSlaveContext,
    ModbusSparseDataBlock,
)
from pymodbus.device import ModbusDeviceIdentification

# --------------------------------------------------------------------------- #
# import the various client implementations
# --------------------------------------------------------------------------- #
from pymodbus.server import (
    StartAsyncSerialServer,
    StartAsyncTcpServer,
    StartAsyncTlsServer,
    StartAsyncUdpServer,
)


_logger = logging.getLogger()


def setup_server(description=None, context=None, cmdline=None):
    """Run server setup."""
    args = get_commandline(server=True, description=description, cmdline=cmdline)
    if context:
        args.context = context
    if not args.context:
        _logger.info("### Create datastore")
        # The datastores only respond to the addresses that are initialized
        # If you initialize a DataBlock to addresses of 0x00 to 0xFF, a request to
        # 0x100 will respond with an invalid address exception.
        # This is because many devices exhibit this kind of behavior (but not all)
        if args.store == "sequential":
            # Continuing, use a sequential block without gaps.
            datablock = ModbusSequentialDataBlock(0x00, [17] * 100)
        elif args.store == "sparse":
            # Continuing, or use a sparse DataBlock which can have gaps
            datablock = ModbusSparseDataBlock({0x00: 0, 0x05: 1})
        elif args.store == "factory":
            # Alternately, use the factory methods to initialize the DataBlocks
            # or simply do not pass them to have them initialized to 0x00 on the
            # full address range::
            datablock = ModbusSequentialDataBlock.create()

        if args.slaves:
            # The server then makes use of a server context that allows the server
            # to respond with different slave contexts for different slave ids.
            # By default it will return the same context for every slave id supplied
            # (broadcast mode).
            # However, this can be overloaded by setting the single flag to False and
            # then supplying a dictionary of slave id to context mapping::
            #
            # The slave context can also be initialized in zero_mode which means
            # that a request to address(0-7) will map to the address (0-7).
            # The default is False which is based on section 4.4 of the
            # specification, so address(0-7) will map to (1-8)::
            context = {
                0x01: ModbusSlaveContext(
                    di=datablock,
                    co=datablock,
                    hr=datablock,
                    ir=datablock,
                ),
                0x02: ModbusSlaveContext(
                    di=datablock,
                    co=datablock,
                    hr=datablock,
                    ir=datablock,
                ),
                0x03: ModbusSlaveContext(
                    di=datablock,
                    co=datablock,
                    hr=datablock,
                    ir=datablock,
                    zero_mode=True,
                ),
            }
            single = False
        else:
            context = ModbusSlaveContext(
                di=datablock, co=datablock, hr=datablock, ir=datablock
            )
            single = True

        # Build data storage
        args.context = ModbusServerContext(slaves=context, single=single)

    # ----------------------------------------------------------------------- #
    # initialize the server information
    # ----------------------------------------------------------------------- #
    # If you don't set this or any fields, they are defaulted to empty strings.
    # ----------------------------------------------------------------------- #
    args.identity = ModbusDeviceIdentification(
        info_name={
            "VendorName": "Pymodbus",
            "ProductCode": "PM",
            "VendorUrl": "https://github.com/pymodbus-dev/pymodbus/",
            "ProductName": "Pymodbus Server",
            "ModelName": "Pymodbus Server",
            "MajorMinorRevision": pymodbus_version,
        }
    )
    return args
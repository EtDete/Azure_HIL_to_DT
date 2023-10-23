import asyncio
import uuid
from azure.iot.device.aio import IoTHubDeviceClient
from azure.iot.device import Message

#CONNECTION_STRING = os.getenv("IOTHUB_DEVICE_CONNECTION_STRING")
TOTAL_MESSAGES_SENT = 0

messages_to_send = 10

async def main():
    global TOTAL_MESSAGES_SENT
    print("Starting telemetry sample")
    print("Press Ctrl-C to exit")
    try:
        global TOTAL_MESSAGES_SENT
        print("Connecting to IoT Hub...")
        Iothub = IoTHubDeviceClient.create_from_sastoken("HostName=MicrogridHub.azure-devices.net;DeviceId=Wind_unit;SharedAccessSignature=SharedAccessSignature sr=MicrogridHub.azure-devices.net%2Fdevices%2FWind_unit&sig=bNTtkKIR%2B%2FrMEA6hChTGHxnEgRGGzmMRGy7n24oB7ms%3D&se=1688132881")
        Iothub.connect()
        async def send_test_message(i):
            print("sending message #" + str(i))
            msg = Message("test wind speed " + str(i))
            msg.message_id = uuid.uuid4()
            msg.correlation_id = "correlation-1234"
            msg.custom_properties["tornado-warning"] = "yes"
            msg.content_encoding = "utf-8"
            msg.content_type = "application/json"
            await Iothub.send_message(msg)
            print("done sending message #" + str(i))

    # send `messages_to_send` messages in parallel
        await asyncio.gather(*[send_test_message(i) for i in range(1, messages_to_send + 1)])

    # Finally, shut down the client
        await Iothub.shutdown()
    except ValueError as e:
        # Connection has been lost.
        print("Dropped connection. Exiting",e)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        # Exit application because user indicated they wish to exit.
        # This will have cancelled `main()` implicitly.
        print("User initiated exit. Exiting")
    finally:
        print("Sent {} messages in total".format(TOTAL_MESSAGES_SENT))
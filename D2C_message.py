import asyncio
import random
import uuid

# Using the Python Device SDK for IoT Hub:
#   https://github.com/Azure/azure-iot-sdk-python
#   Run 'pip install azure-iot-device' to install the required libraries for this application
#   Note: Requires Python 3.6+

# The sample connects to a device-specific MQTT endpoint on your IoT Hub.
from azure.iot.device.aio import IoTHubDeviceClient
from azure.iot.device import Message

# The device connection string to authenticate the device with your IoT hub.
CONNECTION_STRING = "HostName=MicrogridHub.azure-devices.net;DeviceId=Wind_unit;SharedAccessKey=jw92w3o43TpsXpNGEmb1bXAsRrWvtGSedWGE5zWHYGQ="

MESSAGE_TIMEOUT = 10000

# Define the JSON message to send to IoT Hub.
WIND_SPEED = 20.0
MSG_TXT = "{\"wind_speed\": %.2f}"


async def main():
    try:
        client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
        await client.connect()

        print("IoT Hub device sending periodic messages, press Ctrl-C to exit")

        while True:
            # Build the message with simulated telemetry values.
            wind_speed = WIND_SPEED + (random.random() * 15)
            msg_txt_formatted = MSG_TXT % (wind_speed)
            message = Message(msg_txt_formatted)

            # Add standard message properties
            message.message_id = uuid.uuid4()
            message.content_encoding = "utf-8"
            message.content_type = "application/json"
            
            # Send the message.
            print("Sending message: %s" % message.data)
            try:
                await client.send_message(message)
            except Exception as ex:
                print("Error sending message from device: {}".format(ex))
            await asyncio.sleep(1000)

    except Exception as iothub_error:
        print("Unexpected error %s from IoTHub" % iothub_error)
        return
    except asyncio.CancelledError:
        await client.shutdown()
        print('Shutting down device client')

if __name__ == '__main__':
    print("IoT Hub simulated device")
    print("Press Ctrl-C to exit")
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Keyboard Interrupt - sample stopped')
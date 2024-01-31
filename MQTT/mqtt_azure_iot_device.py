import sys
import time
from azure.iot.device import IoTHubDeviceClient, Message

# Remplacez les valeurs suivantes par les vôtres
CONNECTION_STRING = "HostName=MicrogridHub.azure-devices.net;DeviceId=Wind_unit;SharedAccessKey=jw92w3o43TpsXpNGEmb1bXAsRrWvtGSedWGE5zWHYGQ="
MESSAGE = "Hello from Azure IoT!"

def iothub_client_init():
    # Créer une instance du client IoT Hub
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
    return client

def send_message(client, message):
    try:
        # Créer un objet de message avec les données à envoyer
        message = Message(message)

        # Ajouter des propriétés au message si nécessaire
        message.custom_properties["Propriete1"] = "Valeur1"
        message.custom_properties["Propriete2"] = "Valeur2"

        print(f"Envoi du message: {message}")

        # Envoyer le message au hub IoT
        client.send_message(message)

        print("Message envoyé avec succès!")

    except Exception as ex:
        print("Erreur lors de l'envoi du message:", ex)

def main():
    try:
        print("Initialisation du client IoT Hub...")
        client = iothub_client_init()

        print("Connexion au hub IoT...")
        client.connect()

        print("Envoi du message au hub IoT...")
        send_message(client, MESSAGE)

        print("Attente pendant 5 secondes...")
        time.sleep(5)

        print("Déconnexion du hub IoT...")
        client.disconnect()

    except Exception as ex:
        print("Erreur:", ex)
        sys.exit(1)

if __name__ == "__main__":
    main()

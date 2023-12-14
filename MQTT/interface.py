import mqttClass
import appJar

class mqtt_interface():
    
    def __init__(self,id :str, mqtt_client : mqttClass.mqttClient) -> None:
        #id : unique identifiant d'une interface
        #mqtt_client : le client mqtt auquel est lié l'interface
        self.__app = appJar.gui("Client MQTT")
        self.id = id
        self.mqtt_client = mqtt_client
        
    
    def press(self,button):
        if button == "Connect":
            self.subscribe()
        elif button == "Disconnect":
            self.mqtt_client.client.disconnect()
            
    def construct(self):
        with self.__app as app:
            app.addLabel("en-tête", "MQTT CLIENT",app.getRow(),0,2)
            app.addLabel("en-tête_2","Tableau de bord",app.getRow(),0,2)
            app.addButton(title="Connect",func=self.press)
            app.addButton(title="Disconnect",func=self.press)
    
                
    def subscribe(self):
        self.__app.stringBox(title="Subscribe to a topic", message="Write the name of the topic to subscribe", parent=None)
        self.__app.startSubWindow("MQTT Client---Chat")
        self.__app.addMessage(title="Tchat_entry",text="Bienvenue sur le Tchat MQTT !")
        
    
        

    def launch(self):
        self.construct()
        self.__app.go()

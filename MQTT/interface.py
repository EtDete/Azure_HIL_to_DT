from unittest import TestCase
import mqttClass
import appJar

topic = ""
text = ""
class mqtt_interface():
    
    def __init__(self,id :str, mqtt_client : mqttClass.mqttClient) -> None:
        #id : unique identifiant d'une interface
        #mqtt_client : le client mqtt auquel est lié l'interface
        self.__app = appJar.gui("Client MQTT")
        self.id = id
        self.mqtt_client = mqtt_client
        
    def press(self,button):
        if button == "Connect":
            self.mqtt_client.run()
            self.mqtt_client.client.loop_start()
            self.subscribe()
        elif button == "Disconnect":
            self.mqtt_client.client.loop_stop()
            self.mqtt_client.client.disconnect()
            self.__app.infoBox(title="Disconnection",message="The client was successfully disconnected")
            self.__app.stop()
            
    def construct(self):
        with self.__app as app:
            app.addLabel("en-tête", "MQTT CLIENT",app.getRow(),0,2)
            app.addLabel("en-tête_2","Tableau de bord",app.getRow(),0,2)
            app.addButton(title="Connect",func=self.press)
            app.addButton(title="Disconnect",func=self.press)
    
                
    def subscribe(self):
        global topic
        topic  = self.__app.stringBox(title="Subscribe to a topic", message="Write the name of the topic to subscribe", parent=None)
        self.mqtt_client.receive_message(topic=topic)
        sub_window = self.__app.startSubWindow("MQTT Client---Chat")
        sub_window.show()
        self.__app.addEntry(title="Tchat")
        # self.__app.setEntry("Tchat",)
        self.__app.addButton(title="Send",func=self.tchat)
        self.__app.addMessage(title="Message_sent",text=text)
        #sub_window.addMessage(title="Tchat_entry",text="Bienvenue sur le Tchat MQTT !")
        #while self.__app.getButton(name="Disconnect_tchat"):
        self.__app.addButton(title="Receive",func=self.receive)
          
        self.__app.stopContainer()
        
    def receive(self,btn):
        if btn == "Receive":
            #TODO Regler le problème de réception des messages
            text = text + " Received : " + str(mqttClass.data)
            self.__app.setMessage(title="Message_sent",text=text)    
       
    def tchat(self,btn):
        if btn == "Send":
            global text
            message = str(self.__app.getEntry("Tchat"))
            text = text +" Sent :  "+ message
            self.__app.setMessage(title="Message_sent",text=text)
            self.mqtt_client.send_message(message,topic=topic)
            #self.__app.infoBox("Message_success","The message was sucessefully sent")
        
      

    def launch(self):
        self.construct()
        self.__app.go()
        

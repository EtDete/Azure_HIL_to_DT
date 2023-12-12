from typing import Any
import mqttClass
import appJar

class mqtt_interface():
    
    def __init__(self) -> None:
        __app = appJar.gui("Client MQTT")
    
    def __getattribute__(self) -> Any:
        #return self.__app
        pass
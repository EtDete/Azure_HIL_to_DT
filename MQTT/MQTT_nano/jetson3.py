import mqttClass_nano
import random
import time

client = mqttClass_nano.mqttClient(client_id="jetson3")
client.run(topic='topic/optimisation/variable')
client.client.loop_start()

Timeout = 0

def make_message(x:float,t:int):
    data_message = f"('Jetson3',{x},{t})"
    return data_message

while Timeout <10:
    
    x = random.randint(10,100)/10
    message = make_message(x,Timeout)
    time.sleep(5)
    print("Message sent : ",message)
    client.send_message(message=message,topic=mqttClass_nano.topic)
    time.sleep(10)
    label1,x_1,t_iteration1 = mqttClass_nano.data_j1
    label2,x_2,t_iteration2 = mqttClass_nano.data_j2
    
    print("Message from Jetson 1 received : ",mqttClass_nano.data_j1)
    print("Message from Jetson 2 received : ",mqttClass_nano.data_j2)
    Timeout+=1
    
    
client.client.loop_stop()


def optimisation():
    #faire l'algo d'optimisation
    #t_3=0
    #while condition d'arrêt non respecté:
    #   t_3 +=1
    #   data = receive()
    #   label,x,t = data
    #   if t != t_3-1:
    #       print("Unexpected error")
    #          break
    #   if label == 'Jetson1':
    #       x_1 = x
    #   elif label == 'Jetson2':
    #       x_2 = x
    #   else:
    #       x_3 = x
    #   do iteration of algorithm
    #   send(('Jetson3',x_3,t_3))
    pass
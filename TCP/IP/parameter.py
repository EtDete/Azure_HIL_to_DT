#Quelles sont les adresses IP des cartes Jetson
nb_cartes = int(input("Combien de cartes Jetson Nano il y a t-il ?"))
Ip_cartes = []
Port_cartes = []
for i in range(nb_cartes):
    Ip_cartes.append(input(f"Adresse IPV4 de la carte Jetson n°{i+1}"))
    Port_cartes.append(int(input(f"Port de communication de la carte Jetson n°{i+1}")))

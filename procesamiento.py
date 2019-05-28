from scapy.all import *
import time 
from globales import *
import base_de_datos

def actualizar_datos_del_programa(pkt):

	#guardar los datos en el archivo para analizarlos

	wrpcap('datos.pcap', pkt, append=True)

	#filtrar beacons y estimar cuantas se mandan por 5 segundos
	if pkt[Dot11].haslayer("Dot11Beacon"):
		database_beacons['total_beacons'] += 1
		if (time.time() - database_beacons['time_beacon']) > 5:
		 	database_beacons['time_beacon'] = 0
		 	database_beacons['numero_de_beacons_previo'] = database_beacons['numero_de_beacons_actual']
		 	database_beacons['numero_de_beacons_actual'] = 0
		if database_beacons['time_beacon'] == 0:
		 	database_beacons['time_beacon'] = time.time()
		database_beacons['numero_de_beacons_actual'] += 1

	#En el caso de que sea datos
	if pkt[Dot11].haslayer("Dot11QoS") or pkt[Dot11].subtype == 4:
		base_de_datos.insertar_dato_de_dispositivo(pkt)
		

import sys
import os
from scapy.all import *
import time 
import sqlite3 as lite
import matplotlib.pyplot as plt
import output
import procesamiento
import base_de_datos
from globales import *


#2 PROCESAMIENTO DE LOS PAQUETES

def packet_management(pkt):

		procesamiento.actualizar_datos_del_programa(pkt)
		output.imprimir_output()


#2 INICIAR PROCESON
if __name__ == '__main__':

	try:
		os.system("clear")

		#Creando la base de datos
		base_de_datos.crear_nuevo_almacen()
		

		#Iniciando la recogida de paquetes
		sniff(iface=iface, prn=packet_management, filter= ("ether host " + sys.argv[1]))
	
	finally:

		#Sacando la info resultante de la base de datos en forma de grafico
		base_de_datos.mostrar_info_en_graficos()

    	#limpiando la pantalla y saludo
    	os.system("clear")
    	print("Gracias por usar WIFI ADVANCE ANALYZER")









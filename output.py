import matplotlib.pyplot as plt
import os
from globales import *

def imprimir_output():

	os.system("clear")
	print('		                  [*] WIFI ADVANCE ANALYZER \n')
	print ("\t TOTAL DE BEACONS -> " + str(database_beacons['total_beacons']) + "   |   " + "BEACONS / 5 SEGUNDOS -> " + str(database_beacons['numero_de_beacons_previo']) + "     ")
	for dispositivo in database_provisional:
		if dispositivo == Wifi_MAC:
			print("\tWIFI        - " + str(dispositivo) + " -> " + str(database_provisional[dispositivo]) + " paquetes enviados")

		else:
			print("\tDISPOSITIVO - " + str(dispositivo) + " -> " + str(database_provisional[dispositivo]) + " paquetes enviados")


def crear_grafico(paquetes_capturados, dispositivo):
	plt.plot(paquetes_capturados, [x for x in range(len(paquetes_capturados))])
	plt.title(dispositivo)
	plt.ylabel('Numero de paquetes')
	plt.xlabel('Tiempo en segundos')
	plt.show()
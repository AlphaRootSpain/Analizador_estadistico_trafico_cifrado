import output
import time 
import sqlite3 as lite
from globales import *
from scapy.all import *

def crear_nuevo_almacen():
	global con, cur
	con = lite.connect('wifi_database.db')
	cur = con.cursor()
	cur.execute('DROP TABLE IF EXISTS ' + "_".join(Wifi_MAC.split(':')))
	cur.execute('CREATE TABLE ' + "_".join(Wifi_MAC.split(':')) + ' (dispositivo TEXT, tiempo INT)')

def insertar_dato_de_dispositivo(pkt):
	cur.execute('INSERT into ' + "_".join(Wifi_MAC.split(':')) + ' VALUES(\"' + "_".join(pkt[Dot11].addr2.split(':')) + '\", '+ str(time.time()) + ')')
	if "_".join(pkt[Dot11].addr2.split(':')) in database_provisional:
		database_provisional["_".join(pkt[Dot11].addr2.split(':'))] += 1
	else:
		database_provisional["_".join(pkt[Dot11].addr2.split(':'))] = 1

def mostrar_info_en_graficos():
	cur.execute('SELECT * FROM ' + "_".join(Wifi_MAC.split(':')))
	rows = cur.fetchall()
	for dispositivo in database_provisional:
		paquetes_capturados = []
		for row in rows:
			if row[0] == dispositivo:
				paquetes_capturados.append(row[1] - tiempo_inicial)
		#Creando los graficos
		output.crear_grafico(paquetes_capturados, dispositivo)
	con.close()
		
		

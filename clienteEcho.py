#.........................Librerias Importadas..................................................................
import argparse			#Para la lectura de Argumentos
import re				#Para la busqueda del patron en server:port
import sys	
from socket import *

#..........................Definicion de Procedimientos........................................................

#Envio de Echo UDP (-String Server,-Int Port)
def envio_udp(Server,Port):			
	clientSocket = socket(AF_INET, SOCK_DGRAM)							#Creo un Socket UDP
	print "Conexion UDP al Servidor: %s al Puerto: %s" %(Server,Port)	
	mensaje= raw_input("(UDP) Ingrese el mensaje a enviar: ")			#Leo mensaje a enviar
	clientSocket.sendto(mensaje,(Server,Port))							#Envio el mensaje al (server, puerto)
	mensaje2,servaddr = clientSocket.recvfrom(2048)						#Recibo el mensaje
	print "(UDP) Se recibio el mensaje: "+mensaje2						#Imprimo el mensaje recibido
	if(mensaje == mensaje2):
		print "(UDP) El mensaje recibido es igual al enviado"
	else:
		print "(UDP) El mensaje recibido es distinto al enviado"

#Envio de echo TCP  (-String Server,-Int Port)
def envio_tcp(Server,Port):
	clientSocket = socket(AF_INET, SOCK_STREAM)								#Creo un Socket TCP
	clientSocket.connect((Server,Port))										#Conecto el Socket con el socket TCP que asigne 
	try:																	# el pedido de conexion al socket de Bienvenida
		while True:
			print															
			print "Conexion TCP al Servidor: %s al Puerto: %s" %(Server,Port)	
			mensaje= raw_input("(TCP) Ingrese el mensaje a enviar: ")			#Leo mensaje a enviar
			clientSocket.send(mensaje)											#Envio el mensaje
			mensaje2= clientSocket.recv(2048)									#Leo el mensaje que me envia el server
			print "(TCP) Se recibio: "+mensaje2
			if(mensaje == mensaje2):
				print "(TCP) El mensaje recibido es igual al enviado"
			else:
				print "(TCP) El mensaje recibido es distinto al enviado"
	except KeyboardInterrupt:
		print "\n Finalizo la conexion TCP"
		clientSocket.close()												#Cierro la conexion del Socket  TCP

#...................................Codigo del Programa Ppal........................................................

#Generacion de ayuda y control de parametros obligatorios 
parser = argparse.ArgumentParser() 
parser.add_argument('server',metavar="server:port",type=str, nargs=1, help='  nombre  del  servidor  al  cual  se  debe  conectar,  especificando  el  puerto  adecuado')
parser.add_argument("-p", metavar="<tcp|udp>", choices=['udp', 'tcp'],help="tipo de protocolo de transporte utilizado para la conexion",required=True)
args = parser.parse_args()

#Reconocer server:port
patron = re.compile('([0-9a-zA-Z.]+):([0-9]+)')	# En el nombre del server pueden ir minusculas,mayusculas y puntos
matcher = patron.search(args.server[0])			#  en cambio en el puerto solo numeros
server=matcher.group(1)		#Primera Parte de la Expresion
port=matcher.group(2)		#Segunda Parte de la Expresion

#Reconocer tipo de conexion
if (args.p == "udp") :
	envio_udp(server,int(port))
else:
	envio_tcp(server,int(port))




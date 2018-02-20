#!/usr/bin/python3

import socket

# Definición de funciones
numbers = [5, 4, 3, 2, 1, 0]
index = -1
def contador():
	global index
	index = index + 1
	if index == 6:
		index = 0
	return numbers[index]

codes = {'200': 'OK', '404': 'Not Found'}
def send_response(Code, Body):
	response = ("HTTP/1.1" + " " + Code + " " + codes[Code] + "\r\n\r\n" +
				"<html><body>" + str(Body) + "</body></html>")
	return response

# INICIALIZACIÓN
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mySocket.bind(('localhost', 1234))
mySocket.listen(5)

try:
	while True:
		# SERVIDOR SE P0NE A ESCUCHAR
		print('Waiting for connections')
		(recvSocket, address) = mySocket.accept()
        
		# PARTE DE REALIZAR OPERACIONES
		request = str(recvSocket.recv(2048), 'utf-8')
		resource = request.split()[1]
        
		if resource == "/contador":
			c = contador()
			coment = send_response('200', c)
		else:
			coment = send_response('404', "Not Found!")
							
		# ENVIAMOS LOS RESULTADOS
		recvSocket.send(bytes(coment, 'utf-8'))
		recvSocket.close()
			   
except KeyboardInterrupt:
    print("Closing binded socket")
mySocket.close()

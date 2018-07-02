#!/usr/bin/python3

import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()

port = 9999

serversocket.bind((host, port))

serversocket.listen(10)

while True:
   clientsocket, addr = serversocket.accept()

   print("Connection from %s" % str(addr))

   msg = "Thanks for connecting" + "\r\n"
   clientsocket.send(msg.encode('ascii'))
   clientsocket.close()

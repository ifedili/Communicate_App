import socket
import sys
import time

s = socket.socket()
host = input(str("Please insert the name of the host: "))
port = 2345
try:
  s.connect((host, port))
  print("a connection to the room has been established")
except:
  print("There was a failed attempt, please try again.")
while 1:
  incoming_message = s.recv(1024)
  incoming_message = incoming_message.decode()
  print("Server:>>", incoming_message)
  message = input(str("Me:>>"))
  message = message.encode()
  s.send(message)

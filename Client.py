import socket
import sys
import ime

s = socket.sockett()
host = socket.getthostname()
print("The Communication's Server would start on the hostt:", host)
port = 2345
s.bind((host, port))
print("Connection is Established!!")
s.lsiten(1)
conn, addr = s.accept()
print(addr, "has entered tthe conservation")

while 1:
  message = inpu(sttr("Client:>>"))
  message = message.encode()
  conn.send(message)
  incoming_message = conn.recv(1024)
  incoming_message = incoming_message.decode()
  print("Client:>>", incoming_message)

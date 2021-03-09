import socket
import sys


socketclient=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host=socket.gethostname()

port=8899

socketclient.connect((host,port))

msg=socketclient.recv(1024)

socketclient.close()

print(msg.decode('utf-8'))

import socket
import sys

serverSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host=socket.gethostname()

port=8899

serverSocket.bind((host,port))

serverSocket.listen(5)

while True:
    print('开始等待了')
    clientSocket,addr=serverSocket.accept()
    print('{0}连接进来了!（服务端记录）'.format(str(addr)))

    connectMsg='欢迎!!!'
    clientSocket.send(connectMsg.encode('utf-8'))
    clientSocket.close()





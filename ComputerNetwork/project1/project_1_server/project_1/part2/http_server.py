#!/usr/bin/python3 
from socket import *
import sys
import time
serverPort = 1997
server_Socket = socket(AF_INET,SOCK_STREAM)
server_Socket.bind(('172.17.16.1', serverPort))

server_Socket.listen(1)
print ("server is ready to be contacted . . .\n")
while True:
    client_Socket, addr = server_Socket.accept()
    recieved_header = (client_Socket.recv(1024)).decode("utf-8")
    end = recieved_header.rfind("HTTP")
    first = recieved_header.find("GET")
    temp  =recieved_header[first + 4:end-1]
    file_name =temp[temp.rfind("/") + 1:]
    error_file = "notFound.html"
    try:
        f = open(file_name, 'rb')
        deliver_state = True
    except:
        f = open(error_file, 'rb')
        deliver_state = False
    while True:
        temp1 = f.read(1024)
        if not temp1:
            time.sleep(0.1)
            f.close()
            client_Socket.send(("end connection\r\n").encode("utf-8"))
            break
        client_Socket.send(temp1)
    if deliver_state:
        deliver_msg = "HTTP/1.1 200 OK\r\n\r\n"
    else:
        deliver_msg = "HTTP/1.1 404 Not Found\r\n\r\n"
    client_Socket.send((deliver_msg).encode("utf-8"))
    print (deliver_msg[0: deliver_msg.find("\r")])
    client_Socket.close()


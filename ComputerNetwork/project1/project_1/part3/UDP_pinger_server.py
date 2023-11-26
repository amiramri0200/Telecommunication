#!/usr/bin/python3 
from socket import *
server_port = 1997
server_ip = "172.17.16.1"
s = socket(AF_INET,SOCK_DGRAM)
s.bind((server_ip,server_port))
print("server is ready to be contacted ...\n")    
while True:
    msg, client_ip =s.recvfrom(1024)
    s.sendto(msg, client_ip)
    

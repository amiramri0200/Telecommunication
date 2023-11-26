#!/usr/bin/python3.6 
import socket
import time 
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_ip = '172.17.16.1'
port_server = 1997
s.connect((server_ip,port_server))
sentence = input('what do u want to tell the server?')
time1 = time.time()
s.send(bytes(sentence,"utf-8"))
modifiedSentence = s.recv(1024)
time2 = time.time()
print('the answer from Server:', modifiedSentence.decode("utf-8"))
s.close()
RTT = (time2 - time1)*1000
print("RTT = %d ms"%RTT)


#!/usr/bin/python3 
import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_ip = '172.17.16.1' 
port = 1997
s.bind((server_ip,port))
s.listen(1)
print('sever is ready to be contacted ...')
while 1:
    client_socket,client_ip = s.accept()
    client_sentence=client_socket.recv(1024)
    client_sentence_mod = client_sentence.decode("utf-8")
    client_socket.send(bytes("ACK ---> ur sentece is :","utf-8"))
    client_socket.send(bytes(client_sentence_mod,"utf-8"))
    client_socket.close()
print('the ACK has been sent!')


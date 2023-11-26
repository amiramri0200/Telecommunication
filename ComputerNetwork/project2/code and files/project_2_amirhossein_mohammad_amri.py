#!/usr/bin/python
import socket,time
tcpSerPort = 8899
address= ('127.0.0.1',8899)
tcpSerSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpSerSock.bind(address)
tcpSerSock.listen(5)
while True:
    print('server is ready...')
    connection_from_client, addr = tcpSerSock.accept()
    print('Received a connection from: ', addr)
    message = connection_from_client.recv(4096).decode()
    print(message)
    filename = message.split()[1].partition("/")[2]
    print('///////////////////')        
    print(filename)
    file_Exist = "false"
    try:
        f = open(filename+'.html',"r")
        data = f.readlines()
        print(data)
        file_Exist = "true"
        connection_from_client.send("HTTP/1.1 200 OK \r\n".encode())
        time.sleep(.07)
        connection_from_client.send("Content-Type:text/html\r\n")
        for i in range(0, len(data)):
            connection_from_client.send(data[i].encode())
        print("Read from cache")
    except IOError:
        if file_Exist == "false":
            print('------------------------------------------------')
            print("creating a socket on proxy")
            c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            host_name = filename.replace("www.","",1)
            print("Host name : ",host_name)
            try:
                c.connect((host_name, 80))
                c.sendall(message.encode())
                buff = c.recv(4096)
                print(buff)
                connection_from_client.send(buff)
            except:
                print("Illegal request")
        else:
            print("file notFound")
    connection_from_client.close()
tcpSerSock.close()





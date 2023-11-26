from socket import *
import webbrowser
import sys
server_ip = '172.17.16.1'
file_path = "helloworld.html"
target_port = 1997 # create a socket object
try:
    client = socket(AF_INET, SOCK_STREAM)

    # connect the client
    client.connect((server_ip, target_port))
except:
    print("can't connect to the server")
    sys.exit()

# send some data
data = ""
request = ("GET %s HTTP/1.1\r\nHost:%s\r\n\r\n" % (file_path,server_ip)).encode("utf-8")
client.send(request)
with open("helloworld.html", 'wb') as f:
    while True:
        data =(client.recv(1024)).decode("utf-8")
        if data == "end connection\r\n":
            f.close()
            break
        f.write(data.encode("utf-8"))
deliver_state =(client.recv(1024)).decode("utf-8")
print( "deliver_state = " + deliver_state[0: deliver_state.find("\r")])
client.close()
webbrowser.open('helloworld.html')
print("data connection disconnected")


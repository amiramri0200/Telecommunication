from socket import *
import webbrowser
import sys
target_host = '127.0.0.1'
web=sys.argv[1]
print(web)
file_path = "/"+web
target_port = 8899  # create a socket object
try:
    client = socket(AF_INET, SOCK_STREAM)

    # connect the client
    client.connect((target_host, target_port))
except:
    print("can't connect to the server")
    sys.exit()

# send some data
request = "GET %s HTTP/1.1\r\nHost:%s\r\n\r\n" % (file_path, target_host)
client.send(request.encode())
with open("file.html", 'wb') as f:
    print("recieving data...")
    while True:
        print('fuck')
        data = client.recv(1024)
        if not data:
            f.close()
            break
        print(data)
        temp= data.partition("Content-Type:text/html\r\n")
        print(temp)
        f.write(temp[2])
deliver_state = client.recv(1024).decode()
print("deliver_state = " + deliver_state[0: deliver_state.find("\r")])
client.close()
webbrowser.open('file.html')
print("data connection disconnected")

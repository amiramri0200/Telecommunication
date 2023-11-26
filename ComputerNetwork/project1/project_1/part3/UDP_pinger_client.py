#!/usr/bin/python3 
import time
from socket import *
print("Usage: python UDPPingerClient\n <server ip address : 172.17.16.1> \r\n <server port no : 1997>")

# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
clientSocket = socket(AF_INET, SOCK_DGRAM)

# To set waiting time of one second for reponse from server
#clientSocket.settimeout(1)

ten_ping = [1,2,3,4,5,6,7,8,9,10]
server_ip = "172.17.16.1"
serverPort = 1997 
packetLost = 0
maxRtt = 0
minRtt = 100
RTT = 0
sum_of_RTTs = 0 
client = socket(AF_INET, SOCK_DGRAM)
for counter in ten_ping:
    client.sendto(str(counter).encode("utf-8"), (server_ip, serverPort))
    timer1 = time.time()
    client.settimeout(2)# To set waiting time of one second for reponse from server

    try:
        receive = client.recv(1024)
        timer2 = time.time()
        if(int(receive) == counter):
            RTT = timer2 - timer1
            if RTT > maxRtt:
                maxRtt = RTT
            if RTT < minRtt:
                minRtt = RTT
            print("time for ping %d = %dms" % (counter, RTT * 1000))
        sum_of_RTTs = sum_of_RTTs+RTT
    except:
        packetLost = packetLost + 1
        print("ping %d has been lost"%counter)
print("packet loss =%d percent " %(packetLost*10))
mean_of_RTT = sum_of_RTTs/(10-packetLost)
print( "max RTT: %dms\nmin RTT: %dms\nmean RTT: %fms" % (maxRtt * 1000, minRtt * 1000, (mean_of_RTT) * 1000))
client.close()

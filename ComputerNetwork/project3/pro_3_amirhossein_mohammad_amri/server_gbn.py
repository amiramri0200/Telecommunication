#!/usr/bin/python 
import socket 
import random
#import numpy as np 
from socket import *
import sys
import os
#from prettytable import PrettyTable  
if len(sys.argv) != 3:
    print "check your input argument \n you shoud print :  "
    print "1) a name that you want to save the file with that name"
    print "2) the probability of discard"
    exit(2)
#                      ***********************
#********************* * this is server code **********************************
#                      ***********************    

serverSock = socket(AF_INET, SOCK_DGRAM)
serverIp = '127.0.0.1'
serverPort = int(7735)
serverSock.bind((serverIp, serverPort))
acknum = (1)
header_1 = '0101010101010101'
header_2 = str(0b1010101010101010)
filename =sys.argv[1]
pro =float(sys.argv[2])
#tabl = PrettyTable(["event ","seqnum"])



def check_sum_maker(arg):
    f = []
    temp = []
    checksum = 0
    a = bytearray(arg)
    for i in range(0,len(a)):
        f.append(a[i])
    for z in range(0,len(f)-1,2):
        temp.append((f[z]<<8) + f[z+1])
    for i in range(0,len(temp)):
        checksum = checksum +temp[i] 
        checksum2 = checksum - 65535
        if(checksum2 >= 0):    
            checksum = -65535 + checksum 
        checksum = 65535 - checksum
    return str(checksum)    
#
with open(filename,'wb') as f : 
    i = 0 
    while True:
        discard = random.random()
        msg, addr = serverSock.recvfrom(100000)
        tem = msg.partition(header_1)
        recieving_data = tem[2]
        checksum_recieving = check_sum_maker(recieving_data)
        tem = tem[0].partition(checksum_recieving)#if we could find checksum it means that the chechsum is True
        recieving_seqnum = tem[2]
        if discard >= pro: 
            if recieving_seqnum == str(acknum) + " ":
                f.write(recieving_data)
                serverSock.sendto((str(acknum) + '0000' + header_2 ), addr)
                acknum = (acknum + 1)
        else :
            #tabl.add_row(['Packet loss',acknum])
            print("Packet loss , seqnum : %d")%(acknum)
        if msg == "close":
            f.close()
            break

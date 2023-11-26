#!/usr/bin/python 
import sys
import time 
import socket 
#import numpy as np 
import threading 
from socket import *

#                            ************************* 
# ************************** *this is the client code* *********************************************
#                            *************************

#*** in this part we check the number of input arguments *******************************************
if len(sys.argv) != 6:
    print "please check your input arguments"
    print("1) servers ip")
    print("2) servers port")
    print("3) the file_name that you want to send")
    print("4) the window size")
    print("5) max of segment size")
    exit(2)
#---------------------------------------------------------------------------------------------------

#*************** initializing the arguments ********************************************************
ip = sys.argv[1] #-------------this is the sever ip 
sock = int(sys.argv[2] )#------this is the sever port
file_name =sys.argv[3]
N = int(sys.argv[4])
Mss = int(sys.argv[5])
s=socket(AF_INET,SOCK_DGRAM)#--creating the socket
header_1 = ' 0101010101010101'
data = []
base = 1 
nextseqnum = (1)
timer = [time.time(),True]
stopflg = True
sample_Rtt = ()
st1 = 0 
st2 = 0 
estimated_Rtt = 0
DevRTT = 0
stopflg2 =0 
ss=True
#---------------------------------------------------------------------------------------------------

#*** in this part each  Mss bytes of data is  appended to a list ***********************************
text=[]
a = 1
with open(file_name,'rb') as ob:
    while a :
        a = ob.read(Mss) 
        text.append(a)
counter = 0 
print('the number of packet is {}.'.format(len(text)))
#---------------------------------------------------------------------------------------------------

#******** time function ****************************************************************************
def start_timer():
    global timer 
    timer = [time.time(),1]
#---------------------------------------------------------------------------------------------------

#********* in this function we take the data as input and return the checksum in sting type *********
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
#----------------------------------------------------------------------------------------------------

#************* a fucntion for making packets ready for sending **************************************
def make_pkt(arg,arg2):#-----------------------------------arg stands for main data  
    global header_1    #-----------------------------------arg2 stands for nextseqnum 
    t = check_sum_maker(arg) + str(arg2) + header_1 + arg 
    return t 
#----------------------------------------------------------------------------------------------------

#******* fucntion for estimating the RTT ************************************************************
def Rtt(sample_rtt):
    global estimated_Rtt , DevRTT
    alpha = 0.125 
    beta = 0.25
    estimated_Rtt = (1 - alpha) * estimated_Rtt + alpha * sample_rtt
    DevRTT = (1 - beta) * DevRTT + beta * abs(sample_rtt - estimated_Rtt)
    return (estimated_Rtt + 4 * DevRTT)
#----------------------------------------------------------------------------------------------------

# *************** the function for reliable data transfer********************************************
def rdt_send(content_of_file):
    global nextseqnum , N , base , sample_Rtt,st1,ss
    if nextseqnum < (base + N) and ss:
        snd_pkt = make_pkt(content_of_file,nextseqnum)
        s.sendto(snd_pkt,(ip,sock))
        st1  = time.time()
        if base == nextseqnum :
            start_timer()
        nextseqnum =( nextseqnum + 1 )
        return True   
    else :
        return False 
# ---------------------------------------------------------------------------------------------------
#*************** main function for sending the file *************************************************
def gbn_send():
    time_for_hole_packet = time.time()
    global data ,stopflg,text,counter
    while True :
        try:
            if rdt_send(text[counter]):
                counter = counter + 1 
        except:
            #print(len(text))
            if stopflg2==len(text)-1 or stopflg2==len(text):
                stopflg = False
                s.sendto("close",(ip,sock))
                time_for_hole_packet = time_for_hole_packet - time.time()
                print('the hole time for sending the file is : %d ')%(-time_for_hole_packet)
                break

        if counter > (len(text)) and stopflg2==len(text)-1:
            stopflg = False
            s.sendto("close",(ip,sock))
            time_for_hole_packet = time_for_hole_packet - time.time()
            print('the hole time for sending the file is : %d ')%(-time_for_hole_packet)
            break
# ---------------------------------------------------------------------------------------------------

#************** function for recieving the acknum ***************************************************
def gbn_rcv():
    global nextseqnum , base ,timer,st2,stopflg2,text
    while True:
        if stopflg:
            try :
                ack = s.recv(1024)
                stopflg2=int(ack.partition('0000'+str(0b1010101010101010))[0])
                st2 = time.time()
                s.settimeout(10)
            except :
                pass
        elif not stopflg :
            break
        base = (base + 1)
        if(base == nextseqnum):
            timer[1] = False
        else:
            timer = [time.time(), True]
# ---------------------------------------------------------------------------------------------------

#*************************** function for considering the time out **********************************
def time_out():
    global timer , nextseqnum , stopflg,ss,counter
    while 1 :
        if not stopflg:
            print("++++++++++++++=================+++++++++++++++++================")
            break
        if ((time.time()-timer[0]) > 0.1 ) and (stopflg) and timer[1]:
            print("Timeout ----->  sequence_number = %d ")%(nextseqnum)
            ss=False
            for q in range(base,nextseqnum):
                snd_pkt = make_pkt(text[q-1],q)
                s.sendto(snd_pkt,(ip,sock))
            ss=True
            #counter= q-1
            timer = [time.time(),1]
#----------------------------------------------------------------------------------------------------
                
thread1 = threading.Thread(target=gbn_send)
thread2 = threading.Thread(target=gbn_rcv)
thread3 = threading.Thread(target=time_out)

thread1.start()
thread2.start()
thread3.start()
thread1.join()
thread2.join()
thread3.join()



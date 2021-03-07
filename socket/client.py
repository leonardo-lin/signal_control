# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 21:15:17 2021

@author: leo
"""

import socket

HOST = '192.168.43.201'
PORT = 8000

clientMessage = ['mp',6,89]
print(clientMessage)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
while(1):
    i=0
    a=''
    while(i<3):
        #clientMessage[i]=input()
        a+=str(clientMessage[i])
        a+=','
        i+=1   
    client.sendall(a.encode())    
    #serverMessage = str(client.recv(1024), encoding='utf-8')
    #print('Server:', serverMessage)

client.close()
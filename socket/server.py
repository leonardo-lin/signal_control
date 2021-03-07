# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 20:49:32 2021

@author: leo
"""

# -*- coding: utf-8 -*-
#import sys
import socket
HOST = '192.168.43.201'
PORT = 8000 

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(10)
conn, addr = server.accept()
while True:

    clientMessage = str(conn.recv(1024), encoding='utf-8')
    i=0
    j=0
    signal=['','','']
    while(i<len(clientMessage)):
        if clientMessage[i]!=',':           
            signal[j]+=(clientMessage[i])
        else:
            j+=1
        i+=1
    print('Client message is:',signal)
    #serverMessage = 'I\'m here!'
    #conn.sendall(serverMessage.encode())
    
    conn.close()        
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 23:02:31 2021

@author: leo
"""
from pynput.mouse import Listener
#from pynput import keyboard
import socket
import time
HOST = '192.168.31.174'
PORT = 8000
clientMessage = ['mp',6,89]
print(clientMessage)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
print("connet success")
"""while(1):
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
"""
#client.close()
from pynput import keyboard
import json
import time
def h():
    from pynput.mouse import Listener
    
    def on_move(x, y):
        print('Pointer moved to {0}'.format(
            (x, y)))
        print(type(x))
        
        a={'0':'mm','1':x,'2':y}       
        #print(time.time())
        b=json.dumps(a)
        print(b)
        client.send(b.encode())
    def on_click(x, y, button, pressed):
        print('{0} at {1}'.format(
            'Pressed' if pressed else 'Released',
            (x, y)))
        print(button)
        print(type(button),type(pressed))
        a={'0':'mp','1':x,'2':y}       
        print(a)
        b=json.dumps(a)
        print(b)
        client.send(b.encode())
        if not pressed:
            # Stop listener
            a={'0':'mr','1':x,'2':y}       
            print(a)
            b=json.dumps(a)
            print(b)
            client.send(b.encode())
            return False
    def on_scroll(x, y, dx, dy):
        print('Scrolled ',x,y,dx,dy)
        a={'0':'mm','1':dx,'2':dy}       
        print(a)
        b=json.dumps(a)
        print(b)
        client.send(b.encode())
    # Collect events until released
    with Listener(
            on_move=on_move,
            on_click=on_click,
            on_scroll=on_scroll) as listener:
        listener.join()
#keyboard        
def k():
    doc ={'get':[]}
    def on_press(key):
        try:
            print('alphanumeric key {0} pressed'.format(
                key.char))
            #print(type(key),key)
            if(key.char in doc['get']):
                doc['get'].append(key.char)
                a={'0':'kp','1':key.char,'2':5}       
                #print(a)
                b=json.dumps(a)
                print(b)
                client.send(b.encode())
                #print('get',key.char)
            else:
                print('again',key.char)
            
            
            
        except AttributeError:
            print('special key {0} pressed'.format(
                key))
            print(key)
            if(key==keyboard.Key.up):
                a={'0':'kp','1':'up','2':0}
            if(key==keyboard.Key.down):
                a={'0':'kp','1':'down','2':0}
            if(key==keyboard.Key.left):
                a={'0':'kp','1':'left','2':0}
            if(key==keyboard.Key.right):
                a={'0':'kp','1':'right','2':0}
            if(key==keyboard.Key.enter):
                a={'0':'kp','1':'enter','2':0}
         
            #a={'0':'kp','1':key.char,'2':0}      
            #print(a)
            b=json.dumps(a)
            print(b)
            client.send(b.encode())
             #client.sendall(key)
    def on_release(key):
        try:            
            print('{0} released'.format(key))
            
            a={'0':'kr','1':key.char,'2':5}       
            #print(a)
            b=json.dumps(a)
            print(b)
            client.send(b.encode())
        except Exception:
            print('{0} released'.format(key))
            if(key==keyboard.Key.up):
                a={'0':'kr','1':'up','2':0}
            elif(key==keyboard.Key.down):
                a={'0':'kr','1':'down','2':0}
            elif(key==keyboard.Key.left):
                a={'0':'kr','1':'left','2':0}
            elif(key==keyboard.Key.right):
                a={'0':'kr','1':'right','2':0}
            elif(key==keyboard.Key.enter):
                a={'0':'kr','1':'enter','2':0}
            #print(a)
            b=json.dumps(a)
            print(b)
            client.send(b.encode())
        if key == keyboard.Key.esc:
            # Stop listener
            return False
    
    # Collect events until released
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()
k()
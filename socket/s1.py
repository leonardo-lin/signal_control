# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 23:02:31 2021

@author: leo
"""
import time
from pynput.keyboard import Key, Controller
keyboard_control = Controller()
from pynput import keyboard
from threading import Thread
from  pynput.mouse import Button,Controller 
mouse_control = Controller() 
check_if_press ={'get':[]}
press_key = {}
class pressing(Thread):
    def __init__(self, key, press_dict):
        Thread.__init__(self)
        self.signal = False
        self.key = key
        self.press_dict = press_dict
    def run(self):
        count = 0
        while(self.key in self.press_dict['get']):
            count+=1
            time.sleep(0.01)
            keyboard_control.press(self.key)
            if self.signal:
                print(f'{self.key} thread killed by signal, count={count}')
                break
            if count==100:
                print(f'{self.key} thread killed')
                break
    def kill(self):
        print(f'{self.key} kill signal emit')
        self.signal = True

def mmove(x,y):
    mouse_control.position=(x,y)
    print(mouse_control.position)
    #print(time.time())
def mpress():
    mouse_control.press(Button.left)
    print('mouse has press')
    #print(time.time())
def mrelease():
    mouse_control.release(Button.left)
    print('mouse has release')
    #print(time.time())
    exit(1)
def mscroll(x,y):
    mouse_control.scroll(x,y)
    print('mouse scroll')
    #print(time.time())

def kpress(a):
    #keyboard.press(a)
    keyboard_control.press(a)
    check_if_press['get'].append(a)
    print('keyboard press',a)
    th=pressing(a, check_if_press)
    press_key[a] = th
    press_key[a].daemon = True
    press_key[a].start()
    # press_key[a].join()
    
    

def krelease(a):
    keyboard_control.release(a)
    print('keyboard release',a)
    print(check_if_press['get'])
    check_if_press['get'].remove(a)
    press_key[a].kill()
    print('killed')
    
    
    
#start the main
#socket connect    
import json
import socket
HOST = '192.168.0.101'
PORT = 8000 
print("connecting")
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(10)
conn, addr = server.accept()
print("connect success")
#count=0

#consider mouse or keyboard
while True:
    #count+=1
    #print(time.time())
    clientMessage = (conn.recv(1024))
    signal=json.loads(clientMessage)
    #print (clientMessage)
    print(signal)
    if signal['0']=='mm':
        mmove(int(signal['1']),int(signal['2']))
    elif signal['0']=='mp':
        mpress()
    elif signal['0']=='mr':
        mrelease()
    elif signal['0']=='ms':
        mscroll(int(signal['1']), int(signal['2']))
    elif signal['0']=='kp':
        """if signal['1']=='up':
            keyboard_control.press(keyboard.Key.up)       
        elif signal['1']=='down':
            keyboard_control.press(keyboard.Key.down)         
        elif signal['1']=='left':
            keyboard_control.press(keyboard.Key.left)
            #pressing('left')
        elif signal['1']=='right':
            keyboard_control.press(keyboard.Key.right)
            #pressing('right')
        elif signal['1']=='enter':
            keyboard_control.press(keyboard.Key.enter)
            #pressing('enter')"""
          
        kpress(signal['1'])
        #kpress(signal['1'])            
    elif signal['0']=='kr':
        """if signal['1']=='up':
            keyboard_control.release(keyboard.Key.up)
            check_if_press.remove('up')
        elif signal['1']=='down':
            keyboard_control.release(keyboard.Key.down)
            check_if_press.remove('down')
        elif signal['1']=='left':
            keyboard_control.release(keyboard.Key.left)
            check_if_press.remove('left')
        elif signal['1']=='right':
            keyboard_control.release(keyboard.Key.right)
            check_if_press.remove('right')
        elif signal['1']=='enter':
            keyboard_control.release(keyboard.Key.enter)
            check_if_press.remove('enter')"""
        
        krelease((signal['1']))
    """i=0
    j=0
    signal=['','','']
    while(i<len(clientMessage)):
        if clientMessage[i]!=',':           `
            signal[j]+=(clientMessage[i])
        else:
            j+=1
        i+=1"""
        
    #print('Client message is:',signal)
    #print('message is ',clientMessage)
    #serverMessage = 'I\'m here!'
    #conn.sendall(serverMessage.encode())
    
    #conn.close()      
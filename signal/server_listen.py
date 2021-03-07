# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 20:59:46 2021

@author: leo
"""
from pynput.keyboard import Key, Controller
keyboard = Controller()
from  pynput.mouse import Button,Controller 
mouse = Controller() 
def mmove(x,y):
    mouse.position=(x,y)
    print(mouse.position)
def mpress():
    mouse.press(Button.left)
    print('mouse has press')
def mrelease():
    mouse.release(Button.left)
    print('mouse has releae')
def mscroll(x,y):
    mouse.scroll(x,y)
    print('mouse scroll')
def kpress(a):
    #keyboard.press(a)
    keyboard.press(a)
    print('keyboard press',a)
def krelease(a):
    keyboard.release(a)
    print('keyboard release')
if __name__ == '__main__':
    print('aa')
    signal=[0,0,0]
    import socket
    HOST = '192.168.43.201'
    PORT = 8000 
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(10)
    conn, addr = server.accept()
    while(1):
        """clientMessage = str(conn.recv(1024), encoding='utf-8')
        i=0
        j=0
        signal=['','','']
        while(i<len(clientMessage)):
            if clientMessage[i]!=',':           
                signal[j]+=(clientMessage[i])
            else:
                j+=1
            i+=1"""
        print(signal)
        if signal[0]=='mm':
            mmove(int(signal[1]),int(signal[2]))
        elif signal[0]=='mp':
            mpress()
        elif signal[0]=='mr':
            mrelease()
        elif signal[0]=='ms':
            mscroll(int(signal[1]), int(signal[2]))
        elif signal[0]=='kp':
            kpress(signal[1])
        elif signal[0]=='kr':
            krelease((signal[1]))
"""mouse = Controller()
print(mouse.position)
time.sleep(3)
print('The current pointer position is {0}',format(mouse.position))


#set pointer positon
mouse.position = (277, 645)
print('now we have moved it to {0}',format(mouse.position))

#鼠標移動（x,y）個距離
mouse.move(5, -5)
print(mouse.position)

mouse.press(Button.left)
mouse.release(Button.left)

#Double click
mouse.click(Button.left, 1)

#scroll two  steps down
mouse.scroll(0, 500)
"""
import time
keyboard = Controller()

#Press and release space
keyboard.press(Key.space)
time.sleep(1)
keyboard.release(Key.space)
print(Key.space)
time.sleep(1)
#Type a lower case A ;this will work even if no key on the physical keyboard  is labelled ‘A‘
keyboard.press('a')
time.sleep(1)
keyboard.release('a')
time.sleep(1)
#Type two  upper case As
keyboard.press('A')
time.sleep(1)
keyboard.release('A')
time.sleep(1)
# or 
with keyboard .pressed(Key.shift):
    keyboard.press('A')
    keyboard.release('a')
time.sleep(1)
#type ‘hello world ‘  using the shortcut type  method
keyboard.type('hello world')


    
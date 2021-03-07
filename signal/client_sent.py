# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 15:30:39 2021

@author: leo
"""
"""monitor the mouse"""
import socket

HOST = '192.168.43.201'
PORT = 8000

clientMessage = ['mp',6,89]
print(clientMessage)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
def h():
    from pynput.mouse import Listener
    
    def on_move(x, y):
        print('Pointer moved to {0}'.format(
            (x, y)))
        a='mm,'+str(x)+','+str(y)+','        
        #client.sendall(a.encode())   
    def on_click(x, y, button, pressed):
        print('{0} at {1}'.format(
            'Pressed' if pressed else 'Released',
            (x, y)))
        if not pressed:
            # Stop listener
            return True
    def on_scroll(x, y, dx, dy):
        print('Scrolled ',x,y,dx,dy)
    
    # Collect events until released
    with Listener(
            on_move=on_move,
            on_click=on_click,
            on_scroll=on_scroll) as listener:
        listener.join()
        
        
"""monitor the  keyboard"""      
def f():
    from pynput import keyboard
    
    def on_press(key):
        try:
            print('alphanumeric key {0} pressed'.format(
                key.char))
        except AttributeError:
            print('special key {0} pressed'.format(
                key))
    
    def on_release(key):
        print('{0} released'.format(
            key))
        if key == keyboard.Key.esc:
            # Stop listener
            return False
    
    # Collect events until released
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()
#from multiprocessing import Process
from threading import Thread


if __name__ == '__main__':
    p1= Thread(target=h)
    p1.start()
    p2=Thread(target=f)
    p2.start()
    p1.join()
    p2.join()
    

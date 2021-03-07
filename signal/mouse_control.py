# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 15:21:40 2021

@author: leo
"""
def h():
    from pynput.mouse import Listener
    
    def on_move(x, y):
        print('Pointer moved to {0}'.format(
            (x, y)))
    
    def on_click(x, y, button, pressed):
        print('{0} at {1}'.format(
            'Pressed' if pressed else 'Released',
            (x, y)))
        if not pressed:
            # Stop listener
            return False
    def on_scroll(x, y, dx, dy):
        print('Scrolled {0}'.format(
            (x, y)))
    
    # Collect events until released
    with Listener(
            on_move=on_move,
            on_click=on_click,
            #on_press=press,
            #on_release=release,
            on_scroll=on_scroll) as listener:
        listener.join()
    """from pynput import mouse

def on_move(x, y ):
    print('Pointer moved to {o}',format((x,y)))

def on_click(x, y , button, pressed):
    print('{0} at {1}',format('Pressed' if pressed else 'Released', (x, y)))
    if not pressed:
        return False

def on_scroll(x, y ,dx, dy):
    print('scrolled {0} at {c1}',format(
        (x, y)))

while True:
    with mouse.Listener( no_move = on_move,on_click = on_click,on_scroll = on_scroll) as listener:
        listener.join()
"""
"""from  pynput.mouse import Button, Controller
import time 

mouse = Controller()
print(mouse.position)
time.sleep(3)
print('The current pointer position is ',format(mouse.position))


#set pointer positon
#mouse.position = (286,422)
#print('now we have moved it to ',format(mouse.position))

#鼠標移動（x,y）個距離
#mouse.move(5, -5)
print(mouse.position)
#mouse.position=(1424,6)
print(mouse.position)
mouse.press(Button.left)
time.sleep(3)
mouse.release(Button.left)
#Double click
#mouse.click(Button.left, 1)

#scroll two  steps down
mouse.scroll(0, 500)
print('mouse scroll')"""



# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 17:28:09 2021

@author: leo
"""

import tkinter as tk
#import math
#若python2 T改大寫
# 建立主視窗和 Frame（把元件變成群組的容器）
window = tk.Tk()

window.title('各種測試')
window.geometry('400x400')

canvas = tk.Canvas(window, bg='blue', height=100, width=200)
canvas.pack()

image_file = tk.PhotoImage(file='ins.gif')
image = canvas.create_image(10, 10, anchor='nw', image=image_file)

x0, y0, x1, y1= 50, 50, 80, 80
line = canvas.create_line(x0, y0, x1, y1)

oval = canvas.create_oval(x0, y0, x1, y1, fill='red')  #创建一个圆，填充色为`red`红色
arc = canvas.create_arc(x0+30, y0+30, x1+30, y1+30, start=0, extent=180)  #创建一个扇形
rect = canvas.create_rectangle(100, 30, 100+20, 30+20)   #创建一个矩形

def moveit():
    canvas.move(image,1, 2)

b = tk.Button(window, 
    text='hit me',      # 显示在按钮上的文字
    width=15, height=2, 
    command=moveit)     # 点击按钮式执行的命令
b.pack() 
window.mainloop()
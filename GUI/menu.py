# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 21:38:08 2021

@author: leo
"""
import tkinter as tk
#import math
#若python2 T改大寫
# 建立主視窗和 Frame（把元件變成群組的容器）
window = tk.Tk()

window.title('各種測試')
window.geometry('800x800')


l=tk.Label(window,text='',bg='yellow')
l.pack()
counter = 0
def do_job():
    global counter
    l.config(text= str(counter))
    counter+=1
def do_jb():
    global counter
    l.config(text= 'haha')
    counter+=1
##创建一个菜单栏，这里我们可以把他理解成一个容器，在窗口的上方
menubar = tk.Menu(window)

##定义一个空菜单单元
filemenu = tk.Menu(menubar, tearoff=0)

##将上面定义的空菜单命名为`File`，放在菜单栏中，就是装入那个容器中
menubar.add_cascade(label='File', menu=filemenu)

##在`File`中加入`New`的小菜单，即我们平时看到的下拉菜单，每一个小菜单对应命令操作。
##如果点击这些单元, 就会触发`do_job`的功能
filemenu.add_command(label='New', command=do_job)
filemenu.add_command(label='Open', command=do_job)##同样的在`File`中加入`Open`小菜单
filemenu.add_command(label='hahaha', command=do_jb)##同样的在`File`中加入`Save`小菜单

filemenu.add_separator()##这里就是一条分割线

##同样的在`File`中加入`Exit`小菜单,此处对应命令为`window.quit`
#filemenu.add_command(label='Exit', command=window.quit)
submenu = tk.Menu(filemenu)##和上面定义菜单一样，不过此处实在`File`上创建一个空的菜单
filemenu.add_cascade(label='Import', menu=submenu, underline=0)##给放入的菜单`submenu`命名为`Import`
submenu.add_command(label="Submenu1", command=do_job)##这里和上面也一样，在`Import`中加入一个小菜单命令`Submenu1`



window.config(menu=menubar)

window.mainloop()
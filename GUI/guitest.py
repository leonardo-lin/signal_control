# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 16:35:05 2020

@author: leo
"""

import tkinter as tk
#import math
#若python2 T改大寫
# 建立主視窗和 Frame（把元件變成群組的容器）
window = tk.Tk()

window.title('各種測試')
window.geometry('800x800')


#按鈕
l = tk.Label(window, 
    text='TK!',    # 标签的文字
    bg='gray',     # 背景颜色
    font=('Arial', 12),     # 字体和字体大小
    width=15, height=2  # 标签长宽
    )
l.pack()  

varq = tk.StringVar()    # 这时文字变量储存器
l = tk.Label(window, 
    textvariable=varq,   # 使用 textvariable 替换 text, 因为这个可以变化
    bg='green', font=('Arial', 12))
    #width=15, height=5)
l.pack(pady=20) 
#pack包含('出現位置','text','background','字體&大小','width','heigh')
def hit_me():
    global on_hit
    if on_hit == False:     # 从 False 状态变成 True 状态
        on_hit = True
        varq.set('you hit me')   # 设置标签的文字为 'you hit me'
    else:       # 从 True 状态变成 False 状态
        on_hit = False
        varq.set('') # 设置 文字为空
        
b = tk.Button(window, 
    text='hit me',      # 显示在按钮上的文字
    width=15, height=2, 
    command=hit_me)     # 点击按钮式执行的命令
b.pack()    # 按钮位置

on_hit = False  # 默认初始状态为 False




''''''
#列表
var1=tk.StringVar()
l=tk.Label(window,bg='yellow',width=10,textvariable=var1)
l.pack()

var2 = tk.StringVar()
var2.set((11,22,33,44)) #为变量设置值

#创建Listbox

lb = tk.Listbox(window, listvariable=var2)  #将var2的值赋给Listbox

#创建一个list并将值循环添加到Listbox控件中
list_items = [1,2,3,4]
for item in list_items:
    lb.insert('end', item)  #从最后一个位置开始加入值
lb.insert(1, 'first')       #在第一个位置加入'first'字符
lb.delete(5)
lb.pack()

def print_selection():
    value=lb.get(lb.curselection())
    var1.set(value)


chk= False
def check():
    global chk
    if chk == False:     # 从 False 状态变成 True 状态
        chk = True
        lb.insert(2, 'second') 
           
    else:       
        chk = False
        lb.delete(2) 
        
b1 = tk.Button(window, 
    text='hit me2',    
    bg='gray',# 显示在按钮上的文字
    width=15, height=2, 
    command=print_selection)     # 点击按钮式执行的命令
b1.pack() 

b13 = tk.Button(window, 
    text='hit me3',      # 显示在按钮上的文字
    width=15, height=2, 
    command=check)     # 点击按钮式执行的命令
b13.pack() 



#選項
var = tk.StringVar()
choice_box = tk.Label(window, bg='yellow', width=20, text='empty')
choice_box.pack()

def print_selectio():
    choice_box.config(text='you have selected ' + var.get())
    
r1 = tk.Radiobutton(window, text='Option A',
                    variable=var, value='A',
                    command=print_selectio)

r2 = tk.Radiobutton(window, text='Option B',
                    variable=var, value='B',
                    command=print_selectio)
r4 = tk.Radiobutton(window, text='Option D',
                    variable=var, value='D',
                    command=print_selectio)

r3 = tk.Radiobutton(window, text='Option C',
                    variable=var, value='C',
                    command=check)
r1.pack()
r2.pack()
r3.pack()
r4.pack()


#滾軸
roll = tk.Label(window, bg='yellow', width=20, text='empty')
roll.pack()
roll2 = tk.Label(window, bg='yellow', width=20, text='empty')
roll2.pack()
def print_selecti(strin):
    roll.config(text="you have selected "+ strin)
    roll2.config(text='you have selected ' + strin)
    #print(type(strin))
    
s = tk.Scale(window, label='try me', from_=1, to=10, orient=tk.HORIZONTAL,
             length=300, showvalue=1, tickinterval=1, resolution=0.2, command=print_selecti)
s.pack()
#勾選選項
choose = tk.Label(window, bg='yellow', width=20, text='empty')
choose.pack()
def print_select():
    if (var4.get() == 1) & (var5.get() == 0):   #如果选中第一个选项，未选中第二个选项
        choose.config(text='I love only Python ')
    elif (var4.get() == 0) & (var5.get() == 1): #如果选中第二个选项，未选中第一个选项
        choose.config(text='I love only C++')
    elif (var4.get() == 0) & (var5.get() == 0):  #如果两个选项都未选中
        choose.config(text='I do not love either')
    else:
        choose.config(text='I love both')             #如果两个选项都选中

var4 = tk.IntVar()
var5= tk.IntVar()
c1 = tk.Checkbutton(window, text='Python', variable=var4, onvalue=1, offvalue=0,
                    command=print_select)
c2 = tk.Checkbutton(window, text='C++', variable=var5, onvalue=1, offvalue=0,
                    command=print_select)
c1.pack()
c2.pack()
counter = 0
def do_job():
    global counter
    l.config(text='do '+ str(counter))
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
filemenu.add_command(label='Save', command=do_job)##同样的在`File`中加入`Save`小菜单

filemenu.add_separator()##这里就是一条分割线

##同样的在`File`中加入`Exit`小菜单,此处对应命令为`window.quit`
filemenu.add_command(label='Exit', command=window.quit)
submenu = tk.Menu(filemenu)##和上面定义菜单一样，不过此处实在`File`上创建一个空的菜单
filemenu.add_cascade(label='Import', menu=submenu, underline=0)##给放入的菜单`submenu`命名为`Import`
submenu.add_command(label="Submenu1", command=do_job)##这里和上面也一样，在`Import`中加入一个小菜单命令`Submenu1`

window.config(menu=menubar)





# 運行主程式
window.mainloop()
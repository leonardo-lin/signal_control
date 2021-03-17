# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 15:09:31 2021

@author: leo
"""
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLineEdit, QMessageBox)
from PyQt5.QtCore import QCoreApplication
#from ewq import MyWidget
class MyWidge(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
    
      
    def initUI(self):
        self.setWindowTitle('Button example')
        #change the GUI size here
        self.setGeometry(200, 50, 600, 600)

        """self.btn = QPushButton('Button', self)
        self.btn.move(10, 10)
        self.btn.clicked.connect(self.onClick)"""
        #type the IP in s
        s="aaaaaa"
        #it is used to get IP
        import socket

        def getIP():        
          myname = socket.getfqdn(socket.gethostname())        
          get_s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)        
          get_s.connect(('8.8.8.8', 0))       
          ip = ('hostname: %s, localIP: %s') % (myname, get_s.getsockname()[0])      
          return ip

        def use_here():
            print(s)
            textbox.setText(s)
            """"""
            
        btn_quit = QPushButton('print',self)
        btn_quit.move(10, 50)
        btn_quit.clicked.connect(use_here)
        s=getIP()
        """self.textbox = QLineEdit(self)
        self.textbox.move(10, 90)
        self.textbox.resize(160, 30)"""
        textbox = QLineEdit(self)
        textbox.move(10, 200)
        textbox.resize(500, 50)

        self.show()
    def onClick(self):
        buttonReply = QMessageBox.question(self, 'Message', "input your ip on the upper textbox to connect to server",
             )
        if buttonReply == QMessageBox.Yes:
            print('zconnecting')
            self.textbox.setText("connecting")
        else:
            print('No clicked.')
            self.textbox.setText("No clicked.")
   
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = MyWidge()
    sys.exit(app.exec_())
    
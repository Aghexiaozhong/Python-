#!/usr/bin/python3
# -*- coding:utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication,QWidget

if __name__ == '__main__':
    #每一pyqt5应用程序都必须创建一个应用程序对象，
    #sys.argv参数是一个列表，从命令行输入参数
    app = QApplication(sys.argv)
    
    #QWidget部件是pyqt5所有用户界面面向对象的基类
    #为QWidget函数提供默认构造函数（没有父类）
    w = QWidget()
    
    #w.resize() 用来调整窗口的大小，这里是250px 宽 150px高
    w.resize(250,150)
    
    #move() 方法移动窗口在p屏幕上的位置到x=300,y=300坐标
    w.move(300,300)
    
    #设置窗口标题
    w.setWindowTitle('钟哥')
    
    #显示在屏幕上
    w.show()

    sys.exit(app.exec_())






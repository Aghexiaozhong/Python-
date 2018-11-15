#!/usr/bin/python3
# -*- coding:utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget,QPushButtion,QLineEdit,QLabel, \
QVBoxLayout,QHBoxLayout,QApplication


class LoginWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        userLabel = QLabel('用户名:')
        userLabel.setFixedWidth(38)
        passWordLabel = QLabel('密码:')
        passWordLabel.setFixedWidth(38)
        self.userLineEdit = QLineEdit()
        self.passWordLineEdit = QLineEdit()
        self.passWordLineEdit.setEchoMode(QLineEdit)
        














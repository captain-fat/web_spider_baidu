# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\python_project\web_spider_baidu\main_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.text_inputbox = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.text_inputbox.setGeometry(QtCore.QRect(90, 50, 401, 101))
        self.text_inputbox.setObjectName("text_inputbox")
        self.btn_start = QtWidgets.QPushButton(self.centralwidget)
        self.btn_start.setGeometry(QtCore.QRect(580, 50, 93, 101))
        self.btn_start.setObjectName("btn_start")
        self.text_outputbox = QtWidgets.QTextBrowser(self.centralwidget)
        self.text_outputbox.setGeometry(QtCore.QRect(80, 210, 601, 301))
        self.text_outputbox.setObjectName("text_outputbox")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_start.setText(_translate("MainWindow", "Start"))

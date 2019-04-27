# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'record.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(550, 469)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 130, 72, 15))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(190, 150, 231, 101))
        self.label_2.setObjectName("label_2")
        self.Btn_R = QtWidgets.QPushButton(self.centralwidget)
        self.Btn_R.setGeometry(QtCore.QRect(180, 250, 211, 101))
        self.Btn_R.setText("")
        self.Btn_R.setObjectName("Btn_R")
        self.Btn1 = QtWidgets.QPushButton(self.centralwidget)
        self.Btn1.setGeometry(QtCore.QRect(22, 31, 41, 28))
        self.Btn1.setText("")
        self.Btn1.setObjectName("Btn1")
        self.Btn2 = QtWidgets.QPushButton(self.centralwidget)
        self.Btn2.setGeometry(QtCore.QRect(70, 31, 41, 28))
        self.Btn2.setText("")
        self.Btn2.setObjectName("Btn2")
        self.Btn3 = QtWidgets.QPushButton(self.centralwidget)
        self.Btn3.setGeometry(QtCore.QRect(118, 31, 41, 28))
        self.Btn3.setText("")
        self.Btn3.setObjectName("Btn3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 550, 26))
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
        self.label.setText(_translate("MainWindow", "语音识别"))
        self.label_2.setText(_translate("MainWindow", "点击下面的按钮开始录制音频\n"
"再次点击停止录音开始识别"))


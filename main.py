#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/26 19:55
# @Author  : SeniorZhu1994
# @Email   : SeniorZhu1994@foxmail.com
# @Site    :
# @File    : call_record.py
# @Software: PyCharm

import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor, QPalette, QColor
import qtawesome

from record import Ui_MainWindow


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        # Python3中的继承只用一个super()就可以了，继承后初始化父类的属性
        super().__init__(parent)
        self.setupUi(self)
        self.ui_custom()
        self.init()

    def ui_custom(self):
        self.Btn_Close.setGeometry(QtCore.QRect(30, 20, 30, 30))
        self.Btn_Close.setToolTip("关闭窗口")

        self.Btn_Min.setGeometry(QtCore.QRect(80, 20, 30, 30))
        self.Btn_Min.setToolTip("最小化")

        self.Btn_Max_Nor.setGeometry(QtCore.QRect(130, 20, 30, 30))
        self.Btn_Max_Nor.setToolTip("最大化")

        self.Btn_R.setGeometry(QtCore.QRect(190, 250, 101, 71))
        self.label.setGeometry(QtCore.QRect(80, 60, 351, 70))
        self.label_2.setGeometry(QtCore.QRect(80, 130, 351, 91))

        # 设置窗口透明度，隐藏原始边框
        self.setWindowOpacity(0.9)  # 设置窗口透明度
        # Ui_MainWindow3.setAttribute(QtCore.Qt.WA_TranslucentBackground) #
        # 设置窗口背景透明
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        pe = QPalette()
        self.setAutoFillBackground(True)
        pe.setColor(QPalette.Window, Qt.lightGray)  # 设置背景色

        # 设置标题和图标
        self.setPalette(pe)
        self.setWindowTitle("语音识别")
        spin_icon = qtawesome.icon('fa5s.microphone-alt', color='black')
        # self.pushButton.setIcon(spin_icon)#设置图标
        self.setWindowIcon(spin_icon)

        # 美化左上角的三个按钮。美化的效果就是圆形，红
        # 黄
        # 绿色
        # 悬停时颜色会加深。
        self.Btn_Close.setStyleSheet('''QPushButton{background:#F76677;border-radius:15px;}
        QPushButton:hover{background:red;}''')
        self.Btn_Min.setStyleSheet('''QPushButton{background:#F7D674;border-radius:15px;}
        QPushButton:hover{background:yellow;}''')
        self.Btn_Max_Nor.setStyleSheet('''QPushButton{background:#6DDF6D;border-radius:15px;}
        QPushButton:hover{background:green;}''')

        # 美化中间靠上的label
        self.label.setStyleSheet(
            '''QLabel{color:white;font-size:40px;font-family:Roman times;}''')
        # 美化中间的label
        self.label_2.setStyleSheet('''QLabel{color:darkGray;background:white;border:2px solid #F3F3F5;border-radius:45px;
                        font-size:14pt; font-weight:400;font-family: Roman times;} ''')

        # 对于label的设置还有
        # 使字体居中显示。
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label.setAlignment(Qt.AlignCenter)

        # 最下面的按钮美化
        spin_icon = qtawesome.icon('fa5s.microphone-alt', color='white')
        self.Btn_R.setIcon(spin_icon)  # 设置图标
        self.Btn_R.setIconSize(QtCore.QSize(50, 50))
        self.Btn_R.setStyleSheet('''QPushButton{border:none;}
        QPushButton:hover{color:white;
                    border:2px solid #F3F3F5;
                    border-radius:35px;
                    background:darkGray;}''')

    def init(self):
        self.m_drag = False
        self.max_flag = True
        self.Btn_Close.clicked.connect(self.close)
        self.Btn_Min.clicked.connect(self.showMinimized)
        self.Btn_Max_Nor.clicked.connect(self.Max_or_Nor)

    def Max_or_Nor(self):
        if self.max_flag == True:
            self.showMaximized()
            self.max_flag = False
            self.Btn_Max_Nor.setToolTip("恢复")
        else:
            self.showNormal()
            self.max_flag = True
            self.Btn_Max_Nor.setToolTip("最大化")

    # 重写三个方法使我们的Example窗口支持拖动,上面参数window就是拖动对象
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_drag = True
            self.m_DragPosition = event.globalPos() - self.pos()
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_drag:
            self.move(QMouseEvent.globalPos() - self.m_DragPosition)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_drag = False
        self.setCursor(QCursor(Qt.ArrowCursor))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())

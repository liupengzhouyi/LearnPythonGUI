# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Test.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPainter, QColor, QPixmap
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QHBoxLayout
from PyQt5 import QtQuickWidgets
from 手写数字界面.MyFuncation import getN


class Canvas(QLabel):
    def __init__(self):
        super().__init__()

        self.paly()
        self.last_x, self.last_y = None, None
        self.pen_color = QColor('#000')

    def paly(self):
        self.canvas = QPixmap(320, 320)
        self.canvas.fill(QColor('white'))
        self.setPixmap(self.canvas)

    def GetContentAsQImage(self):
        # self.canvas = canvas.resize((28, 28), canvas.ANTIALIAS)  # 将截图转换成 28 * 28 像素
        image = self.canvas.toImage()
        return image

    def set_pen_color(self, c):
        self.pen_color = QColor(c)

    def mouseReleaseEvent(self, *args, **kwargs):
        """
        松开鼠标事件
        """
        self.last_x, self.last_y = None, None

    def mouseMoveEvent(self, e):
        """
        移动鼠标事件
        """
        if self.last_x is None:
            self.last_x = e.x()
            self.last_y = e.y()
            return

        painter = QPainter(self.pixmap())
        pen = painter.pen()
        pen.setWidth(18)
        pen.setColor(self.pen_color)
        painter.setPen(pen)
        painter.drawLine(self.last_x, self.last_y, e.x(), e.y())
        painter.end()
        self.update()

        # update the origin for next time
        self.last_x = e.x()
        self.last_y = e.y()

        image = self.canvas.toImage()
        image.save('paly.png', 'png', image.Format_RGB888)



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 514)
        MainWindow.setStyleSheet("MainWindow{background-color: yellow}")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 151, 51))

        font = QtGui.QFont()
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setObjectName("label")


        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(672, 360, 111, 51))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(672, 310, 111, 51))
        self.pushButton_2.setObjectName("pushButton_2")

        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(50, 50, 370, 370))
        self.widget.setObjectName("widget")

        self.createQuickWidget()

        self.pushButton_2.clicked.connect(lambda : self.resetLabet1())

        self.pushButton.clicked.connect(lambda : self.saveImage())

        self.widget.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "手写数字"))
        self.label.setText(_translate("MainWindow", "Welcome"))
        self.pushButton.setText(_translate("MainWindow", "识别"))
        self.pushButton_2.setText(_translate("MainWindow", "清除"))

    def resetLabet0(self):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("MainWindow", "666"))

    def resetLabet1(self):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("MainWindow", "Welcome"))
        self.canvas.paly()

    def createQuickWidget(self):
        self.quickWidget = QtQuickWidgets.QQuickWidget(self.widget)
        self.quickWidget.setGeometry(QtCore.QRect(50, 50, 370, 370))
        self.quickWidget.setResizeMode(QtQuickWidgets.QQuickWidget.SizeRootObjectToView)
        self.quickWidget.setObjectName("quickWidget")
        self.canvas = Canvas()
        vlayout = QVBoxLayout()
        self.quickWidget.setLayout(vlayout)
        vlayout.addWidget(self.canvas)
        palette = QHBoxLayout()
        vlayout.addLayout(palette)

    def saveImage(self):
        image = self.canvas.canvas.toImage()
        # image.save('paly.png', 'png', image.Format_RGB888)

        # image = image.resize((28, 28), image.ANTIALIAS)  # 将截图转换成 28 * 28 像素
        image = image.scaled(28, 28)

        # myimage = image.convert('L')  # 转换成灰度图

        tv = list(image)  # 获取图片像素值
        print(tv)
        tva = [(255 - x) * 1.0 / 255.0 for x in tv]  # 转换像素范围到[0 1], 0是纯白 1是纯黑
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("MainWindow", getN(tva)))


    # def doImageColor(self, image):
    #
    #     return iGray



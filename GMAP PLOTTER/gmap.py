# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1059, 839)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(10, 10, 1041, 821))
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.frame = QtWidgets.QFrame(self.widget)
        self.frame.setGeometry(QtCore.QRect(10, 20, 1011, 791))
        self.frame.setStyleSheet("background-color: rgb(16, 0, 49);\n"
"border-top-left-radius:50px;\n"
"border-bottom-right-radius:50px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 1011, 791))
        self.frame_2.setStyleSheet("QFrame#frame_2{\n"
"background-color: rgba(106, 67, 99,100);\n"
"border-top-left-radius:50px;\n"
"border-bottom-right-radius:50px;\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(970, 10, 30, 30))
        self.pushButton.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton.setStyleSheet("QPushButton{\n"
"border-radius:15px;\n"
"background-color: rgb(194, 65, 0);\n"
"}\n"
"QPushButton:Hover{\n"
"background-color: rgb(194, 65, 0,120);\n"
"}")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setGeometry(QtCore.QRect(930, 10, 30, 30))
        self.pushButton_2.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_2.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"border-radius:15px;\n"
"background-color: rgb(0, 170, 127);\n"
"}\n"
"QPushButton:Hover{\n"
"background-color: rgba(0, 170, 127,120);\n"
"}")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_3.setGeometry(QtCore.QRect(890, 10, 30, 30))
        self.pushButton_3.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_3.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"border-radius:15px;\n"
"background-color: rgb(53, 106, 159);\n"
"}\n"
"QPushButton:Hover{\n"
"background-color: rgba(53, 106, 159,120);\n"
"}")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.map_plot = QWebView(self.frame_2)
        self.map_plot.setGeometry(QtCore.QRect(10, 100, 991, 651))
        self.map_plot.setStyleSheet("QWidget{\n"
"border:1px solid rgba(145,145,145,255);\n"
"background-color: rgba(0,0,0,0);\n"
"border-top-left-radius:0px;\n"
"border-bottom-right-radius:0px;\n"
"}")
        self.map_plot.setObjectName("map_plot")
        self.map_plot.load(QtCore.QUrl("https://www.google.com/maps"))
        self.map_plot.show()

        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(180, 10, 681, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("background:None;\n"
"color:rgba(145,145,145,255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(190, 760, 681, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background:None;\n"
"color:rgba(145,145,145,255);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QtCore.QRect(10, 61, 421, 31))
        self.lineEdit.setStyleSheet(u"color:#fff;")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.pushButton_4 =QtWidgets.QPushButton(self.frame_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QtCore.QRect(870, 60, 121, 30))
        self.pushButton_4.setStyleSheet(u"QPushButton{\n"
"color:rgb(220,220,220);\n"
"border-radius:15px;\n"
"background-color: rgb(53, 106, 159,120);\n"
"}\n"
"QPushButton:Hover{\n"
"background-color: rgba(53, 106, 159);\n"
"}")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QtCore.QRect(440, 60, 421, 31))
        self.lineEdit_2.setStyleSheet(u"color:#fff;")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "GMAP PLOTTER"))
        self.label_2.setText(_translate("Form", "Copyright©2021,Sihab Sahariar"))
        self.lineEdit.setPlaceholderText(_translate("Form", u"Longitude", None))
        self.pushButton_4.setText(_translate("Form", u"GO", None))
        self.lineEdit_2.setPlaceholderText(_translate("Form", u"Latitude", None))



class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.center()
        self.oldPos = self.pos()
        self.ui.pushButton.clicked.connect(self.closeWindow)
        self.ui.pushButton_2.clicked.connect(self.hideWindow)
        self.ui.pushButton_4.clicked.connect(self.Map_search)
    # Center the screen
    def center(self):
        ref = self.frameGeometry()
        place = QtWidgets.QDesktopWidget().availableGeometry().center()
        ref.moveCenter(place)
        self.move(ref.topLeft())

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QtCore.QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    def hideWindow(self):
        self.showMinimized()

    # Close window
    def closeWindow(self):
        self.close()
    def Map_search(self):
        Longitude = self.ui.lineEdit.text().rstrip()
        Latitude = self.ui.lineEdit_2.text().lstrip()
        
        condition_check = Longitude != '' and Latitude != ''
        if condition_check:
            # URL="https://www.google.com/maps/@"+
            # Latitude+","
            # +Longitude+",9z"
            #https://www.google.com/maps/place/23%C2%B010'24.4%22N+81%C2%B056'10.2%22E/@23.1734515,81.9339634
            Url = QtCore.QUrl(f'https://www.google.com/maps/place/{Latitude}+{Longitude}')
            #print("url is :",Url)
            browser = self.ui.map_plot
            browser.load(Url)

import sys
from PyQt5.QtWebEngineWidgets import QWebEngineView as QWebView,QWebEnginePage as QWebPage
from PyQt5.QtWebEngineWidgets import QWebEngineSettings as QWebSettings
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()

    sys.exit(app.exec_())
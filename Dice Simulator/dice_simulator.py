from PyQt5 import QtCore, QtGui, QtWidgets
import random

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(382, 428)
        Form.setWindowTitle("Random Dice Simulator")
        Form.setStyleSheet("background-color:#0091D5;")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, -10, 381, 91))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/dice-none.png"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(0, 70, 381, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:#fff;\n"
"background:transparent;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.dice = QtWidgets.QLabel(Form)
        self.dice.setGeometry(QtCore.QRect(10, 120, 361, 131))
        self.dice.setStyleSheet("border: 1px solid rgba(57,57,57,200);")
        self.dice.setText("")
        self.dice.setPixmap(QtGui.QPixmap("img/dice-1.png"))
        self.dice.setScaledContents(False)
        self.dice.setAlignment(QtCore.Qt.AlignCenter)
        self.dice.setObjectName("dice")
        self.lcdNumber = QtWidgets.QLCDNumber(Form)
        self.lcdNumber.setGeometry(QtCore.QRect(150, 260, 221, 51))
        self.lcdNumber.setStyleSheet("border:None;\n"
"color:#23282D;")
        self.lcdNumber.setObjectName("lcdNumber")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 260, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:#fff;\n"
"background:transparent;")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(160, 320, 70, 70))
        self.pushButton.setStyleSheet("QPushButton#pushButton{\n"
"background:transparent;\n"
"border:None;\n"
"}\n"
"QPushButton#pushButton:Hover{\n"
"padding-top:5px;\n"
"image-position:top;\n"
"}")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/reset.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(64, 64))
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(10, 400, 361, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgba(255,255,255,200);\n"
"background:transparent;")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(10, 400, 361, 3))
        self.line.setStyleSheet("")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pushButton.clicked.connect(self.RandomDice)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        self.label_2.setText(_translate("Form", "Dice Simulator"))
        self.label_3.setText(_translate("Form", "Dice Digit :"))
        self.label_4.setText(_translate("Form", "Developed By Sihab Sahariar"))

    def RandomDice(self, Form):
    	list_dice = [1,2,3,4,5,6]
    	random.shuffle(list_dice)
    	x = random.choice(list_dice)
    	self.dice.setPixmap(QtGui.QPixmap(f"img/dice-{x}.png"))
    	self.lcdNumber.display(x)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())


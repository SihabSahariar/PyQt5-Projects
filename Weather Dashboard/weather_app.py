from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QMovie
from datetime import datetime
import requests
import random

class Ui_WeatherApp(object):
    def setupUi(self, WeatherApp):
        bg_img = random.randint(1,8)
        WeatherApp.setObjectName("Weather Dashboard")
        WeatherApp.resize(520, 600)
        WeatherApp.setMaximumSize(QtCore.QSize(520, 600))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        WeatherApp.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        WeatherApp.setWindowIcon(icon)
        WeatherApp.setStyleSheet("background-image : url(\"bg/a%d.jpg\")"%bg_img)
        WeatherApp.setIconSize(QtCore.QSize(35, 35))
        self.centralwidget = QtWidgets.QWidget(WeatherApp)
        self.centralwidget.setObjectName("centralwidget")
        self.heading = QtWidgets.QLabel(self.centralwidget)
        self.heading.setGeometry(QtCore.QRect(10, 10, 361, 31))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.heading.setFont(font)
        self.heading.setAutoFillBackground(False)
        self.heading.setStyleSheet("color : white;\n"
"background : transparent;")
        self.heading.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.heading.setFrameShadow(QtWidgets.QFrame.Plain)
        self.heading.setObjectName("heading")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(110, 50, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setStyleSheet("border: 2px solid rgb(91, 101, 124);\n")
        self.lineEdit.setText("")
        self.lineEdit.setFrame(True)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.search_btn = QtWidgets.QPushButton(self.centralwidget)
        self.search_btn.setGeometry(QtCore.QRect(200, 110, 111, 41))
        self.search_btn.setStyleSheet("color : white;")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.search_btn.setFont(font)
        self.search_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.search_btn.setObjectName("search_btn")
        self.city_label = QtWidgets.QLabel(self.centralwidget)
        self.city_label.setGeometry(QtCore.QRect(100, 160, 321, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.city_label.setFont(font)
        self.city_label.setStyleSheet("color : white;\n"
"background : transparent;")
        self.city_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.city_label.setText("")
        self.city_label.setAlignment(QtCore.Qt.AlignCenter)
        self.city_label.setObjectName("city_label")
        self.time_label = QtWidgets.QLabel(self.centralwidget)
        self.time_label.setGeometry(QtCore.QRect(100, 200, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.time_label.setFont(font)
        self.time_label.setAutoFillBackground(False)
        self.time_label.setStyleSheet("color : white;\n"
"background : transparent;")
        self.time_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.time_label.setText("")
        self.time_label.setAlignment(QtCore.Qt.AlignCenter)
        self.time_label.setObjectName("time_label")
        self.image_label = QtWidgets.QLabel(self.centralwidget)
        self.image_label.setGeometry(QtCore.QRect(150, 240, 221, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.image_label.setFont(font)
        self.image_label.setStyleSheet("color : white;\n"
"background : transparent;")
        self.image_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.image_label.setText("")
        self.image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.image_label.setObjectName("image_label")
        self.temp_label = QtWidgets.QLabel(self.centralwidget)
        self.temp_label.setGeometry(QtCore.QRect(149, 310, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.temp_label.setFont(font)
        self.temp_label.setStyleSheet("color : white;\n"
"background : transparent;")
        self.temp_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.temp_label.setText("")
        self.temp_label.setAlignment(QtCore.Qt.AlignCenter)
        self.temp_label.setObjectName("temp_label")
        self.weather_label = QtWidgets.QLabel(self.centralwidget)
        self.weather_label.setGeometry(QtCore.QRect(150, 360, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.weather_label.setFont(font)
        self.weather_label.setStyleSheet("color : white;\n"
"background : transparent;")
        self.weather_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.weather_label.setText("")
        self.weather_label.setAlignment(QtCore.Qt.AlignCenter)
        self.weather_label.setObjectName("weather_label")
        self.cloud_label = QtWidgets.QLabel(self.centralwidget)
        self.cloud_label.setEnabled(True)
        self.cloud_label.setGeometry(QtCore.QRect(150, 410, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cloud_label.setFont(font)
        self.cloud_label.setStyleSheet("color : white;\n"
"background : transparent;")
        self.cloud_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.cloud_label.setText("")
        self.cloud_label.setAlignment(QtCore.Qt.AlignCenter)
        self.cloud_label.setObjectName("cloud_label")
        self.humidity_label = QtWidgets.QLabel(self.centralwidget)
        self.humidity_label.setGeometry(QtCore.QRect(150, 450, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.humidity_label.setFont(font)
        self.humidity_label.setStyleSheet("color : white;\n"
"background : transparent;")
        self.humidity_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.humidity_label.setText("")
        self.humidity_label.setAlignment(QtCore.Qt.AlignCenter)
        self.humidity_label.setObjectName("humidity_label")
        self.wind_label = QtWidgets.QLabel(self.centralwidget)
        self.wind_label.setGeometry(QtCore.QRect(150, 490, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.wind_label.setFont(font)
        self.wind_label.setStyleSheet("color : white;\n"
"background : transparent;")
        self.wind_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.wind_label.setText("")
        self.wind_label.setAlignment(QtCore.Qt.AlignCenter)
        self.wind_label.setObjectName("wind_label")
        self.visibility_label = QtWidgets.QLabel(self.centralwidget)
        self.visibility_label.setGeometry(QtCore.QRect(150, 530, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.visibility_label.setFont(font)
        self.visibility_label.setStyleSheet("color : white;\n"
"background : transparent;")
        self.visibility_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.visibility_label.setText("")
        self.visibility_label.setAlignment(QtCore.Qt.AlignCenter)
        self.visibility_label.setObjectName("visibility_label")
        self.c_tag = QtWidgets.QLabel(self.centralwidget)
        self.c_tag.setGeometry(QtCore.QRect(30, 410, 105, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.c_tag.setFont(font)
        self.c_tag.setStyleSheet("color : white;\n"
"background : transparent;")
        self.c_tag.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.c_tag.setObjectName("c_tag")
        self.h_tag = QtWidgets.QLabel(self.centralwidget)
        self.h_tag.setGeometry(QtCore.QRect(30, 450, 105, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.h_tag.setFont(font)
        self.h_tag.setStyleSheet("color : white;\n"
"background : transparent;")
        self.h_tag.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.h_tag.setObjectName("h_tag")
        self.w_tag = QtWidgets.QLabel(self.centralwidget)
        self.w_tag.setGeometry(QtCore.QRect(20, 490, 115, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.w_tag.setFont(font)
        self.w_tag.setStyleSheet("color : white;\n"
"background : transparent;")
        self.w_tag.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.w_tag.setObjectName("w_tag")
        self.v_tag = QtWidgets.QLabel(self.centralwidget)
        self.v_tag.setGeometry(QtCore.QRect(25, 530, 115, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.v_tag.setFont(font)
        self.v_tag.setStyleSheet("color : white;\n"
"background : transparent;")
        self.v_tag.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.v_tag.setObjectName("v_tag")
        self.gif_label = QtWidgets.QLabel(self.centralwidget)
        self.gif_label.setGeometry(QtCore.QRect(20, 50, 61, 31))
        self.gif_label.setText("")
        self.gif_label.setObjectName("gif_label")
        self.gif_label.setStyleSheet("background: transparent;")
        WeatherApp.setCentralWidget(self.centralwidget)


        self.retranslateUi(WeatherApp)
        QtCore.QMetaObject.connectSlotsByName(WeatherApp)
        
        gif = QMovie("icons/gif1.gif")
        self.gif_label.setMovie(gif)
        gif.start()
        
        #Search button connection
        self.search_btn.clicked.connect(self.search)

    #program start
        
    def search(self):
        
        city = self.lineEdit.text()
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
        api_key = 'bc7fee6f03cb4ca53abfb383fa32ca02'
        result = requests.get(url.format(city,api_key))
        err_img = QPixmap("icons/invalid_icon.png")
   
        #msg_box
        msg = QMessageBox()
        msg.setWindowTitle("Invalid !")
        msg.setText("Enter another city name")
        msg.setIcon(QMessageBox.Information)
        

        if result:
            json = result.json()
            city = json['name']
            country = json['sys']['country']
            date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
            temp_kelvin = json['main']['temp']
            temp_celcius = temp_kelvin-273.15
            temp_fahrenheit = (temp_kelvin-273.15)*9/5+32
            ico = json['weather'][0]['icon']
            icon = QPixmap("icons/%s.png"%ico)
            climate = json['weather'][0]['main']
            cloudiness= json['clouds']['all']
            humidity = json['main']['humidity']
            wind = json['wind']['speed']*3.6
            visibility=json['visibility']/1000
            
            
            #Printing Statements-
            self.city_label.setText(city + " " + country)
            self.time_label.setText(date_time)
            self.image_label.setPixmap(icon)
            self.temp_label.setText("%d"%temp_celcius+ " °C | " + "%d"%temp_fahrenheit + " °F")
            self.weather_label.setText(climate)
            self.cloud_label.setText("%d"%cloudiness + " %")
            self.humidity_label.setText("%d"%humidity + " %")
            self.wind_label.setText("%.1f"%wind+" KM/H")
            self.visibility_label.setText("%.1f"%visibility+" KM")
            
        else:
           invalid = "Input Correctly"
           self.city_label.setText(invalid)
           self.time_label.setText("")
           self.image_label.setPixmap(err_img)
           self.temp_label.setText("")
           self.weather_label.setText("")
           self.cloud_label.setText("")
           self.humidity_label.setText("")
           self.wind_label.setText("")
           self.visibility_label.setText("")
           msg.exec_()

    def retranslateUi(self, WeatherApp):
        _translate = QtCore.QCoreApplication.translate
        WeatherApp.setWindowTitle(_translate("WeatherApp", "WEATHER DASHBOARD APP"))
        self.heading.setText(_translate("WeatherApp", "CURRENT WEATHER FORECAST..."))
        self.lineEdit.setPlaceholderText(_translate("WeatherApp", "City"))
        self.search_btn.setText(_translate("WeatherApp", "SEARCH"))
        self.search_btn.setShortcut(_translate("WeatherApp", "Return"))
        self.c_tag.setText(_translate("WeatherApp", "CLOUD      :"))
        self.h_tag.setText(_translate("WeatherApp", "HUMIDITY :"))
        self.w_tag.setText(_translate("WeatherApp", "WIND        :"))
        self.v_tag.setText(_translate("WeatherApp", "VISIBILITY :"))
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WeatherApp = QtWidgets.QMainWindow()
    ui = Ui_WeatherApp()
    ui.setupUi(WeatherApp)
    WeatherApp.show()
    sys.exit(app.exec_())


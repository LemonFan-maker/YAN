# -*- coding: utf-8 -*-


#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,QSpinBox
import json, urllib.parse, os, tempfile, random
from qt_material import apply_stylesheet

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(822, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 801, 601))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textBrowser = QtWidgets.QTextBrowser(self.horizontalLayoutWidget)
        self.textBrowser.setObjectName("textBrowser")
        self.horizontalLayout.addWidget(self.textBrowser)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout.addWidget(self.comboBox_2, 2, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 4, 0, 1, 2)
        self.spinBox = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.spinBox.valueChanged.connect(self.changeValue)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout.addWidget(self.spinBox, 3, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.pushButton.clicked.connect(self.clickButton)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "性别"))
        self.label_3.setText(_translate("MainWindow", "类型"))
        self.comboBox.setItemText(0, _translate("MainWindow", "男"))
        self.comboBox.setItemText(1, _translate("MainWindow", "女"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "普通"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "玄幻"))
        self.pushButton.setText(_translate("MainWindow", "生成"))
        self.label_2.setText(_translate("MainWindow", "数量"))        
    
    def changeValue(self):
        times = self.spinBox.value()
        return times

    def clickButton(self):
        for i in range(self.changeValue()):
            self.textBrowser.append(self.read_json())
        self.textBrowser.append("-----")

    def read_json(self):
        fantasy_name_dir = os.getcwd() + "\\core\\RandomName\\fantasy_name.json"

        with open(fantasy_name_dir,'r',encoding='utf-8')as fantasy_name:
            data = fantasy_name.read()
            data = urllib.parse.unquote(data)
            temp_file = tempfile.TemporaryFile('w',encoding='utf-8',delete=False)
            #f = open(temp_file.name, 'w', encoding="utf-8")
            temp_file.write(data)

        with open(temp_file.name,'r',encoding='utf-8') as json_data:
            json_data = json_data.read()
            data = json.loads(json_data, strict=False)
        girl_lastname = list(data['girl_lastname'].replace(",", ""))
        girl_firstname = list(data['girl_firstname'].replace(",", ""))
        girl = list(data['girl_name'].replace(",", ""))    
        
        #random.shuffle(girl_lastname)
        #random.shuffle(girl_firstname)

        font_string = ''
        for i in range(0,random.randint(1,3)):
            font_string+= random.choice(girl_firstname)
        surname = random.choice(girl_lastname)
        name_random = surname+font_string
        result = [girl[i] + girl[i+1] for i in range(0, len(girl), 2)]
        name = random.choice(result)
        name = "".join (name)
        selected_str = random.choice([name, name_random])
        temp_file.close()
        os.remove(temp_file.name)
        return selected_str
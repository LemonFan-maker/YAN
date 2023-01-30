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
import  ctypes

ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("996")
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(830, 610)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 801, 601))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.comboBox_2 = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.gridLayout.addWidget(self.comboBox_2, 1, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.spinBox = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.spinBox.setMaximum(999)
        self.spinBox.valueChanged.connect(self.changeValue) 
        self.spinBox.setObjectName("spinBox")
        self.gridLayout.addWidget(self.spinBox, 3, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 6, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 6, 2, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.horizontalLayoutWidget)
        self.textBrowser.setStyleSheet("QTextBrowser{\n"
"    font-size: 18px;\n"
"    }")
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 2, 2, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.pushButton_2.clicked.connect(self.clean)
        self.pushButton.clicked.connect(self.clickButton)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "玄幻"))
        self.label_2.setText(_translate("MainWindow", "数量"))
        self.label_3.setText(_translate("MainWindow", "类型"))
        self.pushButton_2.setText(_translate("MainWindow", "清空"))
        self.pushButton.setText(_translate("MainWindow", "生成"))
    
    def clean(self):
        self.textBrowser.clear()

    def get_type(self):
        name_type = self.comboBox_2.currentText()
        return name_type

    def changeValue(self):
        times = self.spinBox.value()
        return times

    def clickButton(self):
        types= self.get_type()
        #normal_lastname, double_lastname, boy_firstname, girl_firstname = self.normal_read_json()
        if types == "玄幻": 
            self.textBrowser.append("——————————")
            for i in range(self.changeValue()):
                self.textBrowser.append(self.fantasy_read_json())
            self.textBrowser.append("——————————")
        # else:
        #     mix= self.normal_read_json()
        #     if sex == "女":
        #         for i in range(self.changeValue()):
        #             self.textBrowser.append(mix)
        #         self.textBrowser.append("——————————")
        #     else:
        #         for i in range(self.changeValue()):
        #             self.textBrowser.append(boy_mix)
        #         self.textBrowser.append("——————————")

    def fantasy_read_json(self):
        fantasy_name_dir = os.getcwd() + "\\core\\RandomName\\fantasy_name.json"

        with open(fantasy_name_dir,'r',encoding='utf-8')as fantasy_name:
            data = fantasy_name.read()
            data = urllib.parse.unquote(data)
            
            temp_file = tempfile.TemporaryFile('w',encoding='utf-8',delete=False)
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

    # def normal_read_json(self):
    #     # 读取lastname
    #     normal_last_name_dir = os.getcwd() + "\\core\\RandomName\\last_name.json"
    #     with open(normal_last_name_dir, 'r', encoding='utf-8')as normal_last_name:
    #         normal_last_name = normal_last_name.read()
    #         normal_last_name = urllib.parse.unquote(normal_last_name)

    #         temp_file = tempfile.TemporaryFile('w+', encoding='utf-8', delete=False)
    #         temp_file.write(normal_last_name)
    #         temp_file.seek(0)

    #     with open(temp_file.name, 'r', encoding='utf-8') as json_data:
    #         json_data = json_data.read()
    #         data = json.loads(json_data, strict=False)
    #         normal_lastname = list(data['lastname'].replace(",", ""))
    #         double_lastname = list(data['doub_lastname'].replace(",", ""))
    #         double_lastname = [double_lastname[i] + double_lastname[i+1] for i in range(0, len(double_lastname), 2)]
            
    #     # 读取fistname
    #         normal_first_name_dir = os.getcwd() + "\\core\\RandomName\\first_name.json"
    #     with open(normal_first_name_dir, 'r', encoding='utf-8') as normal_first_name:
    #         normal_first_name = normal_first_name.read()
    #         normal_first_name = urllib.parse.unquote(normal_first_name)

    #         temp_file = tempfile.TemporaryFile('w+', encoding='utf-8',delete=False)
    #         temp_file.write(normal_first_name)
    #         temp_file.seek(0)

    #     with open(temp_file.name, 'r', encoding='utf-8') as json_data:
    #         json_data = json_data.read()
    #         data = json.loads(json_data, strict=False)
    #         boy_firstname = list(data['boy_firstname'].replace(",", ""))
    #         girl_firstname = list(data['girl_firstname'].replace(",", ""))

    #     types, sex = self.get_type()
    #     if sex == "女":
    #         random_girl_firstname = random.choice(girl_firstname)
    #         random_double_lastname = random.choice(double_lastname)
    #         girl_result_double = random.choice(random_double_lastname) + random.choice(random_girl_firstname)
    #         girl_result_normal = random.choice(normal_lastname) + random.choice(random_girl_firstname)
    #         girl_mix = random.choice(girl_result_normal + girl_result_double)
    #         return girl_mix
    #     else:
    #         random_boy_firstname = random.choice(boy_firstname)
    #         random_double_lastname = random.choice(double_lastname)
    #         boy_result_double = random.choice(random_double_lastname) + random.choice(random_boy_firstname)
    #         boy_result_normal = random.choice(normal_lastname) + random.choice(random_boy_firstname)
    #         boy_mix = random.choice(boy_result_normal + boy_result_double)
    #         return boy_mix

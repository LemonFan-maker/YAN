# -*- coding: utf-8 -*-

#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QWidget, QFileDialog, QPushButton, QGridLayout, QApplication, QMainWindow, QMessageBox
from qt_material import apply_stylesheet
from wordcloud import WordCloud
from pyqt5Custom import Toast
import tempfile, os, shutil
from wordcloud import ImageColorGenerator
import numpy as n
from PIL import Image
import ctypes

ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("996")
class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(943, 584)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setTabBarAutoHide(True)
        self.tabWidget.setObjectName("tabWidget")
        self.WordCloud = QtWidgets.QWidget()
        self.WordCloud.setObjectName("WordCloud")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.WordCloud)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser = QtWidgets.QTextBrowser(self.WordCloud)
        self.textBrowser.setStyleSheet("QTextBrowser{\n"
"    font-size:18px;\n"
"    }")
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.gridLayout_2.addLayout(self.verticalLayout, 1, 1, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_Open = QtWidgets.QPushButton(self.WordCloud)
        self.pushButton_Open.setObjectName("pushButton_Open")
        self.gridLayout.addWidget(self.pushButton_Open, 0, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.pushButton_Save = QtWidgets.QPushButton(self.WordCloud)
        self.pushButton_Save.setObjectName("pushButton_Save")
        self.gridLayout.addWidget(self.pushButton_Save, 2, 0, 1, 1)
        self.pushButton_Exit = QtWidgets.QPushButton(self.WordCloud)
        self.pushButton_Exit.setObjectName("pushButton_Exit")
        self.gridLayout.addWidget(self.pushButton_Exit, 4, 0, 1, 1)
        self.pushButton_View = QtWidgets.QPushButton(self.WordCloud)
        self.pushButton_View.setObjectName("pushButton_View")
        self.gridLayout.addWidget(self.pushButton_View, 1, 0, 1, 1)
        self.pushButton_Clear = QtWidgets.QPushButton(self.WordCloud)
        self.pushButton_Clear.setObjectName("pushButton_Clear")
        self.gridLayout.addWidget(self.pushButton_Clear, 3, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.tabWidget.addTab(self.WordCloud, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # 绑定事件槽
        self.pushButton_Open.clicked.connect(self.Open)
        self.pushButton_Exit.clicked.connect(QCoreApplication.instance().quit)
        self.pushButton_Clear.clicked.connect(self.Clear)
        self.pushButton_View.clicked.connect(self.View)
        self.pushButton_Save.clicked.connect(self.Save)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_Open.setText(_translate("MainWindow", "打开本地文件"))
        self.pushButton_Save.setText(_translate("MainWindow", "保存到本地"))
        self.pushButton_Exit.setText(_translate("MainWindow", "退出"))
        self.pushButton_View.setText(_translate("MainWindow", "预览云图"))
        self.pushButton_Clear.setText(_translate("MainWindow", "清空"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.WordCloud), _translate("MainWindow", "词云"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
    
    def Clear(self):
        self.textBrowser.clear()

    def Open(self):
        self.file,fileType = QFileDialog.getOpenFileName(self, 'open file', './', "text files (*.*)")
        if self.file:
            with open(self.file, 'r', encoding='utf-8') as f:
                self.textBrowser.append(f.read())
    
    def Cloud(self):
        bg=n.array(Image.open('core\\Analysis\\assets\\I.png')) #将图片以数组形式输出
        if self.file:
            with open(self.file, 'r', encoding='utf-8') as f:
                data = f.read()
                print(data)
                cloud = WordCloud(font_path=r'assets\WordCloud.ttf',
                                mode='RGBA',
                                mask=bg,
                                repeat=True,
                                background_color='#FFFFFF',
                                random_state=8,
                                scale=2).generate(data)
                ig=ImageColorGenerator(bg) #图片颜色导入
                cloud.recolor(color_func=ig) #重新设置词云图颜色
                temp = tempfile.mkdtemp()
                self.pic = temp + "\\Cloud.png"
                print(self.pic)
                cloud.to_file(self.pic)

    def View(self):
        self.Cloud()
        im = Image.open(self.pic)
        im.show()

    def Save(self):
        try:
            self.pic
        except AttributeError:
            self.Cloud()

        dirs = self.pic
        file= QFileDialog.getExistingDirectory(self, 'save file', './')

        #shutil.copyfileobj(dirs, file, length=8*512)
        print(file)
        if os.path.exists(file+"\\Cloud.png"):
            confirm = QMessageBox.question(self,'覆盖','发现重文件，是否覆盖?',QMessageBox.Yes|QMessageBox.No,QMessageBox.No)
            if confirm == QMessageBox.Yes:
                os.remove(file+"\\Cloud.png")
                shutil.move(dirs, file)
                QMessageBox.about(self,'提示','保存成功,在'+file+"目录下")
            if confirm == QMessageBox.No:
                pass
        else:
            shutil.move(dirs, file)
            QMessageBox.about(self,'提示','保存成功,在'+self.file+"目录下")
        

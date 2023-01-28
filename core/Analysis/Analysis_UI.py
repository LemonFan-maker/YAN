# -*- coding: utf-8 -*-

#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication, pyqtSignal
from PyQt5.QtWidgets import QWidget, QFileDialog, QPushButton, QGridLayout, QApplication, QMainWindow, QFormLayout, QLineEdit
from qt_material import apply_stylesheet
import jieba
from wordcloud import WordCloud
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
        self.pushButton_View = QtWidgets.QPushButton(self.WordCloud)
        self.pushButton_View.setObjectName("pushButton_View")
        self.gridLayout.addWidget(self.pushButton_View, 2, 0, 1, 1)
        self.pushButton_Open = QtWidgets.QPushButton(self.WordCloud)
        self.pushButton_Open.setObjectName("pushButton_Open")
        self.gridLayout.addWidget(self.pushButton_Open, 0, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.pushButton_Save = QtWidgets.QPushButton(self.WordCloud)
        self.pushButton_Save.setObjectName("pushButton_Save")
        self.gridLayout.addWidget(self.pushButton_Save, 3, 0, 1, 1)
        self.pushButton_Exit = QtWidgets.QPushButton(self.WordCloud)
        self.pushButton_Exit.setObjectName("pushButton_Exit")
        self.gridLayout.addWidget(self.pushButton_Exit, 4, 0, 1, 1)
        self.pushButton_Load = QtWidgets.QPushButton(self.WordCloud)
        self.pushButton_Load.setObjectName("pushButton_Load")
        self.gridLayout.addWidget(self.pushButton_Load, 1, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.tabWidget.addTab(self.WordCloud, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # 绑定事件槽
        self.pushButton_Open.clicked.connect(self.Open)
        self.pushButton_Exit.clicked.connect(QCoreApplication.instance().quit)
        # self.pushButton_Load.clicked.connect(self.Load)
        self.pushButton_View.clicked.connect(self.View)
        self.pushButton_Save.clicked.connect(self.Save)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_View.setText(_translate("MainWindow", "预览云图"))
        self.pushButton_Open.setText(_translate("MainWindow", "打开本地文件"))
        self.pushButton_Save.setText(_translate("MainWindow", "保存到本地"))
        self.pushButton_Exit.setText(_translate("MainWindow", "退出"))
        self.pushButton_Load.setText(_translate("MainWindow", "读取当前文件"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.WordCloud), _translate("MainWindow", "词云"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))

    def Open(self):
        self.file,fileType = QFileDialog.getOpenFileName(self, 'open file', './', "all (*.*)")
        if self.file:
            with open(self.file, 'r', encoding='utf-8') as f:
                self.textBrowser.append(f.read())

    def View(self):
        bg=n.array(Image.open('core\\Analysis\\assets\\wallhaven-yj7o2l_1500x907.png')) #将图片以数组形式输出
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
                im = Image.open(self.pic)
                im.show()
    
    def Save(self):
        dirs = self.pic
        file= QFileDialog.getExistingDirectory(self, 'save file', './')
        shutil.move(dirs, file)
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    apply_stylesheet(app, theme="dark_cyan.xml")
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
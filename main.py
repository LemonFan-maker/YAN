from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QApplication, QMainWindow, QSplashScreen
from qt_material import apply_stylesheet
from pyqt5Custom.toast import Toast
import sys, os, time, ctypes

ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("996")
class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1096, 600)
        font = QtGui.QFont()
        font.setFamily("华文细黑")
        font.setPointSize(11)
        MainWindow.setFont(font)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon.fromTheme("accessories-calculator")
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowIcon(QtGui.QIcon("./assets/logo.png"))
        MainWindow.setWindowOpacity(0.90)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 126, 551))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_new = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_new.setObjectName("pushButton_new")
        self.verticalLayout.addWidget(self.pushButton_new)
        self.pushButton_open = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_open.setObjectName("pushButton_open")
        self.verticalLayout.addWidget(self.pushButton_open)
        self.pushButton_save = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_save.setObjectName("pushButton_save")
        self.verticalLayout.addWidget(self.pushButton_save)
        self.pushButton_random = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_random.setObjectName("pushButton_random")
        self.verticalLayout.addWidget(self.pushButton_random)
        self.pushButton_markdown = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_markdown.setObjectName("pushButton_markdown")
        self.verticalLayout.addWidget(self.pushButton_markdown)
        self.pushButton_VSCode = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_VSCode.setObjectName("pushButton_VSCode")
        self.verticalLayout.addWidget(self.pushButton_VSCode)
        self.pushButton_settings = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_settings.setObjectName("pushButton_settings")
        self.verticalLayout.addWidget(self.pushButton_settings)
        self.pushButton_NY = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_NY.setObjectName("pushButton_NY")
        self.verticalLayout.addWidget(self.pushButton_NY)
        self.pushButton_QT = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_QT.setObjectName("pushButton_QT")
        self.verticalLayout.addWidget(self.pushButton_QT)
        self.pushButton_Issue = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_Issue.setObjectName("pushButton_Issue")
        self.verticalLayout.addWidget(self.pushButton_Issue)
        self.pushButton_Update = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_Update.setObjectName("pushButton_Update")
        self.verticalLayout.addWidget(self.pushButton_Update)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.scrollArea, 0, QtCore.Qt.AlignLeft)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(16)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("QTextEdit{\n"
"border-radius: 22px;\n"
"}")
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout.addWidget(self.textEdit)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setObjectName("tableView")
        self.gridLayout.addWidget(self.tableView, 1, 1, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignBottom)
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setObjectName("listView")
        self.gridLayout.addWidget(self.listView, 0, 1, 1, 1, QtCore.Qt.AlignRight)
        self.horizontalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        # 绑定事件槽
        self.pushButton_open.clicked.connect(self.Open)
        self.pushButton_VSCode.clicked.connect(self.CodeX)
        self.pushButton_random.clicked.connect(self.RandomName)
        self.pushButton_save.clicked.connect(self.Save)
        self.pushButton_markdown.clicked.connect(self.MD)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "无 · 言"))
        self.pushButton_new.setText(_translate("MainWindow", "新建项目"))
        self.pushButton_open.setText(_translate("MainWindow", "打开项目"))
        self.pushButton_save.setText(_translate("MainWindow", "保存项目"))
        self.pushButton_random.setText(_translate("MainWindow", "随机生成"))
        self.pushButton_markdown.setText(_translate("MainWindow", "MD编辑器"))
        self.pushButton_VSCode.setText(_translate("MainWindow", "代码编辑器"))
        self.pushButton_settings.setText(_translate("MainWindow", "设置"))
        self.pushButton_NY.setText(_translate("MainWindow", "关于 无·言"))
        self.pushButton_QT.setText(_translate("MainWindow", "关于Qt5"))
        self.pushButton_Issue.setText(_translate("MainWindow", "报告错误"))
        self.pushButton_Update.setText(_translate("MainWindow", "检查新版本"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'新宋体\'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt;\"><br /></p></body></html>"))
    
    def Save(self):
        self.fname, ftype = QFileDialog.getSaveFileName(self, 'save file', './', "ALL (*.*)")
        print(self.fname)
        if self.fname:
            data = self.textEdit.toPlainText()
            if os.path.exists(self.fname):
                pass
                #Toast(self, text="文件已存在")
            else:    
                with open(self.fname, 'w', encoding="utf-8") as fn:
                    fn.write(data)
                    fn.close()

    def Open(self):
        self.file,fileType = QFileDialog.getOpenFileName(self, 'open file', './', "ALL (*.*)")
        if self.file:
            with open(self.file, 'r', encoding='utf-8') as f:
                data = f.read()
                self.textEdit.append(data)


    def CodeX(self):
        data = ' ' + os.getcwd() + '\\' + 'core\\CodeX\\main_codeX.py'
        os.system(r'python'+data)  
    
    def MD(self):
        data = ' ' + os.getcwd() + '\\' + 'core\\MD\\main_markdown.py'
        os.system(r'python'+data)
    
    def RandomName(self):
        data = ' ' + os.getcwd() + '\\' + 'core\\RandomName\\main_RandomName.py'
        os.system(r'python'+data)
class MySplashScreen(QSplashScreen):
    pass

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    splash = MySplashScreen()
    pixmap = QtGui.QPixmap('./assets/loading.png')
    splash.show()
    font = QtGui.QFont('Microsoft JhengHei',18)
    pixmap = pixmap.scaledToWidth(800)
    splash.setPixmap(pixmap)
    splash.showMessage("欢迎!", QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom, QtCore.Qt.white)
    splash.setFont(font)
    time.sleep(3)
    MainWindow = QtWidgets.QMainWindow()
    apply_stylesheet(app ,theme='dark_cyan.xml')
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    splash.finish(ui)
    MainWindow.show()
    sys.exit(app.exec_())
import sys, os
from PyQt5 import QtGui
from PyQt5.QtCore import QStringListModel, QUrl, QJsonValue, pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget, QInputDialog
from PyQt5.QtWebChannel import QWebChannel
from qt_material import apply_stylesheet

from MD_UI import Ui_MainWindow

class AppMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(AppMainWindow, self).__init__(parent)
        self.channel = QWebChannel()
        self.setupUi(self)
        self.set_window_center()
        self.init_config()
        self.load_mdeditor()

    def set_window_center(self):
        """ 设置窗口居中 """
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    # 初始化配置
    def init_config(self):
        """ 初始化配置文件 """
        self.mdEditorWbrowser.page().setWebChannel(self.channel)
        self.channel.registerObject("pythonBridge", self)

    def load_mdeditor(self):
        """ 加载Markdown编辑器 """
        url = os.getcwd() + '\\' + 'core\\MD\\mdeditor\\index.html'
        self.mdEditorWbrowser.load(QUrl.fromLocalFile(url))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    appMainWin = AppMainWindow()
    apply_stylesheet(app, theme="dark_cyan.xml")
    appMainWin.show()
    sys.exit(app.exec_())
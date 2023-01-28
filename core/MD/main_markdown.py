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
        # 实例化QWebChannel
        self.channel = QWebChannel()
        # 初始化ui
        self.setupUi(self)
        # 设置窗口居中显示
        self.set_window_center()
        # 初始化配置
        self.init_config()
        # 加载Markdown编辑器
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
        # 注册Bridge与js交互
        self.mdEditorWbrowser.page().setWebChannel(self.channel)
        self.channel.registerObject("pythonBridge", self)

    def load_mdeditor(self):
        """ 加载Markdown编辑器 """
        url = os.getcwd() + '\\' + 'core\\MD\\mdeditor\\index.html'
        self.mdEditorWbrowser.load(QUrl.fromLocalFile(url))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 初始化
    appMainWin = AppMainWindow()
    # 将窗口控件显示在屏幕上
    appMainWin.show()
    # 程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())
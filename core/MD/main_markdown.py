import sys, os, time, re, json, queue

from PyQt5.QtCore import QStringListModel, QUrl, QJsonValue, pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget, QInputDialog
from PyQt5.QtWebChannel import QWebChannel
from qt_material import apply_stylesheet

from MD_UI import Ui_MainWindow
from threading import Thread

class AppMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(AppMainWindow, self).__init__(parent)
        # 实例化QWebChannel
        self.channel = QWebChannel()
        # 笔记本列表数据model
        self.notebook_list_model = QStringListModel()
        # 笔记本列表数据
        self.notebook_list_data = []
        # 当前选中笔记本索引
        self.current_selected_notebook = None
        # 笔记列表数据model
        self.note_list_model = QStringListModel()
        # 笔记列表数据
        self.note_list_data = []
        # 当前选中笔记索引
        self.current_selected_note = None
        # 基本路径
        self.base_path = os.path.join(
            os.path.expanduser("~"), r".config", "qypt-note")
        # local-data本地数据存放路径
        self.local_data_path = os.path.join(
            os.path.expanduser("~"), r".config", "qypt-note", "local-data")
        # 配置文件路径
        self.config_file_path = os.path.join(
            os.path.expanduser("~"), r".config", "qypt-note", "config.json")
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
        # 基目录
        if not os.path.exists(self.base_path):
            os.makedirs(self.base_path)
        # local-data文件夹不存在则创建
        if not os.path.exists(self.local_data_path):
            os.makedirs(self.local_data_path)

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
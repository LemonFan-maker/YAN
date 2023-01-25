from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QFileDialog, QApplication, QMainWindow, QDesktopWidget, QInputDialog, QMessageBox
from qt_material import apply_stylesheet
import sys, os
import CodeX_UI


class AppMainWindow(QMainWindow, CodeX_UI.Ui_mainWindow):
    def __init__(self, parent=None):
        super(AppMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.load_mdeditor()
        self.set_window_center()

    def set_window_center(self):
        """ 设置窗口居中 """
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def load_mdeditor(self):
        """ 加载CodeX编辑器 """
        url = os.getcwd() + '\\' + 'core\\CodeX\\utils\\index.html'
        self.VSCode.load(QUrl.fromLocalFile(url))

# if __name__=="__main__":
#     app = QApplication(sys.argv)
#     baseW = QtWidgets.QMainWindow()
#     appMainWin = AppMainWindow()
#     apply_stylesheet(app, theme='dark_teal.xml')
#     appMainWin.show()
#     sys.exit(app.exec_())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 初始化
    appMainWin = AppMainWindow()
    apply_stylesheet(app, theme='dark_cyan.xml')
    # 将窗口控件显示在屏幕上
    appMainWin.show()
    # 程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())
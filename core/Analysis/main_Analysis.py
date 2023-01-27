from Analysis_UI import Ui_MainWindow
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QSettings
from qt_material import apply_stylesheet

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    apply_stylesheet(app, theme="dark_cyan.xml")
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
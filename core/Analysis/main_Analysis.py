from Analysis_UI import Ui_MainWindow
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QSettings
from qt_material import apply_stylesheet

settings =QSettings("core\\Settings\\config\\config.ini", QSettings.IniFormat)
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    apply_stylesheet(app, theme=settings.value("Global/Theme"))
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QSettings
from Settings_UI import Ui_Setting
from qt_material import apply_stylesheet

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Setting = QtWidgets.QWidget()
    ui = Ui_Setting()
    apply_stylesheet(app,theme="dark_cyan.xml")
    ui.setupUi(Setting)
    Setting.show()
    sys.exit(app.exec_())  
import os, sys
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox

def save_event(self):
    save_path = r"./apc.txt"
    print(save_path)
    if save_path is not None:
        try:
            with open(file=save_path, mode='a+', encoding='utf-8') as file:
                file.write(self.textEdit.toPlainText())
            print('已保存！')
        except:
            pass
#!/usr/bin/env python
# coding: utf-8

'''
Created on 2013/12/12

@author: dacapo
'''
import sys
from dictionary import DictionaryList
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow
from gui import Ui_MainWindow

class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        # connect myaction_logic to myaction.toggled signal
        #self.pushButton.toggled.connect(self.input_check)
        
        #self.lineEdit.toggled.connect(self.editing_finished)
  
    def editing_finished(self):
        word=self.lineEdit.text()
        self.search(word)
    
    def search(self, word):
        context="dictionary.translate(word)"
        print(context)
    
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = MyMainWindow()
    myapp.show()
    sys.exit(app.exec_())
    
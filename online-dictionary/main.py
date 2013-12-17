#!/usr/bin/env python
# coding: utf-8

'''
Created on 2013/12/12

@author: dacapo
'''
import sys
from Dictionary.DictionaryElement import DictionaryList
from Dictionary.Webster import WebsterDict
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow
from gui import Ui_MainWindow

class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.allDict=DictionaryList()
        try:
            self.allDict.load()
        except FileNotFoundError:
            print("previous file not found")
            self.allDict.insert(WebsterDict())
        
        # connect myaction_logic to myaction.toggled signal
        #self.pushButton.toggled.connect(self.input_check)
        
        #self.lineEdit.toggled.connect(self.editing_finished)
  
    def editing_finished(self):
        word=self.lineEdit.text()
        answer=self.search(word)
        self.setView(str(answer["Merriam-Webster"]))
    
    def search(self, word):
        answer=self.allDict.search(word)
        return answer
        
    def setView(self, text):
        self.webView.setHtml(text)
    
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = MyMainWindow()
    myapp.show()  
    
    sys.exit(app.exec_())
    
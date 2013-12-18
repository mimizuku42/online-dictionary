#!/usr/bin/env python
# coding: utf-8

'''
Created on 2013/12/12

@author: dacapo
'''
import sys
from Dictionaries.DictionaryElement import DictionaryList
from Dictionaries.OnlineDictionaries import WebsterDict, YahooDict
from PyQt5 import QtWebKitWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QListWidgetItem
from Ui.gui import Ui_MainWindow
from Ui.block import Ui_Form
from PyQt5.QtCore import *

class Searcher(QObject):
    update=pyqtSignal(str, str)
    
    def __init__(self, dictionary, word):
        super(Searcher, self).__init__()
        self.dictionary=dictionary
        self.word=word
    def run(self):
        try:
            answer=self.dictionary.search(self.word)
            self.update.emit(self.dictionary.name, answer)
        except AttributeError:
            pass
        


class MyMainWindow(QMainWindow, Ui_MainWindow, QObject):
    search_signal=pyqtSignal(str)
    
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__()
        self.setupUi(self)
        self.allDict=DictionaryList()
#         try:
#             self.allDict.load()
#         except FileNotFoundError:
        print("previous file not found")
        self.allDict.insert(WebsterDict())
        self.allDict.insert(YahooDict())
            
        item=QListWidgetItem(self.listWidget)
        item_widget=Ui_Form()
        item.setSizeHint(item_widget.sizeHint())
        self.listWidget.addItem(item)
        self.listWidget.setItemWidget(item, item_widget)
        self.previous_word=""
        self.searchThreads=[QThread() for i in self.allDict.dictList]
        
        

  
    def editing_finished(self):
        word=self.lineEdit.text()
        if word=="":
            return
        elif self.previous_word==word:
            return
        else:
            self.previous_word=word
            self.search(word)

    def search(self, word):
        self.searchers=[]

        for dictionary in self.allDict.dictList.values():
            self.searchers.append(Searcher(dictionary, word))
            
        for index , searcher in enumerate(self.searchers):
            searcher.update.connect(self.renew_gui)
            searcher.moveToThread(self.searchThreads[index])
            self.searchThreads[index].start()

            self.search_signal.connect(searcher.run)
        
        self.search_signal.emit("fire!!")
    
    def renew_gui(self, name, text):
        print(name)
        #print(text)
    
    
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = MyMainWindow()
    myapp.show()
    
    sys.exit(app.exec_())
    
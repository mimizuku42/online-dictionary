#!/usr/bin/env python
# coding: utf-8

'''
Created on 2013/12/12

@author: dacapo
'''
import sys
from Dictionaries.DictionaryElement import DictionaryList, Dictionary
from Dictionaries.OnlineDictionaries import WebsterDict, YahooDict
from PyQt5 import QtWebKitWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QListWidgetItem
from Ui.gui import Ui_MainWindow
from Ui.block import Ui_Form
from PyQt5.QtCore import *

class Searcher(QObject):
    gui_update_signal=pyqtSignal(str, str)
    def __init__(self, dictionary):
        super(Searcher, self).__init__()
        self.dictionary=dictionary
    def search(self, word):
        text=self.dictionary.search(word)
        self.gui_update_signal.emit(self.dictionary.name, text)

        

class SearchElement:
    def __init__(self, dictionary, gui_update, search_signal):
        self.thread=thread=QThread()
        self.searcher=searcher=Searcher(dictionary)
        
        searcher.gui_update_signal.connect(gui_update)
        search_signal.connect(searcher.search)
        searcher.moveToThread(thread)
        thread.start()
        
        

class MyMainWindow(QMainWindow, Ui_MainWindow, QObject):
    search_signal=pyqtSignal(str)
    
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__()
        self.setupUi(self)
        self.previous_word=""
            
        dictList=[WebsterDict(), YahooDict()]
        self.search_elements=dict()
        
        for dictionary in dictList:
            search_element = SearchElement(dictionary, self.gui_update, self.search_signal)
            self.search_elements[dictionary.name] = search_element
         
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
        self.search_signal.emit(word)
    
    def gui_update(self, name, text):
        print(name)
        #print(text)
    
    
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = MyMainWindow()
    myapp.show()
    
    sys.exit(app.exec_())
    
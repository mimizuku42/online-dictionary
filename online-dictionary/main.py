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
            print("success"+str(self))
        except AttributeError:
            print("fail"+str(self))
        


class MyMainWindow(QMainWindow, Ui_MainWindow, QObject):
    signal=pyqtSignal(str)
    
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__()
        self.setupUi(self)
        self.allDict=DictionaryList()
        try:
            self.allDict.load()
        except FileNotFoundError:
            print("previous file not found")
            self.allDict.insert(WebsterDict())
            self.allDict.insert(YahooDict())
            
        item=QListWidgetItem(self.listWidget)
        item_widget=Ui_Form()
        item.setSizeHint(item_widget.sizeHint())
        self.listWidget.addItem(item)
        self.listWidget.setItemWidget(item, item_widget)
        self.previous_word=""
        
        self.searchThreads=[]
        for dictionary in self.allDict.dictList:
            self.searchThreads.append(QThread())
        

        
        
        
        # connect myaction_logic to myaction.toggled signal
        #self.pushButton.toggled.connect(self.input_check)
        
        #self.lineEdit.toggled.connect(self.editing_finished)
  
    def editing_finished(self):
        word=self.lineEdit.text()
        if word=="":
            return
        elif self.previous_word==word:
            return
        else:
            self.previous_word=word
        
        self.searchers=[]

        for dictionary in self.allDict.dictList.values():
            self.searchers.append(Searcher(dictionary, word))
            
        for index , searcher in enumerate(self.searchers):
            searcher.update.connect(self.renew)
            searcher.moveToThread(self.searchThreads[index])
            self.searchThreads[index].start()

            self.signal.connect(searcher.run)
        
        
        self.signal.emit("fire!!")
        print("edited")
               
        #self.multi_search(list(self.allDict.dictList.values()) , word, self.single_renew)
    

    
    
    def search(self, word):
        pass
    
    def renew(self, text, text2):
        #print(dictname)
        print(text)
        print(text2)
        
    
    '''
    def multi_search(self, dictlist, word, resultfunct):
        
        import PyQt5.QtCore as QtCore
        class Searcher(QtCore.QThread):
            def __init__(self, dictionary, f):
                super(Searcher, self).__init__()
                self.dictionary=dictionary
                self.f=f
                
            def run( self ):
                self.f(dictionary, word, resultfunct)
                
        
        searcher_list=[]
        for dictionary in dictlist:
            searcher_list.append(Searcher(dictionary, self.))
            
        
        for searcher in searcher_list:
            searcher.start()
            
        for searcher in searcher_list:
            searcher.wait()
        
    def single_search(self, dictionary, word, resultfunct):
        print(dictionary.name)
#         # search
#         answer=dictionary.search(word)
#         # renew        
#         resultfunct(dictionary, answer)


    def single_renew(self, dictionary, answer):
        print(dictionary.name+" said")
        #print(answer)
        
        
    def setView(self, text):
        self.webView.setHtml(text)
    '''
    
    
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = MyMainWindow()
    myapp.show()
    
    sys.exit(app.exec_())
    
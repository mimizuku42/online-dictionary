#!/usr/bin/env python
# coding: utf-8

'''
Created on 2013/12/11

@author: dacapo
'''

if __name__ == '__main__':
    pass



class Dictionary:
    name=""
    chinese_support=False
    memory=dict()
    def __init__(self, name, chinese_support):
        self.name=name
        self.chinese_support=chinese_support
    
    def translate(self, word):
        try:
            return self.memory[word]
        except KeyError:
            self.memory[word]=self.fetch_translation_from_web(word)
            return self.memory[word]
    
    def fetch_translation_from_web(self, word):
        return "oops"
    
    def search(self):
        pass



class DictionaryList:
    dictList=dict()
    k=1
    @classmethod
    def insert(self, dictionary):
        self.dictList[dictionary.name]=dictionary

# 
# d=Dictionary("Merriam-Webster", False)
# DictionaryList.insert(d)

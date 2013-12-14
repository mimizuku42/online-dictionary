#!/usr/bin/env python
# coding: utf-8

'''
Created on 2013/12/11

@author: dacapo
'''

if __name__ == '__main__':
    pass

class dictionary:
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
            self.memory[word]=self.fetch_translation(word)
            return self.memory[word]
    
    def fetch_translation(self, word):
        return "oops"

    

# d=dictionary("Merriam-Webster", True)
# d.translate("abc")

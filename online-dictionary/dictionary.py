#!/usr/bin/env python
# coding: utf-8

'''
Created on 2013/12/11

@author: dacapo
'''
import pickle


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
    filename="dictionary_cache"
    dictList=dict()   
    
    def insert(self, dictionary):
        self.dictList[dictionary.name]=dictionary
    
    def search(self, word):
        answer=dict()
        for name, dictionary in self.dictList.items():
            answer[name]=dictionary.translate(name)
    
    def load(self):
        f = open(self.filename,'rb')
        tmp_dict = pickle.load(f)
        f.close()          
    
        self.__dict__.update(tmp_dict) 
    
    def save(self):
        f = open(self.filename,'wb')
        pickle.dump(self.__dict__,f,2)
        f.close()
        
d=DictionaryList()
d.insert(Dictionary("Merriam-Webster", False))
print(d.search("apple"))
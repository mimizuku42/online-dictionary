#!/usr/bin/env python
# coding: utf-8

'''
Created on 2013/12/11

@author: dacapo
'''
import pickle


class Dictionary:
    
    def __init__(self, name, chinese_support):
        self.name=name
        self.chinese_support=chinese_support
        self.__memory=dict()
        self.new_word=False
    
    def inner_search(self, word):
        return self.__memory[word]
    
    def outer_search(self, word):
        self.__memory[word]=self.fetch_translation_from_web(word)
        return self.__memory[word]
    
    def search(self, word):
        try:
            return self.inner_search(word)
        except KeyError:
            self.new_word=True
            self.__memory[word]=self.outer_search(word)
            return self.__memory[word]
    
    def fetch_translation_from_web(self, word):
        return "oops"
    

class DictionaryList:
    filename="dictionary_cache"
    def __init__(self):
        self.dictList=dict()
    
    def insert(self, dictionary):
        self.dictList[dictionary.name]=dictionary
        
    def load(self):
        f = open(self.filename,'rb')
        tmp_dict = pickle.load(f)
        f.close()          
    
        self.__dict__.update(tmp_dict) 
    
    def save(self):
        f = open(self.filename,'wb')
        pickle.dump(self.__dict__, f, 2)
        f.close()


if __name__ == '__main__':     
    d=DictionaryList()
    d.insert(Dictionary("Merriam-Webster", False))
    #d.insert(Dictionary("Yahoo", True))
    #d.load()
    print(d.search("apple"))
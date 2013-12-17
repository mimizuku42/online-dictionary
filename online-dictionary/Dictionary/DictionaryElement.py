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
    
    def inner_translate(self, word):
        return self.__memory[word]
    
    def outer_translate(self, word):
        self.__memory[word]=self.fetch_translation_from_web(word)
        return self.__memory[word]
    
#     
#     def translate(self, word):
#         try:
#             return self.__memory[word]
#         except KeyError:
#             self.__memory[word]=self.fetch_translation_from_web(word)
#             new_word=True;
#             return self.__memory[word]
    
    def fetch_translation_from_web(self, word):
        return "oops"
    
    def search(self):
        pass

class DictionaryList:
    filename="dictionary_cache"
    def __init__(self):
        self.dictList=dict()
    
    def insert(self, dictionary):
        self.dictList[dictionary.name]=dictionary
    
    def search(self, word):
        answer=dict()
        new_word=False;
        for name, dictionary in self.dictList.items():
            try:
                answer[name]=dictionary.inner_translate(word)
            except KeyError:
                new_word=True
                answer[name]=dictionary.outer_translate(word)

        if new_word:
            self.save()

        return answer
    
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
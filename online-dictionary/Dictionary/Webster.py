'''
Created on 2013/12/16

@author: dacapo
'''

import lxml.html
from lxml import etree
from Dictionary.DictionaryElement import Dictionary 

class WebsterDict(Dictionary):
    
    def __init__(self):
        super().__init__("Merriam-Webster", False)
        self.url_prefix="http://www.merriam-webster.com/dictionary/"
        self.xpath='//*[@id="wordclick"]/div/div/div/div/div/div/div/div'

    def fetch_translation_from_web(self, word):
        url=self.url_prefix + word
        page=lxml.html.parse(url)
        form=page.xpath(self.xpath)
        #print(etree.tostring(form[0]))
        return str(etree.tostring(form[0]))

if __name__ == '__main__':
    d=WebsterDict()
    print(d.outer_translate("apple"))


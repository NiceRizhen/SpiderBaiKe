#-*- coding: UTF-8 -*- 

'''
Created on 2017年10月25日

@author: 406
'''

class url_manager(object):
    
    def __init__(self):
        self.newurls = set()
        self.oldurls = set()
    
    def get_url(self):

        newurl = self.newurls.pop()
        self.oldurls.add(newurl)
        return newurl

    def add_url(self, url):
        if url is None:
            return None
        
        if url not in self.newurls and url not in self.oldurls:
            self.newurls.add(url)
        
    def add_urls(self, urls):

        if urls is None or 0 == len(urls):
            return None
        
        for url in urls:
            self.add_url(url)

    def has_newurl(self):
        if (0 != len(self.newurls)):
            return True
        
        return False


    
    
    
    
    
    
    
    
    
    
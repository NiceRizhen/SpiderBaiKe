#-*- coding: UTF-8 -*- 

'''
Created on 2017年10月25日

@author: 406
'''
import urllib2


class html_downloader(object):
    
    
    def get_html(self, url):

        if url is None:
            return None
        
        html = urllib2.urlopen(url)
        
        if 200 != html.getcode():
            return None
        
        return html.read()
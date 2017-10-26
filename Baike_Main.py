#-*- coding: UTF-8 -*- 

'''
Created on 2017年10月25日

@author: 406
'''
from Baike import url_manager, html_downloader, html_parser, content

class Baike_Main(object):
        
    def __init__(self):
        self.urls = url_manager.url_manager()
        self.parser = html_parser.url_parser()
        self.downloader = html_downloader.html_downloader()
        self.output = content.outputer()
        
        
        
    
    def run(self, base_url):
        
        self.urls.add_url(base_url)      
        number = 1

        try:
            while self.urls.has_newurl():
                
                curl = self.urls.get_url()
                print u'正在抓取第%d条数据:%s' %(number, curl)
                html = self.downloader.get_html(curl)
                content, urls = self.parser.parser_html(curl, html)
                if content == None or urls == None:
                    continue
                self.urls.add_urls(urls)
                self.output.getdata(content)
                number = number + 1

                if number > 1000:
                    break
        except Exception, e:
            print e.message
            print 'bu ok'
        self.output.writedata()
        
        
if __name__ == "__main__":
    
    base_url = 'https://baike.baidu.com/item/%E5%BD%B1%E9%AD%94/10861150'.decode('utf-8').encode('utf-8')
    main = Baike_Main()
    main.run(base_url)
    
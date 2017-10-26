#-*- coding: UTF-8 -*- 

'''
Created on 2017年10月25日

@author: 406
'''
import sys


class outputer(object):
    
    
    def __init__(self):
        self.totaldata = []
    
    def getdata(self, data):
        if data is None:
            print '传入的数据有误'
            return None

        self.totaldata.append(data)
        #print data['url'] + '      ' + data['title'] + '\n'
       
        #self.totaldata.add(data)
        return
    
    def writedata(self):
        f = open('data.txt', 'w')                       
        reload(sys)
        sys.setdefaultencoding('utf-8')
        for data in self.totaldata:
            print data.get('url')
            f.write(data.get('url') + '\n' + data.get('title') + '\n' + data.get('summary') +'\n\n')
            #
        f.close()




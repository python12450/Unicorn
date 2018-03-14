#coding=utf-8
from __future__ import unicode_literals
from bs4 import BeautifulSoup
import re
class HTMLParase():
    def __init__(self,html_doc):
        self.__html=html_doc
    def GetLink(self):
        self.sp = BeautifulSoup(self.__html,"html.parser" )
        data=self.sp.find_all(u"div",class_=u"a1wrp")
        res=[]
        rex=re.compile(r'a href="https://page.auctions.yahoo.co.jp/jp/auction/(.*?)" onmousedown="this.href=.*">')
        for i in data:
            s=str(i)
            res.append(re.findall(rex,s)[0])
        return res
    def GetCurrentPrice(self):
        self.sp = BeautifulSoup(self.__html,"html.parser")
        data=self.sp.find_all(u"td",class_=u"pr1")
        res=[]
        for i in data:
            s=i.text
            s=s[0:10]
            s=s.strip("            \nYahoo!かんたん決済送料無料\n")
            s=s.replace(" ","")
            s=s.replace("\u5186","")

            s=s.replace(",",'')
            pr=int(s)
            res.append(pr)
        return res
    def GetNext(self):
        self.sp = BeautifulSoup(self.__html,"html.parser")
        try:
            data=self.sp.find(u"p",class_=u"next").find('a')["href"]
        except Exception:
            data=None
        return data
    def GetName(self):
        self.sp = BeautifulSoup(self.__html,"html.parser")
        data=self.sp.find_all(u"div",class_=u"a1wrp")
        res=[]
        for i in data:
            try:
                res.append(i.find('a').text)
            except AttributeError:return []
        return res

#coding=utf-8
from GetContent import GetHTML
import URLgen
from Parase import HTMLParase
htmlrecer=GetHTML()
htmlrecer.Gethtml("https://auctions.yahoo.co.jp/search/search?p=90cm%E3%80%80%E6%B5%AE%E3%81%8D%E8%BC%AA&oq=&auccat=0&tab_ex=commerce&fixed=0&sc_i=&ei=UTF-8&b=101")
htmlpa=HTMLParase(htmlrecer.html)
print(htmlpa.GetLink())
print(htmlpa.GetCurrentPrice())
print(htmlpa.GetNext())
print(htmlpa.GetName())
print(URLgen.gen("东侧为"))


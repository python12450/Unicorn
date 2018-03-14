#coding=utf-8
import urllib2,sys
def gen(name):
    print type(name)
    utf8data =name.encode("utf-8")
    print(type(utf8data))
    utf8data=utf8data.replace(" ","+")
    suburl = urllib2.quote(utf8data)
    urltemplete="https://auctions.yahoo.co.jp/search/search/<amamiharubersacar!>/0/"
    url=urltemplete.replace("<amamiharubersacar!>",suburl)
    return url
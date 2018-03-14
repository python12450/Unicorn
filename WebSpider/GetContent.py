#coding=utf-8
import urllib2,cookielib
import os
import re
from HTMLParser import HTMLParser
class GetHTML():
    html=''
    res=None
    def __init__(self):
        self.cookie=cookielib.MozillaCookieJar()
        self.path=os.path.expanduser('~')+os.sep+"auction"+os.sep+"cookie.cki"
    def Gethtml(self,url="",loadcookie=False):
        req = urllib2.Request(url)
        req.add_header("User-Agent",
                       "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36")
        if loadcookie:
            try:
                self.cookie.load(self.path)
            except Exception:
                print("file not exist or Bad format")
                exit(23)
            try:
                opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookie))
                self.html=opener.open(req).read()
            except urllib2.URLError:
                self.html=''
            #loadcookie from file
        else:
            try:
                opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookie))
                #self.res = urllib2.urlopen(req)
                self.html = opener.open(req).read()
            except urllib2.URLError as e:
                self.html = ''
            if self.cookie:
                self.cookie.save(self.path,ignore_discard=True,ignore_expires=True)
        return self.html
    def Regx(self,rex):
        ret= re.findall(rex,self.html)
        return ret


import urllib2
import cookielib
url="https://auctions.yahoo.co.jp/search/search?n=100&p=%E6%B5%AE%E3%81%8D%E8%BC%AA&ei=UTF-8&oq=&auccat=0&tab_ex=commerce&fixed=0&slider=0"
cookie = cookielib.MozillaCookieJar()
handler=urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
try:
    req = urllib2.Request(url)
    req.add_header("User-Agent",
                   "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36")
    #res = urllib2.urlopen(req)
    html = opener.open(req).read()
    if cookie:
        cookie.save("cookie.txt")
    #html = res.read()
    #html = html.strip("\n")
    # self.html=unicode(self.html,'GBK').encode('UTF-8')
except urllib2.URLError as e:
    html = ''
def CookiBaker(url):
    cookie = cookielib.MozillaCookieJar()
    handler = urllib2.HTTPCookieProcessor(cookie)
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    try:
        req = urllib2.Request(url)
        req.add_header("User-Agent",
                       "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36")
        html = opener.open(req).read()
        if cookie:
            cookie.save("cookie.txt")
    except Exception:
        pass
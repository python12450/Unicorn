from WebSpider.GetContent import GetHTML


def init():
    downloader = GetHTML()
    downloader.Gethtml(
        url="https://auctions.yahoo.co.jp/search/search?n=100&p=90cm+%E6%B5%AE%E3%81%8D%E8%BC%AA&ei=UTF-8&oq=&aucca"
            "t=0&tab_ex=commerce&fixed=0&slider=0", loadcookie=False)

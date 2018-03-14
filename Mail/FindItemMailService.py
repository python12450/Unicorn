#coding=utf8
from EmailBase import SenderBase
class FMIMail(SenderBase):
    def config(self, **kwargs):
        self.sender = "" if "to" not in kwargs.keys() else str(kwargs["sender"])
        self.to=""if "to" not in kwargs.keys() else str(kwargs["to"])
        self.subj="我们好像发现了什么"
        self.isConfiged=True
        return self.isConfiged
    def contentGen(self, **kwargs):
        data_list=[]if "data" not in kwargs.keys() else list(kwargs["data"])
        ret_str=""
        for i in data_list:
            ret_str=ret_str+"名称:"
            ret_str =ret_str+i["name"].encode("utf-8")
            ret_str =ret_str+"链接:"
            ret_str=ret_str+"https://page.auctions.yahoo.co.jp/jp/auction/"+i["auction_id"]+"\n"
        self.content=ret_str

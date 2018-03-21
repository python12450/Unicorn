# coding=utf8
from abc import ABCMeta, abstractmethod

import requests


def mailginFunction(**kwargs):
    apikey = "" if "apikey" not in kwargs.keys() else str(kwargs["apikey"])
    domain = "example.com" if "domain" not in kwargs.keys() else str(kwargs["domain"])
    sender = "" if "sender" not in kwargs.keys() else str(kwargs["sender"])
    to = "" if "to" not in kwargs.keys() else str(kwargs["to"])
    content = "" if "content" not in kwargs.keys() else str(kwargs["content"])
    subj = "" if "subj" not in kwargs.keys() else str(kwargs["subj"])
    data = {}
    data['from'] = 'Unicorn监视器邮件服务<' + sender + '>'
    data["to"] = to
    data['subject'] = subj
    data['text'] = content
    url = "https://api.mailgun.net/v3/YOUR_DOMAIN_NAME/messages".replace("YOUR_DOMAIN_NAME", domain)
    r = requests.post(url, auth=("api", apikey), data=data)
    print r.content


class SenderBase(object):
    __metaclass__ = ABCMeta

    def __init__(self, apikey="", domain=""):
        # self.__pool = multiprocessing.Pool()
        self.content = ""
        self.__apikey = apikey
        self.__dommain = domain
        self.sender = ""
        self.to = ""
        self.subj = ""
        self.isConfiged = False

    def send_sync(self):
        if not self.isConfiged:
            raise AttributeError("Please Config this Instant Fist!!")
        else:
            data = {}
            data['from'] = 'Unicorn监视器邮件服务<' + self.sender + '>'
            data['to'] = self.to
            data['subject'] = self.subj
            data["text"] = self.content
            url = "https://api.mailgun.net/v3/YOUR_DOMAIN_NAME/messages".replace("YOUR_DOMAIN_NAME", self.__dommain)
            r = requests.post(url, auth=("api", self.__apikey), data=data)
            return r.content

    '''def send(self):
        if not self.isConfiged:
            raise AttributeError("Please Config this Instant Fist!!")
        else:
            mailarg = {"apikey": self.__apikey, "domain": self.__dommain, "sender": self.sender, "to": self.to,
                       "subj": self.subj, "content": self.content}
        self.__pool.apply_async(mailginFunction, kwds=mailarg)'''

    @abstractmethod
    def config(self, **kwargs):
        pass

    @abstractmethod
    def contentGen(self, **kwargs):
        pass

# coding=utf8
import os
import time
from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.exc import *
from sqlalchemy.orm import sessionmaker

import itemmanerger


class ResultProxy(object):
    def __init__(self):
        self.ENGINE = create_engine('sqlite:///' + os.path.expanduser('~') + os.sep + "auction" + os.sep + 'itemset.db')
        self.Session = sessionmaker(bind=self.ENGINE, autocommit=False, autoflush=False)
        self.session = self.Session()

    def delete(self, result):
        self.session.delete(result)
        self.session.commit()

    def Add(self, auction_id, name, url=u""):
        if type(name) == str:
            name = name.decode("utf-8")
        if url == u"":
            url = u"https://page.auctions.yahoo.co.jp/jp/auction/" + auction_id
        result = itemmanerger.Result()
        result.name = name
        result.auction_id = auction_id
        result.url = url
        result.time = int(time.mktime(datetime.now().timetuple())) + 3600
        try:
            self.session.add(result)
            self.session.commit()
            return 1
        except IntegrityError:
            self.session.rollback()
            self.session.merge(result)
            self.session.commit()
            return -33  # 键对重复

    def GetALL(self):
        query = self.session.query(itemmanerger.Result)
        q_set = query.all()
        list_set = []
        currenttime = int(time.mktime(datetime.now().timetuple()))
        for i in q_set:
            if int(i.time) < currenttime:
                self.delete(i)
            else:
                list_set.append(i.to_dict())
        return list_set

    def Destroy(self):
        self.session.close()

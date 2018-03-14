from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import  declarative_base
BASE=declarative_base()
class Item(declarative_base()):
    __tablename__="item"
    __table_args__ = {'sqlite_autoincrement': True}
    id=Column(Integer,primary_key=True,autoincrement=True,default=1)
    name=Column(TEXT)
    maxvalue=Column(Integer)
class Result(declarative_base()):
    __tablename__="result"
    auction_id=Column(TEXT,primary_key=True)
    name=Column(TEXT)
    url=Column(TEXT)
    time=Column(INTEGER)
    def to_dict(self):
        return {"auction_id":self.auction_id,"name":self.name,"url":self.url}


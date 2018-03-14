#coding=utf8
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from itemmanerger import Result
ENGINE=create_engine('sqlite:///./itemset.db')
Session= sessionmaker(bind=ENGINE, autocommit=False, autoflush=False)
session=Session()
res=Result()
res.name=u"江泽民"
res.auction_id=u"xxxxx"
res.url=u"xxxxxx"
session.add(res)
session.commit()
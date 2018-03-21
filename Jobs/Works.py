# coding=utf-8
import json
import os
import random
import time
from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.exc import *
from sqlalchemy.orm import sessionmaker

import FileUtil
import SETTING
import SubData.DB
import SubData.itemmanerger
import WebSpider.URLgen
from Config.Reader import loadconfig
from Mail.FindItemMailService import FMIMail


def AutoRun(q, config):
    path = os.path.expanduser('~') + os.sep + "auction" + os.sep + "touch_to_reload"
    FileUtil.FileUtil.create_file(path=path, mode="wb")
    current = os.stat(path).st_mtime
    c = config
    while True:
        ret = Monitor(c, current)
        if ret:
            c = loadconfig()
            current = os.stat(path).st_mtime


def Monitor(config, current):
    list_url = []
    NeedReload = False
    mail = FMIMail(apikey=SETTING.MAILGUN_APIKEY, domain=SETTING.MAILGUN_DOMAIN)
    mail.config(sender=SETTING.MAILGUN_SENDER, to=SETTING.MAILGUN_TO)
    for i in config.Itemlist:
        name = i["name"]
        list_url.append(WebSpider.URLgen.gen(name))
    HTMLDownloader = WebSpider.GetContent.GetHTML()
    tmp_dir_path = os.path.expanduser('~') + os.sep + "auction"
    declearfilepath = tmp_dir_path + os.sep + "youfindyourfile"
    FileUtil.FileUtil.create_file(path=declearfilepath, mode="wb")
    list_len = len(list_url) - 1
    dict_res = []
    terminate = False
    for index, url in enumerate(list_url):
        next_page = url
        path = tmp_dir_path + os.sep + "result.json"
        item = config.Itemlist[index]
        page_count = 1
        terminate = touch_reload(current)
        if terminate:
            NeedReload = True
            break
        while True:
            terminate = touch_reload(current)
            if terminate:
                NeedReload = True
                break
            if page_count == 1:
                html_content = HTMLDownloader.Gethtml(url=next_page, loadcookie=True)
            else:
                html_content = HTMLDownloader.Gethtml(url=next_page, loadcookie=True)
            HTMLPaser = WebSpider.Parase.HTMLParase(html_content)
            list_link = HTMLPaser.GetLink()
            list_name = HTMLPaser.GetName()
            list_currentV = HTMLPaser.GetCurrentPrice()
            for j, link in enumerate(list_link):
                terminate = touch_reload(current)
                if terminate:
                    NeedReload = True
                    break
                if list_currentV[j] <= item["maxvalue"]:
                    if Add(auction_id=link, name=list_name[j]) == 1:
                        dict_res.append({"name": list_name[j], "auction_id": link})
                    print("Add result to Dict")
                time.sleep(random.uniform(0.1, SETTING.FRIENDLY_WAIT))
            next_page = HTMLPaser.GetNext()
            if next_page is None:
                break
            # if not q.empty():
            # if q.get()==-961:
            # terminate=True
            # with open(path,mode="wb") as f:
            #    json.dump(dict_res,f)
            # break
        if index == list_len:
            if len(dict_res) != 0 and SETTING.MAIL_ENABLE:
                mail.contentGen(data=dict_res)
                print mail.send_sync()
            with open(path, mode="wb") as f:
                json.dump(dict_res, f)
            print("Saving")
    return NeedReload


def touch_reload(current):
    path = os.path.expanduser('~') + os.sep + "auction" + os.sep + "touch_to_reload"
    statinfo = os.stat(path)
    time = statinfo.st_mtime
    if current != time:
        return True
    else:
        return False


def Add(auction_id, name, url=u""):
    ENGINE = create_engine('sqlite:///' + os.path.expanduser('~') + os.sep + "auction" + os.sep + 'itemset.db')
    Session = sessionmaker(bind=ENGINE, autocommit=False, autoflush=False)
    session = Session()
    if type(name) == str:
        name = name.decode("utf-8")
    if url == u"":
        url = u"https://page.auctions.yahoo.co.jp/jp/auction/" + auction_id
    result = SubData.itemmanerger.Result()
    result.name = name
    result.auction_id = auction_id
    result.url = url
    result.time = int(time.mktime(datetime.now().timetuple())) + 3600
    try:
        session.add(result)
        session.commit()
        session.close()
        return 1
    except IntegrityError:
        session.rollback()
        session.merge(result)
        session.commit()
        session.close()
        return -33

import json
import multiprocessing
import os
from multiprocessing import Queue

from flask import Flask, render_template, render_template_string

import init_tool
from Config import Reader
from Jobs import Works, FileUtil
from SubData.DB import ResultProxy

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template_string('<a href="/r">result</a>')


@app.route('/r')
def Read():
    reslutproxy = ResultProxy()
    list_ret = reslutproxy.GetALL()
    path = os.path.expanduser('~') + os.sep + "auction" + os.sep + "result.json"
    # with open(path,mode="r") as f:
    #   list_ret=json.load(f)
    reslutproxy.Destroy()
    return render_template("read.html", result=list_ret)


@app.route('/p/reload')
def Reload():
    path = os.path.expanduser('~') + os.sep + "auction" + os.sep + "touch_to_reload"
    FileUtil.FileUtil.create_file(path=path, mode="wb")
    return "Naughty!!"


@app.route('/c/list')
def List_Config():
    path = os.path.expanduser('~') + os.sep + "auction" + os.sep + "result.json"
    with open(path, mode="r") as f:
        list_ret = json.load(f)
    return "Naughty!!"


if __name__ == '__main__':
    init_tool.init()
    config = Reader.loadconfig()
    q = Queue()
    p = multiprocessing.Process(target=Works.AutoRun, args=(q, config))
    p.daemon = True
    p.start()
    app.run()

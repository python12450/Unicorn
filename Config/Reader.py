#coding=utf-8
import json,os
import FileUtil
import Cfg
def loadconfig():
    tmp_dir_path=os.path.expanduser('~')+os.sep+"auction"
    declearfilepath = tmp_dir_path + os.sep + "youfindyourfile"
    configname="config.json"
    FileUtil.FileUtil.create_file(path=declearfilepath, mode="wb")
    configpath=tmp_dir_path+os.sep+configname
    if not os.path.isfile(configpath):
        data = {"items": [{"name": "Your+item", "maxvalue": 2000}]}
        with open(configpath, "w") as f:
            json.dump(data, f)
            f.close()
    else:
        with open(configpath,"r") as f:
            data=json.load(f)
    config=Cfg.Config()
    config.Itemlist=data["items"]
    return config
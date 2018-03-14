#!/usr/bin/env python
# -* -coding: UTF-8 -* -

import os
import platform


class FileUtil:
    def __init__(self):
        self.desc = "Filt Util"

    @staticmethod
    def create_file(**kwargs):
        path = None if "path" not in kwargs.keys() else str(kwargs["path"])
        mode = "w+" if "mode" not in kwargs.keys() else str(kwargs["mode"])
        content = None if "content" not in kwargs.keys() else kwargs["content"]
        if None is path:
            raise ValueError("Path should not be Null!")
        abs_path = os.path.abspath(path)
        path_list = abs_path.split(os.sep)
        currwork = ""
        plat = platform.system()
        for i in range(path_list.__len__()):
            if not path_list[i] == "":
                if i == 0 and plat == "Windows":
                    currwork += path_list[i]
                else:
                    currwork += os.sep + path_list[i]
                if not os.path.isdir(currwork):
                    if i == (path_list.__len__() - 1):
                        if content:
                            with open(currwork, mode) as code:
                                code.write(content.read())
                        else:
                            open(currwork, mode).close()
                    else:
                        os.mkdir(currwork)
        return abs_path

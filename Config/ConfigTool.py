# coding=utf8
import json
import os
from Tkinter import *


def Add_click(list_item, list_value, master):
    global length
    length = length + 1
    Label(master, text="物品").grid(row=length, sticky=W)
    item = Entry(master)
    item.grid(row=length, column=1)
    list_item.append(item)
    Label(master, text="价格").grid(row=length, column=2, sticky=W)
    v = Entry(master)
    v.grid(row=length, column=3)
    list_value.append(v)


def Save_click(list_item, list_value):
    zeroBlankIndex = []
    items = []
    for index, item in enumerate(list_item):
        if None is item.get() or len(item.get()) <= 1:
            zeroBlankIndex.append(index)
        else:
            str_i = item.get().replace(" ", "+")
            int_i = int(list_value[index].get())
            items.append({"name": str_i, "maxvalue": int_i})
    dict_res = {"items": items}
    path = os.path.expanduser('~') + os.sep + "auction" + os.sep + "config.json"
    with open(path, "wt") as f:
        json.dump(dict_res, f)
        f.close()


path = os.path.expanduser('~') + os.sep + "auction" + os.sep + "config.json"
data = {}
with open(path, "r") as f:
    data = json.load(f)
length = len(data["items"])
list_item = []
list_value = []
master = Tk()
add = Button(master, text='add', command=lambda: Add_click(list_item, list_value, master))
add.grid(row=0, column=4, rowspan=1, sticky=N + S)

save = Button(master, text='save', command=lambda: Save_click(list_item, list_value))
save.grid(row=1, column=4, rowspan=1, sticky=N + S)
for i in range(length):
    Label(master, text="物品").grid(row=i, sticky=W)
    item = Entry(master)
    item.insert(0, data["items"][i]["name"])
    item.grid(row=i, column=1)
    list_item.append(item)
    Label(master, text="价格").grid(row=i, column=2, sticky=W)
    v = Entry(master)
    v.insert(0, data["items"][i]["maxvalue"])
    v.grid(row=i, column=3)
    list_value.append(v)
mainloop()




import time
import timeago,datetime
from operator import itemgetter










def get_type_data_cloud(type,number,creative_database):
    #global creative_database
    u = []
    for i in creative_database:
        if i["type"] == type :
            u.append(i)
    u.sort(key=itemgetter('time'), reverse=True)
    try:
        t = u[0:int(number)]
    except:
        t = u
    return t


def change_time_type_cloud(data):
    now = datetime.datetime.now()
    t = []
    for i in data:
        f = {}
        if i["comment_number"] == "true":
            f["name"], f["summary"], f['author'], f["author_id"], f["content"], f["id"], f["type"], f["time"], f[
                "view_number"] \
                = i["name"], i["summary"], i['author'], i["author_id"], i["content"], i["id"], i["type"], i["time"], i[
                "view_number"]
            f["time"] = timeago.format(f["time"], now, "zh_CN")
            t.append(f)
    return t



def change_password_type_cloud(data):
    t = []
    for i in data:
        f = {}
        if i["view_number"] == "true":
            f["name"], f["summary"], f['author'], f["author_id"], f["content"], f["id"], f["type"], f["time"], f[
                "view_number"] \
                = i["name"], i["summary"], "", i["author_id"], i["content"], i["id"], i["type"], i["time"], i[
                "view_number"]
            t.append(f)
        else:
            f["name"], f["summary"], f['author'], f["author_id"], f["content"], f["id"], f["type"], f["time"], f[
                "view_number"] \
                = i["name"], i["summary"], i['author'], i["author_id"], i["content"], i["id"], i["type"], i["time"], i[
                "view_number"]
            t.append(f)
    return t





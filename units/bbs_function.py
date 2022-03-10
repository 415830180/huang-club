

import time
import timeago,datetime
from operator import itemgetter



def change_time_type(data,type="1"):
    now = datetime.datetime.now()
    data.sort(key=itemgetter('create_time'), reverse=True)
    t = []
    for i in data:
        f = {}
        if i["type"] == type:
            f["tid"], f["abstract"],f["time"],f['content'] \
                = i["tid"], i["abstract"], i['create_time'],i['content']
            f["time"] = timeago.format(f["time"], now, "zh_CN")
            t.append(f)
        if type == "1":
            f["tid"], f["abstract"], f["time"], f['content'] \
                = i["tid"], i["abstract"], i['create_time'], i['content']
            f["time"] = timeago.format(f["time"], now, "zh_CN")
            t.append(f)
    return t
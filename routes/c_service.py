

from flask import Blueprint,request,make_response,jsonify,render_template
import json
import uuid
from models import *
from tencent_cloud import up_tencent
import random

connection_service = Blueprint("connection_service",__name__)





@connection_service.route("/api/search",methods = ['get','post'])
def api_search():
    search_value = str(request.cookies.get("search_value"))
    t = []
    a = Post().post_list()
    for i in a:
        try:
            if search_value in i['content']:
                i['type'] = 'post'
                t.append(i)
        except:
            pass
    cloud_search_res = Cloud().search_cloud(search_value)
    t = t + cloud_search_res
    return { "search_result" : t,
             "search_value" : search_value }




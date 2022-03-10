from flask import Blueprint,request,make_response,jsonify,render_template
import json
import uuid
from models import *
from tencent_cloud import up_tencent
import random

connection_cloud = Blueprint("connection_cloud",__name__)


@connection_cloud.route("/api/get_cloud",methods = ["get","POST"])
def get_cloud():
    return Cloud().get_cloud()


@connection_cloud.route("/api/get_more_file",methods = ["get","POST"])
def get_more_file():
    t = request.cookies.get("more_file")
    t = int(t)
    t = t + 10
    #print(t)
    return Cloud().get_more_file(t)

@connection_cloud.route("/api/get_cloud_file",methods = ["get","POST"])
def gg_cloud_file():
    request_data = json.loads(request.get_data())
    return Cloud(request_data).get_cloud_file()



@connection_cloud.route('/api/video_up_video_cloud', methods=['GET', 'POST'])
def up_file_cloud():
    if request.method == "POST":
        address = str(uuid.uuid4())[0:8]
        t = request.cookies.get("id")
        file = request.files['mf']
        file_address_test = t + str(file.filename)
        new_fname = r'/data/www/' + str(file_address_test)
        file.save(new_fname)  # 保存文件到指定路径
        #print("本地保存成功")
        up_tencent(new_fname,
                   "web_file/picture/" + address + "/" + str(file.filename))
        #print(t,str(file.filename))
        database_operation("insert", "creative_data", "(id,type,time,name,author,author_id,summary,content)",
                           str((t,"file", get_time(), str(file.filename),address,get_ip(),str(file.filename),"none"))
                           )
        return jsonify('上传成功')
    return "fuck"



@connection_cloud.route("/api/up_file_inf_cloud",methods = ["get","POST"])
def up_file_inf():
    request_data = json.loads(request.get_data())
    id = request.cookies.get("id")
    password,password_value,public,other_name,other_name_value,note = request_data["password"],\
        request_data["password_value"],request_data["public"],request_data["other_name"],\
        request_data["other_name_value"],request_data["note"]
    database_operation("update", "creative_data", "id", id, "view_number", password)
    database_operation("update", "creative_data", "id", id, "like_number", password_value)
    database_operation("update", "creative_data", "id", id, "comment_number", public)
    database_operation("update", "creative_data", "id", id, "all_comment", other_name)
    database_operation("update", "creative_data", "id", id, "summary", other_name_value)
    database_operation("update", "creative_data", "id", id, "content", note)
    print(request_data)
    return jsonify("success")



@connection_cloud.route("/api/verify",methods = ["get","POST"])
def hh():
    request_data = json.loads(request.get_data())
    password = request_data["password"]
    t = Cloud(request_data).get_file_inf()
    real_password = t[0]["like_number"]
    if password == real_password:
        return jsonify(t[0]["author"])
    return jsonify("password_error_huang")





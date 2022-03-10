from flask import Blueprint,request,make_response,jsonify,render_template
import json
import uuid
from models import *
from tencent_cloud import up_tencent
import random



connection_bbs = Blueprint("connection_bbs",__name__)




@connection_bbs.route('/api/delete', methods=['GET', 'POST'])
def delete():
    ajax_data = json.loads(request.get_data())
    post_id = ajax_data["post_id"]
    token = request.cookies.get("token")
    user = User(token)
    if token == None :
        return {'status':200,'msg':'验证过期。'}
    if user.status == 200 :
        if Post(post_id).right(token) == "无此id":
            return {'status': 200, 'msg': '找不到此 ID.'}
        if Post(post_id).right(token) == "vip":
            Post(post_id).delete()
            return {'status': 200, 'msg': '尊贵的vip您好。帖子已删除。'}
        if Post(post_id).right(token) == "yes":
            Post(post_id).delete()
            return {'status': 200, 'msg': '帖子已删除。'}
        if Post(post_id).right(token)[0] == "no_right":
            text = '此帖子属于' + Post(post_id).right(token)[1] + "，您无权限操作。"
            return {'status': 200, 'msg': text }
    return {'status':200,'msg':'验证过期。'}



@connection_bbs.route("/api/get_data2",methods = ["get","POST"])
def fff():
    ajax_data = json.loads(request.get_data())
    tid = ajax_data["type"]
    if Post(tid).status == 200:
        return Post(tid).post_only()
    return "error"



@connection_bbs.route("/api/get_data1",methods = ["get","POST"])
def ff():
    return jsonify(Post().post_list())



@connection_bbs.route("/api/get_comment",methods = ["get","POST"])
def get_comment():
    ajax_data = json.loads(request.get_data())
    tid = ajax_data["type"]
    if Post(tid).status == 200 :
        return Post(tid).get_comment()
    return "error"



@connection_bbs.route("/api/comment",methods = ["get","POST"])
def comment():
    ajax_data = json.loads(request.get_data())
    comment_id = request.cookies.get("file_name")
    content = ajax_data["content"]
    print(content)
    id = str(uuid.uuid4())
    tid = id[:8]
    if content != '<p></p>':
        Post(comment_id).up_comment(tid,content)
    return {'status': 200, 'msg': tid}



@connection_bbs.route('/api/receive_content', methods=['GET', 'POST'])
def receive_content():
    ajax_data = json.loads(request.get_data())
    content = ajax_data["content"]
    token = request.cookies.get("token")
    print(content)
    id = str(uuid.uuid4())
    tid = id[:8]
    if content != '<p></p>':
        uid = User(token).get("id")
        if token != '':
            Post().create(tid,uid,content)
        else:
            Post().create(tid,"游客",content)
    return {'status':200,'msg':tid }


@connection_bbs.route('/file', methods=['GET', 'POST'])
def up_file1():
    if request.method == "POST":
        t = str(uuid.uuid4())
        t = t[:8]
        file = request.files['ajaxTaskFile']
        file_address_test = t + str(file.filename)
        new_fname = r'/data/www/' + str(file_address_test)
        file.save(new_fname)  # 保存文件到指定路径
        up_tencent(new_fname, "web_file/picture/" + t + ".jpg")
        return jsonify('https://huang-1258465420.cos.ap-shanghai.myqcloud.com/web_file/picture/' + t + ".jpg")
    return ""





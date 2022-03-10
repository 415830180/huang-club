from flask import Blueprint,request,make_response,jsonify,render_template,Flask
import json
from models import *
import uuid
import random
from mail import send_mail

connection_user = Blueprint("connection_user",__name__)


@connection_user.route("/api/get_name",methods = ["get","POST"])
def get_name():
    ajax_data = json.loads(request.get_data())
    token = ajax_data["token"]
    user = User(token)
    if user.status == 200 :
        return jsonify(user.get("username"))
    return "error"



#
# @app.route('/api/sign', methods=['GET', 'POST'])
# def verify_sign():
#     ajax_data = json.loads(request.get_data())
#     email = ajax_data["email"]
#     password = ajax_data["password"]
#     for i in database_operation("search", "core"):
#         try:
#             if i["email"] == email:
#                 if i['password'] == password:
#                     token1 = str(uuid.uuid4())
#                     token = token1[:8]
#                     database_operation("update", "core", "email", email, "token", token)
#                     response = make_response({'status':200,'msg':"登入成功。"})
#                     response.set_cookie("token", token, 3600)
#                     return response
#         except:
#             pass
#     return {'status':200,'msg':'邮箱地址或密码错误。'}




@connection_user.route('/api/sign', methods=['GET', 'POST'])
def verify_sign():
    ajax_data = json.loads(request.get_data())
    email = ajax_data["email"]
    password = ajax_data["password"]
    user = User(email)
    if user.status == 404:
        return {'status':200,'msg':'邮箱地址或密码错误。'}
    if user.status == 200:
        if user.verify_password(password):
            token1 = str(uuid.uuid4())
            token = token1[:8]
            user.change("token",token)
            # database_operation("update", "core", "email", email, "token", token)
            response = make_response({'status':200,'msg':"登入成功。"})
            response.set_cookie("token", token, 3600)
            return response
        else:
            return {'status': 200, 'msg': '邮箱地址或密码错误。'}






@connection_user.route('/api/register', methods=['GET', 'POST'])
def verify_register():
    ajax_data = json.loads(request.get_data())
    email = ajax_data["email"]
    password = ajax_data["password"]
    verify_code = ajax_data["verify_code"]
    name = ajax_data["name"]
    if len(name) > 10:
        return {"status":200,"msg":"名称长度过长。"}
    b = 0
    for i in database_operation("search", "core"):
        try:
            if i["email"] == email:
                b = 1
                if i['password'] != None:
                    a = "此邮箱已被注册。"
                    return {"status": 200, "msg": a}
                if i["Verification_code"] != verify_code:
                    return {"status": 200, "msg": "验证码错误"}
            if i["username"] == name:
                a = "此名称已被注册。"
                return {"status": 200, "msg": a}
        except:
            return {"status": 404, "msg": "error"}
    if b == 0:
        return {"status": 200, "msg": "请不要乱填验证码！"}
    database_operation("update","core","email",email,"password",password)
    database_operation("update","core","email",email,"username",name)
    return {"status":200,"msg":"注册成功"}





@connection_user.route('/api/verify_name', methods=['GET', 'POST'])
def verify_name():
    ajax_data = json.loads(request.get_data())
    name = ajax_data["name"]
    if len(name) > 10:
        return {"status":200,"msg":"名称长度过长。"}
    a = "名称可用"
    for i in database_operation("search", "core"):
        try:
            if i["username"] == name:
                a = "此名称已被注册。"
        except:
            pass
    return {"status":200,"msg":a}






@connection_user.route('/api/verify_code', methods=['GET', 'POST'])
def verify_code():
    ajax_data = json.loads(request.get_data())
    if True :
        #print(ajax_data)
        phone = ajax_data['InputPhone']
        code = ""
        for i in range(6):
            ch = chr(random.randrange(ord('0'), ord('9') + 1))
            code += ch
        a = 0
        for i in  database_operation("search","core"):
            try:
                if i["email"] == phone and i['password'] != None :
                    print(i)
                    database_operation("update","core","email",phone,"Verification_code",str(code))
                    a = 1
                    #print("此邮箱已注册")
                    return {"status": 200, "msg" : "此邮箱已注册，请登入。"}
            except:
                pass

        #msg = Message(subject='zedonghuang.club 注册邮箱验证.', sender='沢栋黄<zedonghuang.club@qq.com>', recipients=[phone])
        ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
        send_mail(phone,ip,code)
        # mail.send(msg)



        print("邮箱账号:", phone)
        print("验证码:", code)
        if a == 0:
            print("there are not this people")
            id = str(uuid.uuid4())
            uid = id[:12]
            database_operation("insert","core",'(uid,email,Verification_code)',
                               str((uid,phone,code
                                   )))
        return {"status": 200, "msg" : "验证码已经发送至您的邮箱，请注意查收."}



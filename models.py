from database import database_operation
from units.global_function import *
from units.bbs_function import *
from units.cloud_function import *
from flask import jsonify

class User(object):

    def __init__(self,id):#,id,email,username,password,token,auth_code
        if database_operation("search","core","uid",id) != [] and database_operation("search","core","uid",id) != "error":
            self.status = 200
            self.__id = database_operation("search","core","uid",id)[0].get('uid')
            self.__email = database_operation("search","core","uid",id)[0].get('email')
            self.__username = database_operation("search","core","uid",id)[0].get('username')
            self.__password = database_operation("search","core","uid",id)[0].get('password')
            self.__token = database_operation("search","core","uid",id)[0].get('token')
            self.__auth_code = database_operation("search","core","uid",id)[0].get('Verification_code')
        elif database_operation("search","core","email",id) != [] and database_operation("search","core","email",id) != "error":
            self.status = 200
            self.__id = database_operation("search","core","email",id)[0].get('uid')
            self.__email = database_operation("search","core","email",id)[0].get('email')
            self.__username = database_operation("search","core","email",id)[0].get('username')
            self.__password = database_operation("search","core","email",id)[0].get('password')
            self.__token = database_operation("search","core","email",id)[0].get('token')
            self.__auth_code = database_operation("search","core","email",id)[0].get('Verification_code')
        elif database_operation("search","core","token",id) != [] and database_operation("search","core","token",id) != "error":
            self.status = 200
            self.__id = database_operation("search","core","token",id)[0].get('uid')
            self.__email = database_operation("search","core","token",id)[0].get('email')
            self.__username = database_operation("search","core","token",id)[0].get('username')
            self.__password = database_operation("search","core","token",id)[0].get('password')
            self.__token = database_operation("search","core","token",id)[0].get('token')
            self.__auth_code = database_operation("search","core","token",id)[0].get('Verification_code')
        else:
            self.status = 404


    def get(self,type):
        if type == "id":
            return self.__id
        if type == "email":
            return self.__email
        if type == "username" :
            return self.__username
        if type == "password" :
            return self.__password
        if type == "token" :
            return self.__token
        if type == "auth_code" :
            return self.__auth_code

    def change(self,type,change_value):
        if type == "email":
            database_operation("update", "core", "uid", self.__id , "email", str(change_value))
        if type == "username" :
            database_operation("update", "core", "uid", self.__id , "username", str(change_value))
        if type == "password" :
            database_operation("update", "core", "uid", self.__id , "password", str(change_value))
        if type == "token" :
            print(1,self.__id)
            database_operation("update", "core", "uid", self.__id , "token", str(change_value))
        if type == "auth_code" :
            database_operation("update", "core", "uid", self.__id , "Verification_code", str(change_value))

    def create(self,email,auth_code):
        database_operation("insert", "core", '(uid,email,Verification_code)',
                           str((self.__id,email,auth_code)))

    def verify_password(self,password):
        if self.__password == password:
            return True
        else:
            return False




class Post(object):
    def __init__(self,id = 'default'):
        if id == "default":
            self.status = 404
        else:
            if database_operation("search", "content_data", "tid", id) != [] and database_operation("search","content_data","tid",id) != "error":
                self.status = 200
                self.__id = id
                self.__owner = database_operation("search", "content_data", "tid", id)[0].get('owner')
                self.__type = database_operation("search", "content_data", "tid", id)[0].get('type')
                self.__create_tme = database_operation("search", "content_data", "tid", id)[0].get('create_time')
                self.__abstract = database_operation("search", "content_data", "tid", id)[0].get('abstract')
                self.__content = database_operation("search", "content_data", "tid", id)[0].get('content')
            else:
                self.status = 404

    def create(self,tid,uid,content):
        try:
            summary = html_to_chinese(content)[:20] + "..."
        except:
            summary = html_to_chinese(content)
        database_operation('insert', 'content_data', "(tid,owner,type,create_time,abstract,content)", str(
            (tid,uid,"post",get_time(),summary, content)))

    def delete(self):
        database_operation("update", "content_data", "tid", self.__id , "type", "post_hidden")

    def right(self,uid):
        if self.status != 200:
            return "无此id"
        else:
            if User(uid).get('email') == "2992989851@qq.com" or User(uid).get('email') == "huangzedong2@gmail.com":
                return "vip"
            else:
                t = self.__owner
                t1 = User(uid).get('id')
                if t != t1:
                    return ['no_right', t]
                if t == t1:
                    return "yes"

    def post_list(self,number = 10):
        try:
            return (change_time_type(database_operation("search", "content_data"), "post"))[:number]
        except:
            return (change_time_type(database_operation("search", "content_data"), "post"))

    def post_only(self):
        return jsonify((change_time_type(database_operation("search","content_data","tid",self.__id))))

    def get_comment(self):
        return jsonify(change_time_type(database_operation("search","content_data","owner",self.__id)))

    def up_comment(self,tid,content):
        database_operation('insert', 'content_data', "(tid,owner,type,create_time,content)", str(
            (tid,self.__id,"comment",get_time(),content)))




class Cloud(object):
    def __init__(self,id='default'):

        if id == "default":
            self.status = 404
            self.__cloud = database_operation("search",'creative_data')
        else:
            self.__cloud = database_operation("search",'creative_data')
            self.__information = database_operation('search','creative_data','id',id['type'])


    def get_cloud(self):
        creative_database = self.__cloud
        return jsonify(change_password_type_cloud(change_time_type_cloud(get_type_data_cloud("file", 10 ,creative_database))))

    def get_more_file(self,number):
        creative_database = self.__cloud
        return jsonify(change_password_type_cloud(change_time_type_cloud(get_type_data_cloud("file", number ,creative_database))))

    def get_cloud_file(self):
        return jsonify(change_password_type_cloud(self.__information))

    def get_file_inf(self):
        return self.__information

    def search_cloud(self,search_value):
        creative_database = self.__cloud
        u = get_type_data_cloud("file", 500, creative_database)
        t = []
        for i in u:
            try:
                if search_value in i["name"] or search_value in i["summary"] or search_value in i["content"]:
                    t.append(i)
            except:
                pass
        return t



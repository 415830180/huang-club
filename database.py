import mysql.connector



def database_operation(operation_type,form_name,obj_key=None,obj_value=None,update_key=None,update_value=None,):
    conn = mysql.connector.connect(user='root', password='20001103', database='web', charset="utf8mb4",
                                   use_unicode=True)
    cursor = conn.cursor(dictionary=True)
    try:
        if operation_type == "search":
            if obj_key and obj_value:
                sql = 'select * from %s where %s = "%s"' % (form_name,obj_key,obj_value)
            else:
                sql = "SELECT * FROM "+str(form_name)
            cursor.execute(sql)
            u = cursor.fetchall()
            #u.sort(key=itemgetter('time'), reverse=True)
            conn.commit()
            return u

        # print(database_operation("insert","creative_data",'(id)','("storyfaee7d17-221f-408a-b6f6-3de78c109")'))
        if operation_type == "insert":
            if obj_key and obj_value :
                cursor.execute(
                'insert into ' + form_name + " " + obj_key + ' values' + obj_value)
                conn.commit()
            #if change_cache(form_name):
                return "insert successful"
        if operation_type == "update":
            if obj_key and obj_value and update_key and update_value :
                cursor.execute('update %s set %s = "%s" where %s = "%s"'
                               %(form_name,update_key,update_value,obj_key,obj_value))
                conn.commit()
            #if change_cache(form_name):
                return "update_successful"
        if operation_type == "delete":
            if obj_key and obj_value :
                cursor.execute('delete from %s where %s = "%s"'
                               % (form_name, obj_key, obj_value))
                conn.commit()
            #if change_cache(form_name):
                return "delete_successful"
    except:
        pass
    conn.close()
    return "error"




import pymysql
from model import User
#连接数据库
def set_conect():
    return pymysql.connect(host='127.0.0.1',port=3306,user='root',password='123',database='bilibili_vedio')
class user_db(object):
    # 删除表(测试用)
    @staticmethod
    def drop_user_table():
        conn = set_conect()
        cursor = conn.cursor()
        try:
            cursor.execute("drop table if exists USER")
            conn.commit()
        except:
            print("drop_user_table error")
        finally:
            cursor.close()
            conn.close()
    #初始化表
    @staticmethod
    def init_user_table():

        sql="""CREATE TABLE USER (
            user_id INT auto_increment PRIMARY KEY ,
            user_name CHAR(16) NOT NULL UNIQUE ,
            password CHAR(16) NOT NULL ,
            user_detail CHAR(200) ,
            name CHAR(16) NOT NULL
            )
        """
        conn = set_conect()
        cursor = conn.cursor()
        try:

            cursor.execute(sql)
            conn.commit()
        except:
            print("init_user_table error")
        finally:
            cursor.close()
            conn.close()
    # 插入用戶,输入用戶类
    @staticmethod
    def insert_user_table(user):
        if type(user) != User:
            return False
        sql = "INSERT INTO USER(user_name,password,user_detail,name) VALUE (%s,%s,%s,%s);"
        conn = set_conect()
        cursor = conn.cursor()
        try:
            cursor.execute(sql, (user.username,user.password,user.detail,user.name))
            conn.commit()
        except:
            print("insert_user_table error")
            conn.rollback()
            return False
        finally:
            cursor.close()
            conn.close()
        return True

    #插入多条课程,输入课程类数组
    @staticmethod
    def insert_users_table(users):
        if users==None:
            return False
        if len(users)==0:
            return False
        sql = "INSERT INTO USER(user_name,password,user_detail,name) VALUE (%s,%s,%s,%s);"
        s=[]
        for row in users:
            if row==None:
                return False
            a=(row.username,row.password,row.detail,row.name)
            s.append(a)
        conn = set_conect()
        cursor = conn.cursor()
        try:
            cursor.executemany(sql, (s))
            conn.commit()
        except:
            print("insert_users_table error")
            conn.rollback()
            return False
        finally:
            cursor.close()
            conn.close()
        return True


    # 删除表中所有元素
    @staticmethod
    def delete_all_user_table():
        sql = "DELETE FROM USER;"
        conn = set_conect()
        cursor = conn.cursor()
        try:
            cursor.execute(sql)
            conn.commit()
        except:
            print("delete_all_user_table error")
            conn.rollback()
            return False
        finally:
            cursor.close()
            conn.close()
        return True

    # 删除表中一个元素(id)
    @staticmethod
    def delete_user_table2(id):
        if id==None:
            return False
        sql = "DELETE FROM USER WHERE user_id= %s "
        conn = set_conect()
        cursor = conn.cursor()

        try:
            cursor.execute(sql, (id))
            conn.commit()
        except:
            print("delete_user_table2 error")
            conn.rollback()
            return False
        finally:
            cursor.close()
            conn.close()
        return True

    #修改用戶中密码,输入id,密码
    @staticmethod
    def update_user_password(id,password):
        if id==None or password==None:
            return False

        sql = "UPDATE USER SET password=%s WHERE user_id= %s "
        conn = set_conect()
        cursor = conn.cursor()

        try:
            cursor.execute(sql, (password,id))
            conn.commit()
        except:
            print("update_user_password error")
            conn.rollback()
            return False
        finally:
            cursor.close()
            conn.close()
        return True
    #修改用戶信息,输入id,用戶类
    @staticmethod
    def update_user_table(id,user):
        if id==None:
            return False
        if user==None:
            return False
        sql = "UPDATE USER SET name=%s,user_detail=%s WHERE user_id= %s "
        conn = set_conect()
        cursor = conn.cursor()

        try:
            cursor.execute(sql, (user.name,user.detail, id))
            conn.commit()
        except:
            print("update_user_table error")
            conn.rollback()
            return False
        finally:
            cursor.close()
            conn.close()
        return True

    #查找用戶帳号,输入帳号,返回帳号名
    @staticmethod
    def select_user_name(username):
        if username==None:
            return None

        sql = "SELECT user_name FROM USER WHERE user_name=%s;"

        conn = set_conect()
        cursor = conn.cursor()
        try:
            cursor.execute(sql, (username))
            conn.commit()
            result = cursor.fetchone()[0]

        except:
            print("select_user_name error")
            return None
        finally:
            cursor.close()
            conn.close()
        return result

    #查找用戶帳号密码,用戶验证,返回密码

    @staticmethod
    def select_password(username, password):
        if username == None or password==None:
            return None

        sql = "SELECT password FROM USER WHERE user_name=%s AND password=%s;"

        conn = set_conect()
        cursor = conn.cursor()
        try:
            cursor.execute(sql, (username,password))
            conn.commit()
            result = cursor.fetchone()[0]

        except:
            print("select_password error")
            return None
        finally:
            cursor.close()
            conn.close()
        return result

    #查找用戶,输入帳号和密码,返回用戶类
    @staticmethod
    def select_user(username,password):
        if username == None or password==None:
            return None

        sql = "SELECT * FROM USER WHERE user_name=%s AND password=%s;"

        conn = set_conect()
        cursor = conn.cursor()
        try:
            cursor.execute(sql, (username,password))
            conn.commit()
            result = cursor.fetchone()
            user=User(username=result[1],password=result[2],detail=result[3],name=result[4])

        except:
            print("select_password error")
            return None
        finally:
            cursor.close()
            conn.close()

        return user

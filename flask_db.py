import pymysql
from model import Course
#连接数据库
def set_conect():
    return pymysql.connect(host='127.0.0.1',port=3306,user='root',password='123',database='bilibili_vedio')
class db(object):

    #删除表(测试用)
    @staticmethod
    def drop_course_table():
        conn = set_conect()
        cursor = conn.cursor()
        try:
            cursor.execute("drop table if exists COURSE")
            conn.commit()
        except:
            print("init_course_table error")
        finally:
            cursor.close()
            conn.close()

    #初始化表
    @staticmethod
    def init_course_table():

        sql="""CREATE TABLE COURSE (
            course_id INT auto_increment PRIMARY KEY ,
            course_name TEXT NOT NULL ,
            course_type VARCHAR(40) NOT NULL ,
            course_url VARCHAR(200) NOT NULL ,
            platform_name VARCHAR(40) NOT NULL
            )
        """
        conn = set_conect()
        cursor = conn.cursor()
        try:
            #cursor.execute("drop table if exists COURSE")
            cursor.execute(sql)
            conn.commit()
        except:
            print("init_course_table error")
        finally:
            cursor.close()
            conn.close()

    #插入课程,输入课程类
    @staticmethod
    def insert_course_table(course):
        if type(course)!=Course:
            return False
        sql="INSERT INTO COURSE(course_name,course_type,course_url,platform_name) VALUE (%s,%s,%s,%s);"
        conn = set_conect()
        cursor = conn.cursor()
        try:
            cursor.execute(sql,(course.course_name,course.course_type,course.course_url,course.platform_name))
            conn.commit()
        except:
            print("insert_course_table error")
            conn.rollback()
            return False
        finally:
            cursor.close()
            conn.close()
        return True
    #插入多条课程,输入课程类数组
    @staticmethod
    def insert_courses_table(courses):
        if courses==None:
            return False
        if len(courses)==0:
            return False
        sql = "INSERT INTO COURSE(course_name,course_type,course_url,platform_name) VALUE (%s,%s,%s,%s);"
        s=[]
        for row in courses:
            if row==None:
                return False
            a=(row.course_name,row.course_type,row.course_url,row.platform_name)
            s.append(a)
        conn = set_conect()
        cursor = conn.cursor()
        try:
            cursor.executemany(sql, (s))
            conn.commit()
        except:
            print("insert_courses_table error")
            conn.rollback()
            return False
        finally:
            cursor.close()
            conn.close()
        return True
    # 删除表中一个元素
    @staticmethod
    def delete_course_table(course):
        if type(course)!=Course:
            return False
        sql="DELETE FROM COURSE WHERE course_name= %s and course_type= %s and platform_name= %s"
        conn = set_conect()
        cursor = conn.cursor()
        try:
            cursor.execute(sql,(course.course_name, course.course_type,course.platform_name))
            conn.commit()
        except:
            print("delete_course_table error")
            conn.rollback()
            return False
        finally:
            cursor.close()
            conn.close()
        return True

    # 删除表中所有元素
    @staticmethod
    def delete_all_course_table():
        sql = "DELETE FROM COURSE;"
        conn = set_conect()
        cursor = conn.cursor()
        try:
            cursor.execute(sql)
            conn.commit()
        except:
            print("delete_all_course_table error")
            conn.rollback()
            return False
        finally:
            cursor.close()
            conn.close()
        return True

    # 删除表中一个元素(id)
    @staticmethod
    def delete_course_table2(id):
        if id==None:
            return False
        sql = "DELETE FROM COURSE WHERE course_id= %s "
        conn = set_conect()
        cursor = conn.cursor()

        try:
            cursor.execute(sql, (id))
            conn.commit()
        except:
            print("delete_course_table2 error")
            conn.rollback()
            return False
        finally:
            cursor.close()
            conn.close()
        return True

    #修改表中的一个元素(类)
    @staticmethod
    def update_course_table(id,course):
        if id==None:
            return False
        if course==None:
            return False
        sql = "UPDATE COURSE SET course_name=%s,course_type=%s,course_url=%s,platform_name=%s WHERE course_id= %s "
        conn = set_conect()
        cursor = conn.cursor()

        try:
            cursor.execute(sql, (course.course_name,course.course_type,course.course_url,course.platform_name,id))
            conn.commit()
        except:
            print("update_course_table error")
            conn.rollback()
            return False
        finally:
            cursor.close()
            conn.close()
        return True


    #查找课程名,输入课程名,返回课程类的数组
    @staticmethod
    def select_course_name(course_name):
        if course_name==None:
            return None
        if course_name=="":
            return []
        sql="SELECT * FROM COURSE WHERE course_name like %s or course_name like %s or course_name like %s or course_name= %s;"
        courses = []
        conn = set_conect()
        cursor = conn.cursor()
        try:
            cursor.execute(sql, ('%'+course_name+'%','%'+course_name,course_name+'%',course_name))
            result=cursor.fetchall()
            conn.commit()

            for row in result:
                c=Course(course_name=row[1],course_type=row[2],course_url=row[3],platform_name=row[4])
                c.id=row[0]
                courses.append(c)

        except:
            print("select_course_name error")
            return None
        finally:
            cursor.close()
            conn.close()

        return courses

    #查找平台类型,输入课程类型,返回课程类的数组
    @staticmethod
    def select_course_type(course_type):
        if course_type==None:
            return None
        if course_type=="":
            return []
        sql = "SELECT * FROM COURSE WHERE course_type like %s or course_type like %s or course_type like %s or course_type = %s;"
        courses = []
        conn = set_conect()
        cursor = conn.cursor()
        try:
            cursor.execute(sql, ('%'+course_type+'%',course_type+'%',course_type+'%',course_type))
            conn.commit()
            result = cursor.fetchall()
            for row in result:
                c=Course(course_name=row[1],course_type=row[2],course_url=row[3],platform_name=row[4])
                c.id = row[0]
                courses.append(c)
        except:
            print("select_course_type error")
            return None
        finally:
            cursor.close()
            conn.close()

        return courses
    #查找平台,输入平台名,返回课程类的数组
    @staticmethod
    def select_platform_name(platform_name):
        if platform_name==None:
            return None
        if platform_name=="":
            return []
        sql = "SELECT * FROM COURSE WHERE platform_name like %s or platform_name like %s or platform_name like %s or platform_name= %s;"
        courses = []
        conn = set_conect()
        cursor = conn.cursor()
        try:
            cursor.execute(sql, ('%'+platform_name+'%',platform_name+'%','%'+platform_name,platform_name))
            conn.commit()
            result = cursor.fetchall()
            for row in result:
                c=Course(course_name=row[1],course_type=row[2],course_url=row[3],platform_name=row[4])
                c.id = row[0]
                courses.append(c)
        except:
            print("select_platform_name error")
            return None
        finally:
            cursor.close()
            conn.close()

        return courses
    #查找所有,返回课程类的数组
    @staticmethod
    def select_all_course():
        sql = "SELECT * FROM COURSE;"
        courses = []
        conn = set_conect()
        cursor = conn.cursor()
        try:
            cursor.execute(sql)
            conn.commit()
            result = cursor.fetchall()
            for row in result:
                c = Course(course_name=str(row[1]), course_type=str(row[2]), course_url=str(row[3]), platform_name=str(row[4]))
                c.id = row[0]
                courses.append(c)
        except:
            print("select_all_course error")
            return None
        finally:
            cursor.close()
            conn.close()

        return courses


    #查找平台,输入平台名,返回课程类的数组
    @staticmethod
    def select_platform_course_name(platform_name,course_name):
        if platform_name==None or course_name==None:
            return None
        if course_name=="":
            return None
        sql = "SELECT * FROM COURSE WHERE platform_name = %s and (course_name like %s or course_name like %s or course_name like %s or course_name= %s);"
        courses = []
        conn = set_conect()
        cursor = conn.cursor()
        try:
            cursor.execute(sql, (platform_name,'%'+course_name+'%','%'+course_name,course_name+'%',course_name))
            conn.commit()
            result = cursor.fetchall()
            for row in result:
                c=Course(course_name=row[1],course_type=row[2],course_url=row[3],platform_name=row[4])
                c.id = row[0]
                courses.append(c)
        except:
            print("select_platform_name error")
            return None
        finally:
            cursor.close()
            conn.close()

        return courses
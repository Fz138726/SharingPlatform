from flask_db import db
from user_db import user_db
import WebWorm_bilibili
from app8_getIMooc import getInfoFromImmocForPython
from app9_getIMoocJava import getInfoFromIMoocForJava
import aiqiyi
from model import User,Course
initcourses=[]
mylist=[]
#表的数据初始化
def initcourse():
    #db.drop_course_table()
    db.init_course_table()
    mylist=getInfoFromImmocForPython()
    db.insert_courses_table(mylist)
    mylist=getInfoFromIMoocForJava()
    db.insert_courses_table(mylist)
    #mylist = WebWorm_bilibili.worm_bilibili_python()
    #db.insert_courses_table(mylist)
    #mylist=WebWorm_bilibili.worm_bilibili_java()
    #db.insert_courses_table(mylist)
    #mylist=WebWorm_bilibili.worm_bilibili_C()
    #db.insert_courses_table(mylist)
    #mylist=WebWorm_bilibili.worm_bilibili_Pr()
    #db.insert_courses_table(mylist)
    #mylist=WebWorm_bilibili.worm_bilibili_PS()
    #db.insert_courses_table(mylist)
    #mylist=aiqiyi.aiqiyi_Python()
    #db.insert_courses_table(mylist)
    db.insert_courses_table(initcourses)

    return  db.select_all_course()

#初始化用戶
def inituser():
    user_db.drop_user_table()
    user_db.init_user_table()
    user_db.insert_user_table(User(username="1ray",password="1ray",name="ray",detail=""))

#按鈕名称初始化
def initcoursetypes():
    return ["JAVA","Python","PS","PR","iOS","C","化学","高数","物理"]

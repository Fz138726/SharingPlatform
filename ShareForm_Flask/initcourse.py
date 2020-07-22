from flask_db import db
from user_db import user_db
from model import User,Course
initcourses=[]
mylist=[]
#表的数据初始化
def initcourse():
    return  db.select_all_course()

#初始化用戶
def inituser():
    user_db.drop_user_table()
    user_db.init_user_table()
    user_db.insert_user_table(User(username="1ray",password="1ray",name="ray",detail=""))

#按鈕名称初始化
def initcoursetypes():
    return ["JAVA","Python","PS","PR","iOS","C","化学","高数","物理"]

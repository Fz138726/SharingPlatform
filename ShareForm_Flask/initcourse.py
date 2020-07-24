from ShareForm_Flask.flask_db import db
from ShareForm_Flask.user_db import user_db
from ShareForm_Flask.model import User

initcourses=[]
mylist=[]
#表的数据初始化
def initcourse():
    db.init_course_table()
    return  db.select_all_course()

#初始化用戶
def inituser():
    user_db.drop_user_table()
    user_db.init_user_table()
    user_db.insert_user_table(User(username="1ray",password="1ray",name="ray",detail=""))

#按鈕名称初始化
def initcoursetypes():
    return ["JAVA","Python","PS","PR","iOS","C","C#","JAVA","Python"]

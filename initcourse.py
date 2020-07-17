from model import Course
from flask_db import db

initcourses=[]
#表的数据初始化
def initcourse():
    course1 = Course(course_name="PYTHON", course_type="PYTHON", course_url="https//www.4399.com", platform_name="4399")
    course2 = Course(course_name="C++", course_type="C", course_url="https//www.7k7k.com", platform_name="7k7k")
    course3 = Course(course_name="JAVA", course_type="C", course_url="https//www.google.com", platform_name="4399")
    initcourses.append(course1)
    initcourses.append(course2)
    initcourses.append(course3)
    db.drop_course_table()
    db.init_course_table()
    db.insert_courses_table(initcourses)
    return  db.select_all_course()
#按鈕名称初始化
def initcoursetypes():
    return ["JAVA","Python","PS","PR","iOS"]
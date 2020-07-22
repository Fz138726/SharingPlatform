import aiqiyi
import app8_getIMooc
import app9_getIMoocJava
import app10_getIMoocCSharp
import app11_getIMoocCPlusPlus
import app12_getIMoocSpringBoot
import app13_getIMoocPHP
import app14_getIMoocDesign
import app16_getYoukuTed
import app18_getYoutubePython
import WebWorm_bilibili
from flask_db import db


if __name__ == '__main__':
    db.drop_course_table()
    db.init_course_table()
    mylist =app8_getIMooc.getInfoFromImmocForPython()
    db.insert_courses_table(mylist)
    mylist = app9_getIMoocJava.getInfoFromIMoocForJava()
    db.insert_courses_table(mylist)
    mylist = WebWorm_bilibili.worm_bilibili_python()
    db.insert_courses_table(mylist)
    mylist=WebWorm_bilibili.worm_bilibili_java()
    db.insert_courses_table(mylist)
    mylist=WebWorm_bilibili.worm_bilibili_C()
    db.insert_courses_table(mylist)
    mylist=WebWorm_bilibili.worm_bilibili_Pr()
    db.insert_courses_table(mylist)
    mylist=WebWorm_bilibili.worm_bilibili_PS()
    db.insert_courses_table(mylist)
    mylist=aiqiyi.aiqiyi_Python()
    db.insert_courses_table(mylist)
    mylist=app10_getIMoocCSharp.getInfoFromIMoocForCSharp()
    db.insert_courses_table(mylist)
    mylist=app11_getIMoocCPlusPlus.getInfoFromIMoocForCPlusPlus()
    db.insert_courses_table(mylist)
    mylist=app13_getIMoocPHP.getInfoFromIMoocForPHP()
    db.insert_courses_table(mylist)
    mylist=app16_getYoukuTed.getInfoFromTedForChina()
    db.insert_courses_table(mylist)

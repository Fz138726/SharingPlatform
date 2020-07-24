from ShareForm_Flask.flask_db import db
from ShareForm_Flask.user_db import user_db
from ShareForm_Flask.model import Course,User

import unittest
#安全性测试
class DBTest(unittest.TestCase):
    # 每个单元测试前都可先初始化数据库
    @classmethod
    def setUpClass(self):

        db.init_course_table()
        user_db.init_user_table()

    # 每个单元测试后删除表
    @classmethod
    def tearDownClass(self):
        db.drop_course_table()
        user_db.drop_user_table()

    def test_course(self):
        a = Course(course_name="这是一个测试", course_type="ss", course_url="4399", platform_name="")
        b = Course(course_name="这是一个测试", course_type="sss", course_url="4399d", platform_name="rt")
        s = [a, b]
        db.insert_courses_table(s)
        #c=COurse(course_name=)
        self.assertTrue(db.insert_course_table(Course(course_name="s", course_type="ss", course_url="757", platform_name="1);DROP ALL TABLE--")))
        self.assertEqual(db.select_all_course()[0].course_name,a.course_name)
        db.delete_all_course_table()
        a = Course(course_name="TABLE", course_type="ss", course_url="4399", platform_name="1);DROP ALL TABLE--")
        b = Course(course_name="ALL", course_type="sss", course_url="4399d", platform_name="1);DROP ALL TABLE--")
        s = [a, b]
        self.assertTrue(db.insert_courses_table(s))
        self.assertEqual(db.select_all_course()[0].course_name, a.course_name)
        self.assertTrue(db.delete_course_table(b))
        self.assertEqual(db.select_all_course()[0].course_name, a.course_name)
        db.drop_course_table()
        db.init_course_table()
        a = Course(course_name="TABLE", course_type="ss", course_url="4399", platform_name="1);DROP TABLE if exists COURSE;--")
        b = Course(course_name="ALL", course_type="sss", course_url="4399d", platform_name="1);DROP TABLE if exists COURSE;--")
        s = [a, b]
        db.insert_courses_table(s)
        self.assertFalse(db.delete_course_table2("1);DROP ALL TABLE--"))
        self.assertEqual(db.select_all_course()[0].course_name,a.course_name)
        self.assertTrue(db.update_course_table(1,Course(course_name="TABLE", course_type="ss", course_url="4399", platform_name="1);DROP TABLE if exists COURSE;--")))
        self.assertEqual(db.select_course_name("5);DROP TABLE if exists COURSE;--"),[])
        self.assertEqual(db.select_course_type("5);DROP TABLE if exists COURSE;--"),[])
        self.assertEqual(db.select_platform_name("5);DROP TABLE if exists COURSE;--"),[])
        self.assertEqual(db.select_course_type_accuracy("5);DROP TABLE if exists COURSE;--"),[])
        self.assertEqual(db.select_platform_course_name("s","5);DROP TABLE if exists COURSE;--"),[])

    def test_user(self):
        a = User(username="1ray", password="sss", name="ray", detail="")
        b = User(username="2ray", password="sss", name="ray", detail="")
        s = [a, b]
        c=User(username="3ray", password="sss", name="ray", detail="1);DROP TABLE if exists USER--")
        self.assertTrue(user_db.insert_users_table(s))
        self.assertTrue(user_db.insert_user_table(c))
        user_db.drop_user_table()
        user_db.init_user_table()
        s.append(c)
        self.assertTrue(user_db.insert_users_table(s))
        self.assertFalse(user_db.delete_user_table2("1);DROP TABLE if exists USER--"))
        self.assertTrue(user_db.update_user_table(1,c))
        self.assertEqual(user_db.select_user_name("1ray);DROP TABLE if exists USER--"),None)
        self.assertEqual(user_db.select_password("1ray","sss);DROP TABLE if exists USER--"),None)
        self.assertEqual(user_db.select_user("1ray","sss);DROP TABLE if exists USER--"),None)


if __name__=='__main__':
    unittest.main()
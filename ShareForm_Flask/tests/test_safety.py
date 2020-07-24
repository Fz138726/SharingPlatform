from ShareForm_Flask.flask_db import db
from ShareForm_Flask.user_db import user_db
from ShareForm_Flask.model import Course

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
        #db.



if __name__=='__main__':
    unittest.main()
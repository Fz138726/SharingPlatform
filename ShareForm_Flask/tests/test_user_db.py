from ShareForm_Flask.user_db import user_db
from ShareForm_Flask.model import User
import unittest

class DBTest2(unittest.TestCase):
    # 每个单元测试前都可先初始化数据库
    @classmethod
    def setUpClass(self):

        user_db.init_user_table()

    @classmethod
    def tearDownClass(self):
        user_db.drop_user_table()

    # 每次测试前都会把表里元素清空
    def setUp(self):
        user_db.delete_all_user_table()

    #插入数据
    #正常输入
    def test_insert1(self):
        a=User(username="1ray",password="sss",name="ray",detail="")
        self.assertTrue(user_db.insert_user_table(a))
    #用戶名为17位
    def test_insert2(self):
        a = User(username="1ddddddddddddddddddddddddddddddday", password="sss", name="ray", detail="")
        self.assertFalse(user_db.insert_user_table(a))
    #输入为None
    def test_insert3(self):
        self.assertFalse(user_db.insert_user_table(None))
    #输入錯誤
    def test_insert4(self):
        self.assertFalse(user_db.insert_user_table("None"))

    #插入多条数
    #正常输入
    def test_insertmany1(self):
        a = User(username="1ray", password="sss", name="ray", detail="")
        b = User(username="2ray", password="sss", name="ray", detail="")
        s=[a,b]
        self.assertTrue(user_db.insert_users_table(s))
    #插入已有用戶名
    def test_insertmany2(self):
        a = User(username="1ray", password="sss", name="ray", detail="")
        b = User(username="1ray", password="sss", name="ray", detail="")
        s = [a, b]
        self.assertFalse(user_db.insert_users_table(s))

    #不正常输入
    def test_insertmany3(self):
        a = User(username="1ray", password="sss", name="ray", detail="")
        b = User(username="2rssssssssssssssssssssssssssssssssay", password="sss", name="ray", detail="")
        s=[a,b]
        self.assertFalse(user_db.insert_users_table(s))
    #输入为NOne
    def test_insertmany4(self):
        self.assertFalse(user_db.insert_users_table(None))
    #输入为[]
    def test_insertmany5(self):
        self.assertFalse(user_db.insert_users_table([]))
    # 输入数组其中有一个是None
    def test_insertmany6(self):
        a = User(username="1ray", password="sss", name="ray", detail="")
        b = None
        s=[a,b]

        self.assertFalse(user_db.insert_users_table(s))

    #删除数据id
    #正常输入
    def test_deleteid1(self):
        a = User(username="1ray", password="sss", name="ray", detail="")
        b = User(username="2ry", password="sss", name="ray", detail="")
        s = [a, b]
        user_db.insert_users_table(s)
        self.assertTrue(user_db.delete_user_table2(1))

    #不正常输入
    def test_deleteid2(self):
        a = User(username="1ray", password="sss", name="ray", detail="")
        b = User(username="2ry", password="sss", name="ray", detail="")
        s = [a, b]
        user_db.insert_users_table(s)
        self.assertTrue(user_db.delete_user_table2(10))
        # 不正常输入
    #输入为None
    def test_deleteid3(self):
        a = User(username="1ray", password="sss", name="ray", detail="")
        b = User(username="2ry", password="sss", name="ray", detail="")
        s = [a, b]
        user_db.insert_users_table(s)
        self.assertFalse(user_db.delete_user_table2(None))


    #删除全部
    #正常删除
    def test_deleteall1(self):
        a = User(username="1ray", password="sss", name="ray", detail="")
        b = User(username="2ry", password="sss", name="ray", detail="")
        s = [a, b]
        user_db.insert_users_table(s)
        self.assertTrue(user_db.delete_all_user_table())
    #表为空时删除
    def test_deleteall(self):
        self.assertTrue(user_db.delete_all_user_table())

    #更新数据
    #更新密码
    #正常输入
    def test_updatepassword1(self):
        a = User(username="1ray", password="sss", name="ray", detail="")
        b = User(username="2ry", password="sss", name="ray", detail="")
        s = [a, b]
        user_db.insert_users_table(s)
        self.assertTrue(user_db.update_user_password(1,"ssss"))
    #不正常输入
    def test_updatepassword2(self):
        a = User(username="1ray", password="sss", name="ray", detail="")
        b = User(username="2ry", password="sss", name="ray", detail="")
        s = [a, b]
        user_db.insert_users_table(s)
        self.assertTrue(user_db.update_user_password(1,"ssssdskkkdjjdnvnkskd11s"))

    #输入为none
    def test_updatepassword3(self):
        a = User(username="1ray", password="sss", name="ray", detail="")
        b = User(username="2ry", password="sss", name="ray", detail="")
        s = [a, b]
        user_db.insert_users_table(s)
        self.assertFalse(user_db.update_user_password(None,"ss"))
        self.assertFalse(user_db.update_user_password(1, None))
        self.assertFalse(user_db.update_user_password(None, None))
    #更新用戶数据
    #正常输入
    def test_update(self):
        a = User(username="1ray", password="sss", name="ray", detail="")
        b = User(username="2ry", password="sss", name="ray", detail="")
        s = [a, b]
        user_db.insert_users_table(s)
        c=User(username="2ry", password="sss", name="rddday", detail="13132")
        self.assertTrue(user_db.update_user_table(1,c))
    #不正1确输入
    def test_update2(self):
        a = User(username="1ray", password="sss", name="ray", detail="")
        b = User(username="2ry", password="sss", name="ray", detail="")
        s = [a, b]
        user_db.insert_users_table(s)
        c = User(username="2ry", password="sss", name="rdsday", detail="13132")
        self.assertTrue(user_db.update_user_table(9, c))
    #输入为None
    def test_update3(self):
        a = User(username="1ray", password="sss", name="ray", detail="")
        b = User(username="2ry", password="sss", name="ray", detail="")
        s = [a, b]
        user_db.insert_users_table(s)
        c = User(username="2ry", password="sss", name="rdsday", detail="13132")
        self.assertFalse(user_db.update_user_table(None, None))
        self.assertFalse(user_db.update_user_table(1, None))
        self.assertFalse(user_db.update_user_table(None, c))

    #查询测试
    #查询用戶
    def test_selectusername1(self):
        a = User(username="1ray", password="sss", name="ray", detail="")
        b = User(username="2ry", password="sss", name="ray", detail="")
        s = [a, b]
        user_db.insert_users_table(s)
        self.assertEqual(user_db.select_user_name("1ray"),a.username)
    #沒有查询失败
    def test_selectusername2(self):
        a = User(username="1ray", password="sss", name="ray", detail="")
        b = User(username="2ry", password="sss", name="ray", detail="")
        s = [a, b]
        user_db.insert_users_table(s)
        self.assertEqual(user_db.select_user_name("ray"), None)
    #输入为空
    def test_selectusername3(self):
        self.assertEqual(user_db.select_user_name(None), None)
    #查询密码
    def test_selectpassword1(self):
        a = User(username="1ray", password="sss", name="ray", detail="")
        b = User(username="2ry", password="sss", name="ray", detail="")
        s = [a, b]
        user_db.insert_users_table(s)
        self.assertEqual(user_db.select_password("1ray","sss"), "sss")
    #d查询失败
    def test_selectpassword2(self):
        a = User(username="1ray", password="sss", name="ray", detail="")
        b = User(username="2ry", password="sss", name="ray", detail="")
        s = [a, b]
        user_db.insert_users_table(s)
        self.assertEqual(user_db.select_password("2ry","ssss"), None)
        self.assertEqual(user_db.select_password("1ra","ssss"),None)
    #输入为NONE
    def test_selectpassword3(self):
        self.assertEqual(user_db.select_password(None,"sss"), None)
        self.assertEqual(user_db.select_password("sss", None), None)
        self.assertEqual(user_db.select_password(None, None), None)

    #查询用戶

    def test_selectuser1(self):
        a = User(username="1ray", password="sss", name="ray", detail="")
        b = User(username="2ry", password="sss", name="ray", detail="")
        s = [a, b]
        user_db.insert_users_table(s)
        self.assertEqual(user_db.select_user("1ray", "sss").username, "1ray")
    #输入錯误
    def test_selectuser2(self):
        a = User(username="1ray", password="sss", name="ray", detail="")
        b = User(username="2ry", password="sss", name="ray", detail="")
        s = [a, b]
        user_db.insert_users_table(s)
        self.assertEqual(user_db.select_user("1ray", "ss"), None)
        self.assertEqual(user_db.select_user("1ry", "ss"), None)
        self.assertEqual(user_db.select_user("1ry", "ss"), None)
    #输入为None
    def test_selectuser3(self):
        self.assertEqual(user_db.select_user(None, "ss"), None)
        self.assertEqual(user_db.select_user("1ry", None), None)
        self.assertEqual(user_db.select_user(None,None), None)

if __name__=='__main__':
    unittest.main()

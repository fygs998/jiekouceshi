import unittest
import requests
from base.denglu import *


class TestDengLu(unittest.TestCase):
    def setUp(self):
        self.s = requests.session()

    def test01(self):
        """正确的账号密码"""
        s = requests.session()
        a = denglu(s, "123123123123", "123123123123")
        # print(a)
        login_result = is_denglu_sucess(a)
        print("登录的结果判断：%s"%login_result)
        self.assertTrue(login_result)

    def test02(self):
        """错误的账号，正确的密码"""
        s = requests.session()
        a = denglu(s, "1231231231ccc23", "123123123123")
        # print(a)

        login_result = is_denglu_sucess(a)
        print("登录的结果判断：%s" % login_result)
        self.assertFalse(login_result)

if __name__=="__main__":
    unittest.main()
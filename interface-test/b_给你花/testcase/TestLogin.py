#!/usr/bin/python
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

import unittest
import requests
import ddt
from api.LoginApi import LoginApi
from tools.log import logger

@ddt.ddt
class TestLogin(unittest.TestCase): 
  
    def setUp(self):
        self.session = requests.session()
        self.ip = 'http://192.168.0.110/money/index.php?m=User&a=login'

    def tearDown(self):
        self.session.close()
    
    # @ddt.unique()
    # @ddt.add_test()
    # @ddt.feed_data()
    # @ddt.idata()
    # @ddt.is_trivial()
    # @ddt.mk_test_name()
    # @ddt.wraps()
    # @ddt._add_tests_from_data()
    # @ddt._get_test_data_docstring()

    @ddt.file_data('../data/user_data.json')
    # @ddt.data(
    #     {"phone":"15607076696","code":"111111","expect":"登录成功"},
    #     {"phone":"1560707669","code":"111111","expect":"手机号不符合规范"},
    #     {"phone":"15607076690","code":"111111","expect":"用户不存在,请先注册!"},
    #     {"phone":"15607076696","code":"","expect":"短信验证码输入有误"}
    # )
    @ddt.unpack
    def test_login(self,phone,code,expect):
        login_api = LoginApi()
        data = {'phone':phone,'code':code,'type':'login'}
        result = login_api.login(session=self.session,data=data)
        print(result)
        try:
            self.assertIn(expect,result)
        except Exception as e:
            logger.error(e)

if __name__== '__main__':
    unittest.TestProgram()
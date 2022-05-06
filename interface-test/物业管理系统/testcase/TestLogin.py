#!/usr/bin/python

import json
import os
import sys
import unittest
import requests,ddt

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

from api.LoginApi import LoginApi
from tools.log import logger

@ddt.ddt
class TestLogin(unittest.TestCase):
    def setUp(self):
        self.session = requests.session()
        self.url = 'http://192.168.0.110:8080/wuyeApi'

    @ddt.data({"username":13000000000,"password":"123456"})
    @ddt.unpack
    def test1_login(self,username,password):
        params = {'username':username,'password':password}
        resp = LoginApi.login(self.session,self.url + '/login',params)
        print(resp)
        global token
        token = resp.get("content").get("token")
        try:
            self.assertIn('success',json.dumps(resp))
        except Exception as e:
            logger.error(e)
    
    def test2_get_account(self,username=13699886845):
        data = {'username':username}
        resp = LoginApi.get_account(session=self.session,url=self.url + '/getAccountInfo',data=data,headers={'Authorization':token})
        print(resp)
        try:
            self.assertIn('success',json.dumps(resp))
        except Exception as e:
            logger.error(e)
        
    def tearDown(self):
        self.session.close()

if __name__ == '__main__':
    unittest.TestProgram()
    

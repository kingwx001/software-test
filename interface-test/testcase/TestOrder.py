#!/usr/bin/python
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

import unittest,requests
from api.OrderApi import OrderApi
from api.LoginApi import LoginApi 

class TestOrder(unittest.TestCase):
    
    def setUp(self):
        self.session = requests.session()
        self.ip = 'http://192.168.0.110/money/index.php?m=Order&a=checkorder'
        self.data = {'phone':15607076696,'code':123456,'type':'login'} 
    
    def tearDown(self):
        self.session.close()

    def test_order(self):
        order_api = OrderApi()
        LoginApi().login(self.session)
        result = order_api.check_order(self.session,self.ip)

if __name__=='__main__': 
    unittest.main()
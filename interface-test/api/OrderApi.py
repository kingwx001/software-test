#!/usr/bin/python
import unittest,ddt,requests

from requests import Session

class OrderApi:
    # 检查订单
    def check_order(self,session:Session,url):
        resp = session.post(url=url)
        return resp.json()
        
    # 申请贷款
    def apply_loan(self,session:Session,url,data):
        resp = session.post(url=url,data=data)
        return resp.text
    
    
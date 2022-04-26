#!/usr/bin/python
from requests import Session

class LoginApi:
    def login(self,session:Session,url = 'http://192.168.0.110/money/index.php?m=User&a=login' ,data = {'phone':15607076696,'code':111111,'type':'login'}):
        resp = session.post(url=url,data=data)
        return resp.json()
    
    def logout(self):
        pass
    
    def mobile_login(self):
        pass
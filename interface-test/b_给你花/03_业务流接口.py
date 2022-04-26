from http import cookies
import json
import unittest,ddt,requests

class TestProcess(unittest.TestCase):

    def setUp(self):
        self.session = requests.session()
        self.ip = 'http://192.168.0.110/money'
        

    def teardown(self):
        self.session.close()
        
   
    def test1_login(self):
        url = '/index.php?m=User&a=login'
        phone = 12345678901
        code = 111111
        data = {'phone':phone,'code':code,'type':'login'} 
        resp = self.session.post(url=self.ip+url,data=data,\
                headers={'Content-Type': 'application/x-www-form-urlencoded'})
        print(resp.url)
        global cookies 
        cookies = resp.cookies
        expect = '登录'

        try:
            self.assertIn(expect,resp.json()['msg'])
        except Exception as e:
            print(e)
        print(json.loads(resp.text))
        
 
    def test2_check(self):
        data = {'phone':'15607076696','code':'111111','type':'login'}
        # 2.检查订单 
        url = "/index.php?m=Order&a=checkorder" 
        resp_dict = self.session.post(url=self.ip+url,cookies=cookies).json() 
        print(resp_dict)
        
    
    def test3_loan(self):
        url ='/index.php?m=Order&a=daikuan' 
        data = {'money':'7500','month':'6'} 
        resp_html = self.session.post(url=self.ip+url,data=data,cookies=cookies).text 
        
        # print(resp_html) # 断言：左边值(预期)是否在右边里面(实际) 
        try:
            self.assertIn('确认借款信息', resp_html) 
        except Exception as e:
            print(e)
        
    
    def test4_true(self):
        url = '/index.php?m=Order&a=daikuan&trueorder=1'
        data = {'money':'7500','month':'6'} 
        resp = self.session.post(url=self.ip+url,data=data,cookies=cookies)
        global ordernum 
        ordernum = resp.json()['payurl'].split('ordernum=')[1]
        
    
    def test5_commit(self):
        url = '/index.php?g=Pay&m=Index&a=index'
        params = {'ordernum':ordernum}
        resp = self.session.get(url=self.ip+url,params=params,cookies=cookies)
        self.assertIn('收银台',resp.text)
        print(resp.text)
        

if __name__ == '__main__':
    unittest.main()
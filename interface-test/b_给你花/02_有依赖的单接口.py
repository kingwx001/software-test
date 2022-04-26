import unittest,requests,ddt 
# 有依赖的单接口 case 
class TestDaikuan(unittest.TestCase): 
    # 环境预设(创建本地会话对象、ip 地址、头信息) 
    def setUp(self): # 设置 fiddler 作为代理服务器
        self.proxies = {'http': '127.0.0.1:8888'} 
        # 打开会话 
        self.session = requests.session() 
        self.ip = "http://192.168.0.110/money" 
        self.headers = {'Content-Type':'application/x-www-form-urlencoded'} 
    # 申请贷款 

    def test_daikuan(self): # 1.先登录 
        data = {'phone':'15607076696','code':'111111','type':'login'} 
        self.session.post(url=self.ip+'/index.php?m=User&a=login',data=data) 
        # 2.检查订单 
        url = "/index.php?m=Order&a=checkorder" 
        resp_dict = self.session.post(url=self.ip+url).json() 
        print(resp_dict) # 3.申请贷款 
        url ='/index.php?m=Order&a=daikuan' 
        data = {'money':'7500','month':'6'} 
        resp_html = self.session.post(url=self.ip+url,data=data,headers=self.headers).text 
        
        print(resp_html) # 断言：左边值(预期)是否在右边里面(实际) 
        self.assertIn('确认借款信息', resp_html) # 环境恢复 
    
    def tearDown(self):
        pass # 主程序 
if __name__=='__main__': # unittest 执行测试 
    unittest.main()
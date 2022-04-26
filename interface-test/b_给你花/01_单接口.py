import json
import unittest
import requests
import ddt


# 使用unittest测试单接口
@ddt.ddt
class TestLogin(unittest.TestCase):

    def setUp(self): # 环境预设
        self.session = requests.session()
        self.ip = 'http://192.168.0.110/money'
        pass
    
    def tearDown(self): # 环境恢复
        self.session.close()
        pass
    @unittest.skip
    @ddt.data(
        {'phone':'15607076696','code':'111111','expect':'登录成功'}, 
        {'phone': '1560707669', 'code': '111111', 'expect': '手机号不符合规范'}, 
        {'phone':'15607076690','code':'111111','expect':'用户不存在,请先注册!'}, 
        {'phone':'15607076696','code':'','expect':'短信验证码输入有误'} 
    )
    @ddt.unpack
    def test_login(self,phone,code,expect):# 执行测试
        data = {'phone':phone,'code':code,'type':'login'} 
        resp = self.session.post(url=self.ip+'/index.php?m=User&a=login',data=data,\
                headers={'Content-Type': 'application/x-www-form-urlencoded'})
        try:
            self.assertIn(expect,resp.json()['msg'])
        except Exception as e:
            print(e)
        print(json.loads(resp.text))
        pass

if __name__ == '__main__':
    unittest.main()


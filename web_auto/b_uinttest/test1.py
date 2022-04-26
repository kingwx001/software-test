#!/usr/bin/env python
import unittest
from selenium import webdriver
'''
使用unittest单元测试框架:
1.自定义类来继承unittest.TestCase类
2.复写setUp()环境预设、tearDown()环境恢复的方法
3.自定义test开头的方法，作为测试用例
'''

x = "__name__"
print(x)
    
class MyTestCase(unittest.TestCase): # test方法的执行顺序按方法名的字母顺序
    def setUp(self):# 环境预设：打开浏览器访问网页。每个test方法之前都会执行一遍
        self.driver = webdriver.Chrome()
        self.driver.get(url=r'C:\htmltest\04_login.html')
        print('1.环境预设')
    def test_login3(self): # 测试用例 - 登录
        self.driver.find_element_by_id('accountID').send_keys('jackma') # 输入用户名
        self.driver.find_element_by_id('passwordID').send_keys('123456') # 输入密码
        self.driver.find_element_by_id('submitID').click() # 点击登录
        expect = '成功'
        actual = self.driver.find_element_by_xpath('//*[@id="divID"]/font').text
        # 断言：让计算机自动判断实际结果和预期是否相符合
        # self.assertEqual(expect,actual) # 断言失败会跑异常，当前方法体提前结束
        self.assertIn(expect,actual) # 判断包含关系，右边包含左边
        print('2.执行测试用例')
    @unittest.skip # 忽略
    def test_login2(self): # 测试用例 - 登录失败
        self.driver.find_element_by_id('accountID').send_keys('jackma')  # 输入用户名
        self.driver.find_element_by_id('passwordID').send_keys('1234567')  # 输入密码
        self.driver.find_element_by_id('submitID').click()  # 点击登录
        print('2.执行测试用例')
    def tearDown(self):# 环境恢复：关闭浏览器。每个test方法之后都会执行一遍
        print('3.环境恢复')
        import time
        time.sleep(5)
        self.driver.quit()
# 主程序
if __name__=='__main__':
    unittest.main() # 执行测试



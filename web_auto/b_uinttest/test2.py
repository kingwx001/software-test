#!/usr/bin/env python
import unittest
from selenium import webdriver
# 需求:定义测试用例类和测试方法
class MytestCase(unittest.TestCase): # unittest中方法的摆放没有顺序
    @classmethod
    def setUpClass(cls): # 环境预设，有n个测试方法也仅执行一次
        cls.driver = webdriver.Chrome()
        cls.driver.get(url=r'C:\htmltest\04_login.html')
    @classmethod
    def tearDownClass(cls): # 环境恢复，有n个测试方法也仅执行一次
        print('3.环境恢复')
        import time
        time.sleep(5)
        cls.driver.quit()
    def test_login(self):
        self.driver.find_element_by_id('accountID').send_keys('jackma')  # 输入用户名
        self.driver.find_element_by_id('passwordID').send_keys('123456')  # 输入密码
        self.driver.find_element_by_id('submitID').click()  # 点击登录
        expect = '成功'
        actual = self.driver.find_element_by_xpath('//*[@id="divID"]/font').text
        # 断言：让计算机自动判断实际结果和预期是否相符合
        # self.assertEqual(expect,actual) # 断言失败会跑异常，当前方法体提前结束
        self.assertIn(expect, actual)  # 判断包含关系，右边包含左边
        print('2.执行测试用例')
    def test_login_fail(self): # 测试用例 - 登录失败
        self.driver.find_element_by_id('accountID').send_keys('jackma')  # 输入用户名
        self.driver.find_element_by_id('passwordID').send_keys('1234567')  # 输入密码
        self.driver.find_element_by_id('submitID').click()  # 点击登录
        expect = '失败'
        actual = self.driver.find_element_by_xpath('//*[@id="divID"]/font').text
        # 断言：让计算机自动判断实际结果和预期是否相符合
        # self.assertEqual(expect,actual) # 断言失败会跑异常，当前方法体提前结束
        self.assertIn(expect, actual)  # 判断包含关系，右边包含左边
        print('2.执行测试用例')
# 主程序
if __name__=='__main__':
    unittest.main() # 执行测试


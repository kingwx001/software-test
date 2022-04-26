#!/usr/bin/env python
from selenium import webdriver # 引入驱动模块
import time
# 1.创建浏览器对象（会同时打开浏览器）。浏览器对象和真实浏览器是对应关系
driver = webdriver.Chrome()
# 2.访问地址
driver.get(url='https://wwww.baidu.com')
t = driver.title
print( t )  # 获取网页标题
print( driver.current_url ) # 获取网页地址
# 3.点击超链接
driver.find_element_by_link_text('hao123').click()






# 关闭网页
#driver.close()

time.sleep(5) # 等待5秒
# 退出浏览器
driver.quit()



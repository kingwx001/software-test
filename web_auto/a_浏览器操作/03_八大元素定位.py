#!/usr/bin/env python
from selenium import webdriver
# 创建浏览器对象（打开浏览器）
driver = webdriver.Chrome()
driver.get(url=r'C:\htmltest\01_autotest.html') # \n
# 1.通过id定位
uname = driver.find_element_by_id('accountID')
uname.send_keys('kobe')
# 2.通过name定位
pwd = driver.find_element_by_name('password')
pwd.send_keys('123456')
# 3.通过classname定位
driver.find_element_by_class_name('cpwd').send_keys('123456')
# 4.通过 tagname定位
citys = driver.find_elements_by_tag_name('option')
print( citys.__len__() ) # 4
print( citys[2].text ) # 获取深圳
citys[2].click() # 选中“深圳”
# 5.通过超链接文本定位
driver.find_element_by_link_text('全球最大的百度搜索').click()
# 6.通过部分超链接文本
driver.find_element_by_partial_link_text('360').click()
# 7.通过xpath定位
sex=driver.find_element_by_xpath('/html/body/form/table/tbody/tr[5]/td/input[2]')
sex.click()
# 8.通过css定位
hobby = driver.find_element_by_css_selector('#u3')
hobby.click()


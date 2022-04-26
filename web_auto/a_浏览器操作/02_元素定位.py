#!/usr/bin/env python
from selenium import webdriver
# 1.打开浏览器(创建浏览器对象)
driver = webdriver.Chrome()
# 2.访问网页
driver.get(url='https://www.so.com')
# 需求：搜索关键字 iphone 13
# 找输入框，然后输入关键字：iphone 13
input = driver.find_element_by_id('input')
input.send_keys('iphone 13')
# 找“搜索按钮”，然后点击
button = driver.find_element_by_id('search-button') # WebElement
# driver.find_elements_by_id() # List[WebElement]
button.click()

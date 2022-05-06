#!/usr/bin/python

import time
import unittest
from HTMLTestRunner import HTMLTestRunner


if __name__ == '__main__':
    test_suite = unittest.defaultTestLoader.discover(start_dir='./testcase/',pattern='Test*.py')
    report_path = f'./report/{time.strftime("%Y%m%d-%H%M%S")}.html'
    runner = HTMLTestRunner(stream=open(report_path,'wb'),title='物业管理系统测试报告',tester='夏敬武')
    runner.run(test_suite)
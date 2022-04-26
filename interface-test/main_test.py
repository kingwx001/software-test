#!/usr/bin/env python
from HTMLTestRunner import HTMLTestRunner
import time,unittest

if __name__ == '__main__':
    loader = unittest.defaultTestLoader.discover(start_dir='./testcase',pattern='Test*.py')
    path = './report/' + time.strftime('%Y%m%d%H%M%S') + '.html'
    runner = HTMLTestRunner(open(path,mode = 'wb'))

    runner.run(loader)


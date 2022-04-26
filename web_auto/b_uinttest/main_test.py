
import time
import unittest,sys,os
from HTMLTestRunner import HTMLTestRunner


if __name__ == '__main__':
    test_suit = unittest.defaultTestLoader.discover(start_dir='./',pattern='test1.py')
    report = open('./report/' + time.strftime('%Y%m%d-%H%M%S') + '.html','wb')
    runner = HTMLTestRunner(stream=report,title='飞猫商城测试',description='飞猫商城测试',tester='乌鸦哥')
    runner.run(test_suit)
    pass

#!/usr/bin/python
import logging.handlers
import os
logger = logging.getLogger()
logger.setLevel(logging.INFO)

format_str ='%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d] - %(message)s'
formatter = logging.Formatter(format_str)


hander = logging.handlers.TimedRotatingFileHandler(
    filename=f'{os.path.dirname(os.path.dirname(__file__))}/log/test.log',# 日志文件的路径
    when='H', # 日志文件的产生周期 
    backupCount= 3, 
    encoding='utf-8'
    ) 

# 封装好日志器：日志器封装处理器，处理器封装格式器 
logger.addHandler(hander) 
hander.setFormatter(formatter)

if __name__ == '__main__':
    logger.warning('警告级别的信息') 
    logger.info('信息级别的信息') 
    logger.debug('调试级别的信息...')
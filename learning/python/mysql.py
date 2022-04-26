# 导入pymysql模块

import pymysql
# 连接database
conn = pymysql.connect(host='localhost', user='root',password='root',database='test',charset='utf8')
# 得到一个可以执行SQL语句的光标对象
cursor = conn.cursor()
# cursor.execute('drop table if exists user1')
# # 定义要执行的SQL语句
# sql = """
# CREATE TABLE USER1 (
# id INT auto_increment PRIMARY KEY ,
# name CHAR(10) NOT NULL UNIQUE,
# age TINYINT NOT NULL
# )ENGINE=innodb DEFAULT CHARSET=utf8;
# """
# # 执行SQL语句
# cursor.execute(sql)
sql = "insert into user1 values(%s,%s,%s)"
insert = cursor.executemany(sql,[(4,'wen',20),(5,'tom',10),(6,'test',30)])
print(insert)
conn.commit()
# 关闭光标对象
cursor.close()
# 关闭数据库连接
conn.close()
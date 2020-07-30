'''
@Author: xyb
@Date: 2020-07-21 20:22:36
@LastEditTime: 2020-07-28 15:39:15
'''
#coding=utf-8
import pymysql

#1.创建连接对象
conn = pymysql.connect(host='localhost', port=3306, user='root', password='123456', database='book')

#2.获取游标对象
cursor = conn.cursor()

#SQL语句
sql = "select * from students;"
#3.执行SQL语句 返回值就是SQL语句在执行过程中影响的行数
row_count = cursor.execute(sql)
print("SQL语句执行影响的行数%d" % row_count)

#打印数据表中第一行数据
# print(cursor.fetchone())

#取出结果集中的所有数据
for line in cursor.fetchall():
    print(line)

#4.关闭游标
cursor.close()

#5.关闭连接
conn.close()



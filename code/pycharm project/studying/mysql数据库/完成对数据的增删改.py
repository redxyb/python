#coding=utf-8
import pymysql

#1.创建连接
conn = pymysql.connect(host='localhost', port=3306, user='root', password='123456', database='python')

#2.获取游标对象
cursor = conn.cursor()

try:
    #添加语句
    #sql = "insert into students value (0,'黄誉',21,170,'男')"
    #修改语句
    #sql = "update students set height=1.70 where name='黄誉'"
    #删除语句
    sql = "delete from students where id = 1"

    #3.执行sql语句
    row_count = cursor.execute(sql)
    print("SQL语句执行影响的行数：%d" % row_count)
    #提交到数据库
    conn.commit()

except Exception as e:
    #回滚数据，即撤销刚刚执行的SQL语句操作
    conn.rollback()

#4.关闭游标
cursor.close()

#5.关闭连接
conn.close()
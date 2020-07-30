#coding=utf-8
import pymysql

def main():
    #创建连接
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='123456', database='python')
    #获取游标对象
    cursor = conn.cursor()
    #执行SQL语句(插入10万条数据)
    for i in range(100000):
        cursor.execute("insert into test_index values('ha-%d')" % i)

    #提交数据
    conn.commit()

if __name__ == '__main__':
    main()
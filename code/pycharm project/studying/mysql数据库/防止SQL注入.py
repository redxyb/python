#coding=utf-8

import pymysql

def main():
    find_name = input("请输入姓名：")

    #创建Connection连接
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='123456', database='python')
    #获取游标对象
    cursor = conn.cursor()

    # 非安全的方式
    # 输入 ' or 1 = 1 or '   (单引号也要输入)
    # sql = "select * from students where name='%s'" % find_name
    # print("""sql===>%s<====""" % sql)
    # # 执行select语句，并返回受影响的行数：查询所有数据
    # count = cs1.execute(sql)

    # 安全的方式
    # 构造参数列表
    params = [find_name]
    # 执行select语句，并返回受影响的行数：查询所有数据
    count = cursor.execute("select * from students where name=%s", params)
    # 注意：
    # 如果要是有多个参数，需要进行参数化
    # 那么params = [数值1, 数值2....]，此时sql语句中有多个%s即可
    # %s 不需要带引号

    #打印受影响的行数
    print("SQL语句执行影响的行数：%d" % count)

    #打印查询结果
    result = cursor.fetchall()
    print(result)

    #关闭游标
    cursor.close()

    #关闭数据库连接
    conn.close()

if __name__ == '__main__':
    main()
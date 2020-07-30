#coding=utf-8
import json
import time
import pymysql
import logging
'''miniweb框架，负责处理动态资源请求'''

#获取首页信息
def index():
    #响应状态
    status = "200 OK";
    #响应头
    response_header = [("Server", "PWS2.0")]

    #打开文件读取数据
    # with open("template/index.html", "r") as file:
    #     file_data = file.read()
    with open("template/index.html", "rb") as file:
        file_data = file.read().decode('utf-8')
    #print(file_data)#for test

    # 处理后的数据，响应体
    data = time.ctime()
    response_body = file_data.replace("{%time%}", data)

    #读取MySQL数据库中的数据并显示
    #1.建立数据库连接
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='123456', database='shares_db')
    #2.获取游标对象
    cursor = conn.cursor()
    #3.执行mysql语句
    sql = "select * from info;"
    cursor.execute(sql)
    #4.获取数据结果
    result = cursor.fetchall()
    print(result)#for test
    #5.关闭游标
    cursor.close()
    #6.关闭数据库连接
    conn.close()

    data = ""
    for line in result:
        data += '''
        <tr>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td><input type="button" value="添加" id="toAdd" name="toAdd" systemidvaule="000007"></td>
        </tr>
        ''' % line
    response_body = response_body.replace("{%content%}", data)

    return status, response_header, response_body

#没有找到动态资源
def not_found():
    #响应状态
    status = "404 Not Found";
    #响应头
    response_header = [("Server", "PWS2.0")]
    #处理后的数据,响应体
    response_body = "not found"
    return status, response_header, response_body

#获取个人中心数据
def center():
    #响应状态
    status = "200 OK";
    #响应头
    response_header = [("Server", "PWS2.0")]

    #打开个人中心数据文件并读取
    with open("template/center.html", "rb") as file:
        file_data = file.read().decode('utf-8')
    # data = time.ctime()
    # #响应体
    # response_body = file_data.replace("{%content%}", data)

    #从数据库读取数据
    #1.连接数据库
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='123456', database='shares_db')
    #2.获取游标对象
    cursor = conn.cursor()
    #3.执行sql语句
    sql = '''select i.code, i.short, i.chg, 
             i.turnover, i.price, i.highs, f.note_info 
             from info as i inner join focus as f on i.id = f.info_id;'''
    cursor.execute(sql)
    #4.获取数据
    result = cursor.fetchall()
    #5.关闭游标
    cursor.close()
    #6.关闭连接
    conn.close()

    #个人中心数据列表
    center_data_list = list()
    #遍历每一行数据将其转换为字典
    for line in result:
        #创建一个空字典
        center_dict = dict()
        center_dict["code"] = line[0]
        center_dict["short"] = line[1]
        center_dict["chg"] = line[2]
        center_dict["turnover"] = line[3]
        center_dict["price"] = str(line[4])
        center_dict["hights"] = str(line[5])
        center_dict["note_info"] = line[6]
        #添加每个字典信息
        center_data_list.append(center_dict)

    # 把列表字典转成json字符串, 并在控制台显示
    json_str = json.dumps(center_data_list, ensure_ascii=False)
    print(json_str)

    return status, response_header, json_str

#定义路由表
route_list = [
    ("/index.html", index),
    ("/center.html", center),
]

#处理动态资源请求
def handle_request(env):
    #获取动态请求资源路径
    request_path = env["request_path"]
    print("接收到动态资源请求：", request_path)

    #遍历路由表，选择执行的函数
    for path, func in route_list:
        if request_path == path:
            result = func()
            return result
    else:
        logging.error("没有相应的路由：" + request_path)
        #没有找到动态资源
        result = not_found()
        return result

    # if request_path == "/index.html":
    #     #获取首页数据
    #     result = index()
    #     return result
    # elif request_path == "/center.html":
    #     result = center()
    #     return result
    # else:
    #     #没有找到动态资源
    #     result = not_found()
    #     return result
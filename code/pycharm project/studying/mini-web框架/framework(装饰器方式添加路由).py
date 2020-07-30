#coding=utf-8
import time
'''mini-web框架，负责处理动态资源请求'''

#定义一个路由表
route_list = []

def route(path):

    def decorate(func):
        #将路由信息添加到路由表
        route_list.append((path, func))

        def inner():
            return func()
        return inner
    #返回装饰器
    return decorate

#获取首页数据
@route('/index.html')
def index():
    #响应状态
    status = "200 OK";
    #响应头
    response_header = [("Server", "PWS2.0")]

    with open("template/index.html", "rb") as file:
        file_data = file.read().decode('utf-8')
    data = time.ctime()
    #响应体
    response_body = file_data.replace("{%content%}", data)
    return status, response_header, response_body

#获取个人中心信息
@route("/center.html")
def center():
    #响应状态
    status = "200 OK";
    #响应头
    response_header = [("Server", "PWS2.0")]

    with open("template/center.html", "rb") as file:
        file_data = file.read().decode('utf-8')
    data = time.ctime()
    #响应体
    response_body = file_data.replace("{%content%}", data)

    return status, response_header, response_body

#没有找到资源
def not_found():
    #响应状态
    status = "404 Not Found";
    #响应头
    response_header = [("Server", "PWS2.0")]
    with open("template/error.html", "rb") as file:
        file_data = file.read().decode('utf-8')
    #响应体
    response_body = file_data

    return status, response_header, response_body

def handle_request(env):
    #获取动态资源请求路径
    request_path = env["request_path"]
    print("接收到的动态资源请求：",request_path)

    #遍历路由表，选择执行的函数
    for path, func in route_list:
        if request_path == path:
            result = func()
            return result
    else:
        #没有找到动态资源
        result = not_found()
        return result
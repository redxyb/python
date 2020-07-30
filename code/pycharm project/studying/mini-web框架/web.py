#coding=utf-8
import socket
import threading
import sys
import framework
import logging

#logging日志的配置
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s:%(message)s',
                    filename="log.txt",
                    filemode='w'
                    )

#定义web服务器类
class HttpWebServer(object):
    def __init__(self):
        #1.创建一个服务器套接字
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #2.设置端口复用，使程序关闭立即释放端口
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        #3.绑定服务器地址
        server_socket.bind(SERVER_ADDR)
        #4.设置监听
        server_socket.listen(128)
        #5.保存创建的服务器套接字
        self.server_socket = server_socket

    @staticmethod
    def handle_client(client_socket):
        #接收客户端发来的请求信息
        recv_data = client_socket.recvfrom(1024)[0].decode('utf-8')
        print(recv_data)
        if len(recv_data) == 0:
            print("关闭浏览器了")
            client_socket.close()
            return

        #对接收的信息进行分割，获得请求资源路径信息
        request_list = recv_data.split(" ", maxsplit=2)
        request_path = request_list[1]
        print(request_path) #for test

        #判断路径是否为根目录，如果满足，指定为首页
        if request_path == "/":
            request_path = "/index.html"

        #判断是否是动态资源请求
        if request_path.endswith(".html"):
            '''这里是动态资源请求，把请求信息交给框架处理'''
            logging.info("动态资源请求：" + request_path)

            #字典存储用户请求信息
            env = {
                "request_path" : request_path
            }

            #获取处理结果
            status, headers, response_body = framework.handle_request(env)

            #使用框架处理的数据拼接响应报文
            #响应行
            response_line = "HTTP/1.1 %s\r\n" % status
            #响应头
            response_header = ""
            #遍历头部信息
            for header in headers:
                #拼接多个响应头
                response_header += "%s: %s\r\n" % header
            response_data = (response_line + response_header + "\r\n" + response_body).encode('utf-8')

            #发送数据
            client_socket.send(response_data)
            #关闭socket
            client_socket.close()

        else:
            '''这里是静态资源请求'''
            logging.info("静态资源请求：" + request_path)

            try:
                #打开请求资源文件
                with open("static" + request_path, "rb") as file:
                    file_data = file.read()
            except Exception as e:
                '''访问资源不存在，返回404数据'''
                #响应行
                response_line = "HTTP/1.1 Not Found\r\n"
                #响应头
                response_header = "Server:PWS1.0\r\n"
                #打开404数据文件
                with open("static/error.html", "rb") as file:
                    file_data = file.read()
                #响应体
                response_body = file_data
                #拼接响应报文
                response_data = (response_line + response_header + "\r\n").encode('utf-8') + response_body
            else:
                #响应行
                response_line = "HTTP/1.1 OK\r\n"
                #响应头
                response_header = "Server:PWS1.0\r\n"
                #响应体
                response_body = file_data
                #拼接响应报文
                response_data = (response_line + response_header + "\r\n").encode('utf-8') + response_body
            finally:
                client_socket.send(response_data)
                client_socket.close()

    def start(self):
        while True:
            #等待接受客户端的连接请求
            client_socket, client_addr = self.server_socket.accept()
            #创建一个子线程
            sub_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
            #将子线程设置为主守护线程
            sub_thread.setDaemon(True)
            sub_thread.start()

def main():
    #1.创建web服务器对象
    web_server = HttpWebServer()
    web_server.start()

#设置服务器地址信息
SERVER_ADDR = (IP, PORT) = ("", 8000)

if __name__ == '__main__':
    main()


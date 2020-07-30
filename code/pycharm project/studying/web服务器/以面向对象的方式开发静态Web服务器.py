#coding=utf-8
import socket
import threading

class HttpWebServer(object):
    def __init__(self):
        #1.创建服务器socket
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #2.设置端口复用，使程序结束之后立即释放端口
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        #3.绑定端口
        server_socket.bind(SERVER_ADDR)
        #4.设置监听
        server_socket.listen(128)
        #5.保存创建成功的服务器套接字
        self.server_socket = server_socket

    @staticmethod
    def handle_client(client_socket):
        #1.接收客户端的请求信息并解码
        recv_data = client_socket.recvfrom(4096)[0].decode('utf-8')
        print(recv_data) #for test
        if len(recv_data) == 0:
            print("关闭浏览器了")
            client_socket.close()
            return
        #对信息进行分割，并提取客户端所要访问资源路径
        request_list = recv_data.split(" ", maxsplit=2)
        request_path = request_list[1].split()[0]
        #print(request_path) #for test

        # 判断请求是否为根目录，如果条件成立，指定首页数据返回
        # 访问请求没有指定文件，通过该判断返回首页数据
        if request_path == "/":
            request_path = "/index.html"

        try:
            #打开指定文件的资源
            with open("html" + request_path, "rb") as file:
                file_data = file.read()
        except Exception as e:
            # 如果要访问的资源不存在，返回404数据
            #响应行
            response_line = "HTTP/1.1 404 Not Found\r\n"
            #响应头
            response_header = "Server:1.1\r\n"
            with open("html/error.html", "rb") as file:
                file_data = file.read()
            #响应体
            response_body = file_data
            #拼接响应报文
            response_data = (response_line + response_header + "\r\n").encode('utf-8') + response_body
        else:
            #响应行
            response_line = "HTTP/1.1 0K\r\n"
            #响应头
            response_header = "Server：1.0\r\n"
            #响应体
            response_body = file_data
            #拼接响应报文
            response_data = (response_line + response_header + "\r\n").encode('utf-8') + response_body
        finally:
            #发送请求信息
            client_socket.send(response_data)
            client_socket.close()

    def start(self):
        while True:
            #等待接受客户端的连接请求
            client_socket, client_addr = self.server_socket.accept()
            #当客户端和服务器建立连接后，创建子线程
            sub_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
            #将子进程设置为主守护线程
            sub_thread.setDaemon(True)
            #启动子线程执行对应的任务
            sub_thread.start()


def main():
    #创建web服务器对象
    web_server = HttpWebServer()
    #启动web服务器进行工作
    web_server.start()

#设置服务器端口
SERVER_ADDR = (IP, PORT) = ("",8000)

if __name__ == '__main__':
    main()
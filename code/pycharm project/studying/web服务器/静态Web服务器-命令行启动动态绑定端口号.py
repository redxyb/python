#coding=utf-8
import socket, threading, sys
'''需要在Linux系统中运行'''

class HttpWebServer(object):
    def __init__(self, port):
        #1.创建服务器端套接字
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #2.设置端口复用，使程序结束立即释放该端口
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        #3.绑定端口
        server_socket.bind(("",port))
        #4.设置监听
        server_socket.listen(128)
        #5.保存创建的服务器套接字
        self.server_socket = server_socket

    @staticmethod
    def handle_client(client_socket):
        recv_data = client_socket.recvfrom(4096)[0].decode('utf-8')
        if len(recv_data) == 0:
            print("关闭浏览器了")
            client_socket.close()
            return

        print(recv_data)#for test
        request_list = recv_data.split(" ",maxsplit=2)
        request_path = request_list[1].split()[0]
        print(request_path)#for test

        if request_path == "/":
            request_path = "index.html"

        try:
            with open("html" + request_path, "rb") as file:
                file_data = file.read()
        except Exception as e:
            #请求资源不存在，返回404数据
            #响应行
            response_line = "HTTP/1.1 404 Not Found\r\n"
            #响应头
            response_header = "Server:1.0\r\n"
            with open("html/error.html", "rb") as file:
                file_data = file.read()
            #响应体
            response_body = file_data
            #拼接响应报文
            response_data = (response_line + response_header + "\r\n") + response_body
        else:
            #响应行
            response_line = "HTTP/1.1 OK\r\n"
            #响应体
            response_header = "Server:1.0\r\n"
            #响应体
            response_body = file_data
            #拼接响应报文
            response_data = (response_line + response_header + "\r\n").encode('utf-8') + response_body
        finally:
            client_socket.send(response_data)
            client_socket.close()


    def start(self):
        while True:
            #等待客户端的连接请求
            client_socket, client_addr = self.server_socket.accept()
            #当客户端与服务器建立连接后，创建子线程
            sub_thread = threading.Thread(target=self.handle_client,args=(client_socket,))
            #将子线程设置为主守护线程
            sub_thread.setDaemon()
            #启动子线程执行对应的任务
            sub_thread.start()

def main():
    print(sys.argv)
    #判断命令行参数是否等于2
    if len(sys.argv) != 2:
        print("执行命令如下：python3 xxx.py 8000")
        return
    #判断字符串是否是数字组成
    if sys.argv[1].isdigit():
        print("执行命令如下：python3 xxx.py 8000")
        return

    #获取终端命令行参数
    port = int(sys.argv[1])
    web_server = HttpWebServer(port)
    web_server.start()

if __name__ == '__main__':
    main()
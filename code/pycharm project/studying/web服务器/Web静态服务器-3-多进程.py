#coding=utf-8
import socket
import multiprocessing
import threading
import gevent
from gevent import monkey

def handle_client(client_socket):
    recv_data = client_socket.recvfrom(4096)[0].decode('utf-8')
    print(recv_data)#for test
    if len(recv_data) == 0:
        print("关闭浏览器了")
        client_socket.close()
        return

    #对客户端发来的信息进行分割，并取出访问需求路径
    request_list = recv_data.split(" ", maxsplit=2)
    #获取需求访问路径
    request_path = request_list[1].split()[0]

    # 判断请求是否为根目录，如果条件成立，指定首页数据返回
    # 访问请求没有指定文件，通过该判断返回首页数据
    if request_path == "/":
        request_path = "/index.html"

    try:
        #打开指定文件并读取信息
        with open("html" + request_path, "rb") as file:
            file_data = file.read()
        pass
    except Exception as e:
        #如果要访问的资源不存在，返回404数据
        #响应行
        response_line = "HTTP/1.1 404 Not Found\r\n"
        #响应头
        response_header = "Server:1.0\r\n"
        with open("html/error.html", "rb") as file:
            file_data = file.read()
        #响应体
        response_body = file_data
        #拼接响应报文
        response_data = (response_line + response_header + "\r\n").encode('utf-8') + response_body

    else:
        #响应行
        response_line = "HTTP/1.1 OK\r\n"
        #响应头
        response_header = "Server:1.0\r\n"
        #响应体
        response_body = file_data
        #拼接响应报文
        response_data = (response_line + response_header + "\r\n").encode('utf-8') + response_body

    finally:
        client_socket.send(response_data)
        client_socket.close()

def main():
    #1.创建一个服务器套接字
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #2.端口复用，使程序关闭之后立即释放端口
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,True)
    #3.绑定服务器地址
    server_socket.bind(SERVER_ADDR)
    #4.设置监听
    server_socket.listen(128)
    while True:
        client_socket, client_addr = server_socket.accept()
        #handle_client(client_socket)
        #1.多进程
        # p = multiprocessing.Process(target=handle_client, args=(client_socket,))
        # p.start()

        #2.多线程
        t = threading.Thread(target=handle_client, args=(client_socket,))
        #把创建的子线程设置为守护主线程：防止主线程无法退出
        t.setDaemon(True)
        t.start()

        #3.协程
        # 有IO才需要这一句
        # monkey.patch_all()
        # gevent.joinall([
        #     gevent.spawn(handle_client, client_socket),
        # ])


#设定服务器端口
SERVER_ADDR = (HOST, PORT) = ("", 8000)
#设置服务器服务静态资源的路径
DOCUMENTS_ROOT = './html'

if __name__ == '__main__':
    main()
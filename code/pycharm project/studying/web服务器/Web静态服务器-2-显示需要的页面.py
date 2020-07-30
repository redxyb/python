#coding=utf-8
import socket

def handle_client(client_socket):
    recv_data = client_socket.recvfrom(4096)[0].decode('utf-8')
    print(recv_data)
    #根据指定字符串进行分割，最大分割次数指定2
    request_list = recv_data.split(" ", maxsplit=2)

    #获取请求资源路径
    request_path = request_list[1].split()[0]
    #print(request_path)#for test

    #判断请求是否为根目录，如果条件成立，指定首页数据返回
    #访问请求没有指定文件，通过该判断返回首页数据
    if request_path == "/":
        request_path = "/index.html"

    try:
        #动态打开指定文件
        with open("html" + request_path, "rb") as file:
            #读取文件数据
            file_data = file.read()
    except Exception as e:
        #请求资源不存在，返回404数据
        #响应行
        response_line = "HTTP/1.1 404 Not Found\r\n"
        #响应头
        response_header = "Server:PWS1.0\r\n"
        with open("html/error.html", "rb") as file:
            file_data = file.read()
        #响应体
        response_body = file_data

        #拼接响应报文
        response_data = (response_line + response_header + "\r\n").encode('utf-8') + response_body
        # 发送数据
        # client_socket.send(response_data)

    else:
        #响应行
        response_line = "HTTP/1.1 OK\r\n"
        #响应头
        response_header = "Server:PWS1.0\r\n"
        #响应体
        response_body = file_data
        #拼接响应报文
        response_data = (response_line + response_header + "\r\n").encode('utf-8') + response_body
        # 发送数据
        # client_socket.send(response_data)

    finally:
        # 发送数据
        client_socket.send(response_data)
        # 关闭服务与客户端的套接字
        client_socket.close()

def main():
    #1.创建套接字
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #2.端口复用，使程序退出立即释放端口号
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    #3.绑定端口号
    server_socket.bind(SERVER_ADDR)
    #4.设置监听
    server_socket.listen(128)
    while True:
        client_socket, client_addr = server_socket.accept()
        handle_client(client_socket)
        client_socket.close()

#设置服务器地址
SERVER_ADDR = (ip, port) = ("",8000)
#设置服务器服务静态资源的路径
DOCUMENTS_ROOT = './html'

if __name__ == '__main__':
    main()
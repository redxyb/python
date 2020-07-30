#coding=utf-8

import socket

def handle_client(client_socket):
    recv_data = client_socket.recvfrom(1024)[0].decode('utf-8')
    print(recv_data)
    with open("html/kobe.html", "rb")as f:
        file_data = f.read()

    #响应行
    response_line = "HTTP/1.1 200 OK\r\n"

    #响应头
    response_header = "HTTP/1.1 200 OK\r\n"#200表示找到这个资源
    #response_header += "\r\n"#用一个空的行与body进行隔开

    #响应体
    response_body = file_data

    # 拼接响应报文
    response_data = (response_line + response_header + "\r\n").encode("utf-8") + response_body
    # 发送数据
    client_socket.send(response_data)

    #关闭服务器与客户端的套接字
    client_socket.close()

def main():
    '''作为程序的主程序入口'''
    #1.创建TCP服务器端套接字
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #2.设置端口号复用，程序退出立即释放端口
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    #3.绑定端口
    server_socket.bind(("", 7788))
    #4.设置监听
    server_socket.listen(128)
    while True:
        #等待接受客户端请求
        client_socket, client_addr = server_socket.accept()
        handle_client(client_socket)

if __name__ == '__main__':
    main()
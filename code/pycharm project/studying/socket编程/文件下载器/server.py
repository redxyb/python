from socket import *
import sys


def get_file_content(file_name):
    #获取文件内容
    try:
        with open(file_name,'rb') as f:
            content = f.read()
        return content
    except:
        print("没有该文件：%s" % file_name)

def main():
    #带参运行
    # if len(sys.argv) != 2:
    #     print("请按照如下方式运行：python3 xxx.py 7788")
    #     return
    # else:
    #     port = int(sys.argv[1])

    #1.创建一个socket
    tcp_server_socket = socket(AF_INET,SOCK_STREAM)

    #2.绑定ip和port
    tcp_server_socket.bind(('',7788))

    #3.listen使socket变为可以被动链接
    tcp_server_socket.listen(128)

    while True:
        #4.accept等待客户端连接
        client_socket,clientAddr = tcp_server_socket.accept()

        #5.接收/发送数据
        recv_data = client_socket.recvfrom(1024)
        file_name = recv_data[0].decode('utf-8')
        print("客户端%s请求下载的文件为：%s" %(clientAddr,file_name))
        file_content = get_file_content(file_name)

        # 发送文件的数据给客户端
        # 因为获取打开文件时是以rb方式打开，所以file_content中的数据已经是二进制的格式，因此不需要encode编码
        if file_content:
            client_socket.send(file_content)

        #关闭这个套接字
        client_socket.close()

    #6.关闭socket
    tcp_server_socket.close()

if __name__ == '__main__':
    main()
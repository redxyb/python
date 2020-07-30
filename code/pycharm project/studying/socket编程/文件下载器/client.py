from socket import *

def mian():
    #1.创建套接字
    tcp_client_socket = socket(AF_INET,SOCK_STREAM)

    #2.获取目的信息
    server_ip = input("请输入服务器IP：")
    server_port = input("请输入服务器port：")

    #3.连接服务器
    tcp_client_socket.connect((server_ip,int(server_port)))

    while True:
        #4.提示用户输入所要下载的文件名
        file_name = input("请输入你要下载的文件名：")
        if file_name == 'exit':
            break

        #5.向服务器发送文件名
        tcp_client_socket.send(file_name.encode('utf-8'))

        #6.客户端接收服务器端发来的文件信息
        recv_data = tcp_client_socket.recvfrom(10000000)#思考：如何根据文件自动控制传输数据大小

        #判断接收信息是否为空，不为空才开始创建文件并写入信息
        if recv_data:
            with open("[下载]"+file_name,'wb') as f:
                f.write(recv_data[0])

    # 7.关闭套接字
    tcp_client_socket.close()

if __name__ == '__main__':
    mian()
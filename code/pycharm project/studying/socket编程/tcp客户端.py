from socket import *
'''简单的一人一句聊天客户端'''

#创建socket
tcp_client_socket = socket(AF_INET,SOCK_STREAM)

#目的信息
server_ip = input("请输入服务器ip:")
server_port = input("请输入服务器port：")

#连接服务器
tcp_client_socket.connect((server_ip,int(server_port)))

#提示用户输入数据
while True:
    send_data = input("请输入要发送给服务器的数据：")
    if send_data == 'exit':
        break
    tcp_client_socket.send(send_data.encode('gbk'))

    # 接收对方发来的数据，控制最大接收1024个字节
    recv_data = tcp_client_socket.recvfrom(1024)
    print("接收到服务器端发来的数据为：",recv_data[0].decode('gbk'))

#关闭套接字
tcp_client_socket.close()
from socket import *
'''简单一人一句聊天服务器端'''

#1.创建socket
tcp_server_socket = socket(AF_INET,SOCK_STREAM)

#2.绑定一个ip和port
tcp_server_socket.bind(('',7788))

#3.listen使套接字变为可以被动链接
tcp_server_socket.listen(128)#参数：最大排队连接数量（默认值为100）

#4.accept等待客户端的链接
'''Return a new socket representing the connection, and the address of the client.
        For IP sockets, the address info is a pair (hostaddr, port).'''
client_socket,clientAddr = tcp_server_socket.accept()

#5.recv/send接收发送数据
while True:
    recv_data = client_socket.recvfrom(1024)
    print("接收到客户端%s发来的信息为：%s" %(clientAddr,recv_data[0].decode('gbk')))

    send_data = input("请输入你要发给客户端的信息：")
    client_socket.send(send_data.encode('gbk'))

#6.关闭套接字
client_socket.close()
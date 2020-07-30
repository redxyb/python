from socket import *
def main():
    #1.创建udp套接字
    udp_socket = socket(AF_INET,SOCK_DGRAM)

    #2.绑定本地的相关信息，如果一个网络程序不绑定，则系统会随机分配
    local_addr = ('',7788)#ip地址和端口号，ip一般不写，表示本机的任何一个ip
    udp_socket.bind(local_addr)

    while True:
        #3.等待接收对方发送的数据
        recv_data = udp_socket.recvfrom(1024)#1024表示本次接收的最大字节数

        #print(recv_data)#接收到的是一个元组，具体格式如下：(b'http://www.cmsoft.cn QQ:10865600', ('192.168.0.102', 7788))
        recv_msg = recv_data[0].decode('gbk',errors='strict')#发送过来消息的内容：初始为bytes类型，要用utf-8解码
        #recv_msg = recv_data[0].decode('gbk')#注意：如果是从Windows端发过来的中文消息（中文采用gbk编码再发送，英文直接发送），要采用gbk解码

        send_addr = recv_data[1]#发送消息主机地址元组（ip,port）
        send_addr_ip = recv_data[1][0]#发送消息主机ip地址

        #4.显示接收到的数据
        #b'xxxx':表示为bytes数据类型，数据主体内容在引号内，需要用utf-8解码
        print('%s发来消息:%s' % (send_addr_ip,recv_msg))

    #5.关闭套接字
    udp_socket.close()

if __name__ == '__main__':
    main()
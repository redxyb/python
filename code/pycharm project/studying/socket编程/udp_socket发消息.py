import socket

def main():

    #创建udp的套接字
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    #准备接收方地址
    dest_addr = ('192.168.43.232',7788)

    while True:
        #可以使用套接字收发送数据
        send_data = input("请输入要发送的数据：")
        if send_data == 'exit':
            break
        #udp_socket.sendto("要发送的数据",(对方的ip,对方的port))
        udp_socket.sendto(send_data.encode('gbk'),dest_addr)

    #关闭套接字
    udp_socket.close()

if __name__ == "__main__":
    main()

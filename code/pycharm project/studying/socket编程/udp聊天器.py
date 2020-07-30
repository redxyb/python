import socket
import time

'''发送多条消息，通过多次接收可将消息全部接收'''
'''bug:如果没有发送消息就直接去接收，程序会阻塞，无法继续执行'''

def send_msg(udp_socket):
    '''从键盘读取数据并发送'''
    #1.从键盘读取要发送的信息
    msg = input("请输入你要发送的消息：")
    #2.输入接收信息的主机IP地址
    dest_ip = input("请输入接收信息的主机IP地址：")
    #3.输入对方的port
    dest_port = input("请输入对方的端口号：")
    #4.数据发送
    udp_socket.sendto(msg.encode('utf-8'),(dest_ip,int(dest_port)))#端口号是数字，不是字符串

def recv_msg(udp_socket):
    '''接收并显示数据'''
    recv_data = udp_socket.recvfrom(1024)
    #数据分离与解码
    recv_ip = recv_data[1][0]
    msg = recv_data[0].decode('utf-8',errors='strict')
    if len(recv_data) <= 0:
        print("没有消息")
    print(">>>%s%s发来消息:%s" % (time.ctime(),recv_ip,msg))

def main():
    #1.创建套接字
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    #2.绑定本地端口
    udp_socket.bind(('',7788))
    while True:
        #3.选择功能
        print("=" * 30)
        print("1.发送信息")
        print("2.接收信息")
        print("=" * 30)
        op_num = input("请输入要操作的功能序号：")#从键盘读取的都是字符串

        #4.根据选择操作调用相应的函数
        if op_num == "1":
            send_msg(udp_socket)
        elif op_num == "2":
            recv_msg(udp_socket)
        else:
            print("你输入的有误，请重新输入！")
    socket_udp.close()

if __name__ == '__main__':
    main()
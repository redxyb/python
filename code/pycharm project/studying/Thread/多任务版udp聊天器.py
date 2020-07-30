#coding=utf-8
import socket
import threading

def recv_msg(udp_socket):
    while True:
        #1.接收信息
        recv_data = udp_socket.recvfrom(1024)
        #2.信息的解码与分离
        recv_ip = recv_data[1][0]
        msg = recv_data[0].decode('utf-8')
        print(">>>%s发来消息：%s" % (recv_ip, msg))

def send_msg(udp_socket,dest_ip,dest_port):
    while True:
        #1.从键盘读取要发送的信息
        msg = input("请输入要发送的信息：")
        # #2.从键盘输入目的的主机ip和端口
        # dest_ip = input("目的主机的ip：")
        # dest_port = input("目的主机的port：")
        udp_socket.sendto(msg.encode('utf-8'), (dest_ip,int(dest_port)))

def main():
    #1.创建socket
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    #2.绑定本地信息
    udp_socket.bind(('192.168.43.232', 7788))
    #2.从键盘输入目的的主机ip和端口
    dest_ip = input("目的主机的ip：")
    dest_port = input("目的主机的port：")
    #3.创建一个子线程来接收信息
    t1 = threading.Thread(target=recv_msg, args=(udp_socket,))
    t2 = threading.Thread(target=send_msg, args=(udp_socket, dest_ip, dest_port))
    t1.start()
    t2.start()
    #4.主线程来发送信息
    # send_msg(udp_socket)

if __name__ == '__main__':
    main()
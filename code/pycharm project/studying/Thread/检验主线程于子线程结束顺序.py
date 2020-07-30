#coding=utf-8
import threading
from time import sleep,ctime

def sing():
    for i in range(3):
        print("正在唱歌。。。%d" % i)
        sleep(1)

def dance():
    for i in range(3):
        print("正在跳舞。。。%d" % i)
        sleep(1)

if __name__ == '__main__':
    print('---开始---：%s' % ctime())

    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)

    t1.start()
    t2.start()

    #查看线程数量
    while True:
        length = len(threading.enumerate())
        print("当前运行的线程数为：%d" % length)
        if length <= 1:
            break

        sleep(0.5)

    #sleep(5)# 屏蔽此行代码，程序会立马结束;执行该代码，运行时间为5s
    print('---结束---:%s' % ctime())
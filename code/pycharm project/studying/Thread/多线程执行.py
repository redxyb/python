#coding=utf-8
import threading
import time

def saySorry():
    print("我错了")
    time.sleep(1)

if __name__ == '__main__':
    for i in range(5):
        t = threading.Thread(target=saySorry)
        t.start()#启动线程，即让线程开始执行（所有结果同时出来）
        #saySorry()#单线程执行：结果一条条出来
        '''1.可以明显看出使用多线程并发的操作，花费时间要短的多
        2.当调用start()时，才会真正的创建线程，并且开始执行
        '''
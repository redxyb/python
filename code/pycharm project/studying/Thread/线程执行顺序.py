#coding=utf-8
import threading
import time

'''多线程程序的执行顺序是不确定的。当执行到sleep语句时，线程将被阻塞（Blocked）,
到sleep结束后，线程进入就绪(Runnable)状态，等待调度。而线程调度将自动选择一个线程执行。
'''
class MyThread(threading.Thread):
    def run(self):#重写run方法
        for i in range(3):
            time.sleep(1)
            msg = "I am" + self.name + " @ " + str(i)#name属性中保存的是当前线程的名字
            print(msg)

def test():
    for i in range(5):
        t = MyThread()
        t.start()

if __name__ == '__main__':
    test()

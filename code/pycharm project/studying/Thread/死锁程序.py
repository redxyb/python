#coding=utf-8
import threading
import time

'''两个线程分别占有一部分资源并且同时等待对方的资源，就会造成死锁'''

class MyThread1(threading.Thread):
    def run(self):
        #对mutexA上锁
        mutexA.acquire()

        # mutexA上锁后，延时1秒，等待另外那个线程 把mutexB上锁
        print(self.name + '---do1---up---')
        time.sleep(1)
        #mutexA.release()#此处解锁A，线程2就可以顺利执行完，所有资源全部释放，从而线程1也得以执行完

        # 此时会堵塞，因为这个mutexB已经被另外的线程抢先上锁了
        mutexB.acquire()
        print(self.name + '---do1---down---')
        mutexB.release()

        #对mutexA解锁
        #mutexA.release()

class MyThread2(threading.Thread):
    def run(self):
        #对mutexB上锁
        mutexB.acquire()

        # mutexB上锁后，延时1秒，等待另外那个线程 把mutexA上锁
        print(self.name + '---do2---up---')
        time.sleep(1)

        # 此时会堵塞，因为这个mutexB已经被另外的线程抢先上锁了
        mutexA.acquire()
        print(self.name + '---do2---down---')
        mutexA.release()

        #对mutexB解锁
        mutexB.release()

mutexA = threading.Lock()
mutexB = threading.Lock()

if __name__ == '__main__':
    thread1 = MyThread1()
    thread2 = MyThread2()
    thread1.start()
    thread2.start()
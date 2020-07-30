import time,threading

'''如果多个线程同时对同一个全局变量操作，会出现资源竞争问题，从而导致数据结果会不正确'''

#假定这是你的银行存款：
balance = 0
#1.创建锁
lock = threading.Lock()

def chang_it(n):
    #现存后取，结果应该为0
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):#线程执行函数
    for i in range(1000000):
        #2.锁定
        # lock.acquire()#先获取锁
        # try:
            chang_it(n)#执行修改
        # finally:
              #3.释放锁
        #     lock.release()#释放锁

t1 = threading.Thread(target=run_thread,args=(5,))
t2 = threading.Thread(target=run_thread,args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)#理论上结果应该为0：由于线程的调度是由操作系统决定的，当t1,t2交替执行时，只要循环次数足够多，balance结果就不一定是0了

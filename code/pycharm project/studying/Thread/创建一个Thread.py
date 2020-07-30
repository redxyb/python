import time,threading


def loop():#定义新线程执行函数
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n+1
        print('thread %s >>> %s' % (threading.current_thread().name,n))
        time.sleep(1)#暂停1s
    print('thread %s ended.' % threading.current_thread().name)#新建立线程结束

print('thread %s is running...' % threading.current_thread().name)#主线程执行
t = threading.Thread(target=loop,name='LoopThread')#创建一个名为LoopThread的线程
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)#主线程结束


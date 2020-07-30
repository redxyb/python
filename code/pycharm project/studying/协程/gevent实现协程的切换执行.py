#coding=utf-8
import gevent
from gevent import monkey
import random
import time

# def f(n):
#     for i in range(n):
#         print(gevent.getcurrent(),i)
#         #用来模拟一个耗时操作，注意不是time模块
#         gevent.sleep(0)#没有耗时将会按g1,g2,g3顺序执行完
#
# g1 = gevent.spawn(f, 5)
# g2 = gevent.spawn(f, 4)
# g3 = gevent.spawn(f, 3)
# g1.join()
# g2.join()
# g3.join()


# 有耗时操作时需要
monkey.patch_all()  # 将程序中用到的耗时操作的代码，换为gevent中自己实现的模块

def coroutine_work(coroutine_name):
    for i in range(10):
        print(coroutine_name, i)
        time.sleep(random.random())#可用gevent.sleep()替代

gevent.joinall([
        gevent.spawn(coroutine_work, "work1"),
        gevent.spawn(coroutine_work, "work2")
])
#coding=utf-8
import time

def get_time(fn):
    def inner():
        start = time.time()
        fn()
        end = time.time()
        print("函数的执行时间：%f" % (end - start))
    return inner()

@get_time
def fun():
    for i in range(100000):
        print(i)
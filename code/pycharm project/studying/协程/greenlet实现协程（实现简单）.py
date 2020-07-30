#coding=utf-8
from greenlet import greenlet
import time

def work1():
    while True:
        print("---A---")
        gr2.switch()
        time.sleep(1)

def work2():
    while True:
        print("---B---")
        gr1.switch()
        time.sleep(1)

gr1 = greenlet(work1)
gr2 = greenlet(work2)

#切换到gr1中运行
gr1.switch()#不可缺少
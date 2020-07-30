#coding=utf-8
from multiprocessing import Process
import time,os

def run_proc():
    '''子进程要执行的代码'''
    print('子进程的进程号：%d' % os.getpid())
    #os.getpid():获取当前进程的进程号
    while True:
        print("---2---")
        time.sleep(1)

if __name__ == '__main__':
    '''创建子进程时，只需要传入一个执行函数和函数的参数，
    创建一个Process实例 ，并用start()启动'''
    process = Process(target=run_proc)
    process.start()

    print('父进程pid:%d' % os.getpid())#os.getpid():获取当前进程的进程号
    while True:
        print("+++1+++")
        time.sleep(1)
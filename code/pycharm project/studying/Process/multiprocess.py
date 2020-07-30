from multiprocessing import Process
import os

#子进程要执行的代码
def run_proc(name):#执行函数
    print("Run child process %s (%s)..." % (name,os.getpid()))

if __name__ == '__main__':
    print("Parent process %s" % os.getpid())
    p = Process(target=run_proc,args=('test',))#创建子进程：传入一个执行函数和函数的参数
    print("Child process will start")
    p.start()
    p.join()
    print('Child process end')

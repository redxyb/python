from multiprocessing import Pool
import os,time,random

def long_time_task(name):
    print("Run task %s (%s)..." % (name,os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print("Task %s run %0.2f seconds" % (name,(end - start)))

if __name__ == '__main__':
    print("Parent process %s" % os.getpid())
    p = Pool(4)#Pool默认大小为CPU的核数，如果你有8核CPU，你要至少提交9个子进程才能看到等待效果
    for i in range(6):
        p.apply_async(long_time_task,args=(i,))#向进程池添加任务
    print("Waiting for all subprocess done...")
    p.close()#调用之后就不能继续添加新的process
    p.join()
    print("All subprocess done")
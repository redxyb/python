import multiprocessing
import time

def action(a, b):  # 待会两个进程要执行的任务↓
    for i in range(30):  # 循环30次
        print(a, ' ', b)
        time.sleep(0.1)  # 等待0.1s

if __name__ == '__main__':  # 这行代码很重要，新建进程的时候都加上它！！原因不用管（我也不知道233）

    jc1 = multiprocessing.Process(target=action, args=('进程一', 0))  # 准备建立一个进程：multiprocessing.Process()
    jc2 = multiprocessing.Process(target=action, args=('进程二', 1))  # 再准备建立一个新进程，这是基本格式记住←
# 必要参数target:指定进程要执行的任务(这里是执行函数 action),必要参数args:直译成中文就是'参数'，顾名思义就是前面target的参数，即action的参数，注意args是个元组，所以args后的参数写成tuple元组格式。直接写target('进程一',0)一定报错的

    jc1.start()  # 将蓄势待发的jc1进程正式启动！！
    jc2.start()  # 同上...

    jc1.join()  # 等待进程jc1将任务执行完...
    jc2.join()  # ...
    print('jc1,jc2任务都已执行完毕')

    jc1.close()  # 彻底关闭进程jc1
    jc2.close()  # ...
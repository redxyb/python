import multiprocessing

#定义一个执行函数
def action(q):
        text = q.get()#获取管道里面的信息
        print('子进程接收到信息。。。')
        print(text)

if __name__ =='__main__':
    queue = multiprocessing.Queue()#创建一个进程通信通道
    process = multiprocessing.Process(target=action,args=(queue,))#创建子进程
    process.start()#启动子进程
    print('主进程准备发送数据。。。')

    text = input("请输入要传递的信息：")
    queue.put(text)

    process.join()
    process.close()
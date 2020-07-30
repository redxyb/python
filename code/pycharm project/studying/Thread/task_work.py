#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#可在两台电脑上测试：两台电脑必须连接在同一网络
import time, sys, queue
from multiprocessing.managers import BaseManager

# Create QueueManager
class QueueManager(BaseManager):
    pass

def do_task_work():
    # This QueueManger can only acquire Queues from network, so only name provided
    QueueManager.register('get_task_queue')
    QueueManager.register('get_result_queue')

    # Connect to server where task_master.py is running
    server_addr = '192.168.0.101'
    print('Connect to server %s ...' % server_addr)

    # authkey must be coordinated with task_master.py
    m = QueueManager(address=(server_addr, 5000), authkey=b'abc')

    # Connect to network
    m.connect()

    # Acquire queue objects
    task = m.get_task_queue()
    result = m.get_result_queue()

    # Read task from task_queue and write to result to result_queue
    for i in range(10):
        try:
            n = task.get(timeout=1)
            print('run task %d * %d...' % (n, n))
            r = '%d * %d = %d' % (n, n, n*n)
            time.sleep(1)
            result.put(r)
        except queue.Empty:
            print('Task queue is empty.')

    # All work done
    print('worker exit')

if __name__ == '__main__':
    do_task_work()
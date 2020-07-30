#可在两台电脑上测试：两台电脑必须连接在同一网络
import random, time, queue
from multiprocessing.managers import BaseManager

# Queue for send tasks
task_queue = queue.Queue()
# Queue for accept results
result_queue = queue.Queue()

# Create a QueueManager herited from BaseManager
class QueueManager(BaseManager):
    pass

def gettask():
    return task_queue

def getresult():
    return result_queue

def do_task_master():
    # Register the two queues to network, argument callable references to Queue object
    # QueueManager.register('get_task_queue', callable=lambda: task_queue)
    # QueueManager.register('get_result_queue', callable=lambda: result_queue)

    # When run under windows, it not support bind through lambda
    QueueManager.register('get_task_queue', callable=gettask)
    QueueManager.register('get_result_queue', callable=getresult)

    # Bind port to 5000, set authentication code as 'abc'
    manager = QueueManager(address=('192.168.0.101', 5000), authkey=b'abc')

    # Start queue
    manager.start()

    # Acquire Queue that used to access through network
    task = manager.get_task_queue()
    result = manager.get_result_queue()

    # Put some tasks into task Queue
    for i in range(10):
        n = random.randint(0, 10000)
        print('Put task %d...' % n)
        task.put(n)

    # Read result from result queue
    print('Try get results...')
    for i in range(10):
        try:
            r = result.get(timeout=10)
            print('Result: %s' % r)
        except queue.Empty:
            print('Result Queue is empty')

    # Close
    manager.shutdown()
    print('Master exit')

if __name__ == '__main__':
    do_task_master()
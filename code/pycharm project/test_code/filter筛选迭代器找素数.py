def _odd_iter():#生成从2开始间隔为2的自然数迭代器
    n = 1
    while True:
        n = n + 2
        yield n
def _not_divisible(n):#筛选函数，保留不能整除的，筛掉可以整除的，即倍数
    return lambda x : x % n > 0
def primes():
    yield 2
    it = _odd_iter()#获得初始序列
    while True:
        n = next(it)#取出序列第一个元素
        yield n
        it = filter(_not_divisible(n),it)#筛选序列中的素数并保存在序列中
#打印素数
for i in primes():
    if i < 20 :
        print(i)
    else:
        break


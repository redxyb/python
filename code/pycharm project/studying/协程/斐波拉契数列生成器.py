#coding=utf-8
'''只要在def中有yield关键字的就称为生成器'''
def fib(n):#不再是函数，而是生成器
    count = 0
    num1, num2 = 0, 1
    while count < n:
        num = num1
        num1, num2 = num2, num1 + num2
        count += 1
        yield num
    return 'done'

if __name__ == '__main__':
    f = fib(5)
    # for i in f:
    #     print(i)#返回值打印不出来
    '''用for循环调用generator时，发现拿不到generator的return语句的返回值。
    如果想要拿到返回值，必须捕获StopIteration错误，
    返回值包含在StopIteration的value中：'''
    while True:
        try:
            x = next(f)
            print("value:%d" % x)
        except StopIteration as e:
            print("生成器返回值：%s" % e.value)
            break
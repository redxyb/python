#coding=utf-8
class FibIterable(object):
    '''斐波拉契数列迭代器'''
    def __init__(self,n):
        self.n = n#指定生成前n个数
        self.count = 0#用来统计已经生成数字个数
        self.num1 = 0#斐波拉契数列第一个数
        self.num2 = 1#斐波拉契数列第二个数

    def __next__(self):
        '''被next()函数调用来获取下一个数'''
        if self.count <self.n :
            num = self.num1
            self.num1, self.num2 = self.num2, self.num1 + self.num2
            self.count += 1
            return num
        else:
            raise StopIteration

    def __iter__(self):
        '''迭代器的__iter__返回自身即可'''
        return self

if __name__ == '__main__':
    fib = FibIterable(10)
    for num in fib:
        print(num,end=' ')
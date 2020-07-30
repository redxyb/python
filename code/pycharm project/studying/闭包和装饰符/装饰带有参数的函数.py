#coding=utf-8
'''装饰带有参数和返回值的函数'''

def logging(fn):
    def inner(num1,num2):
        print("正在计算。。。")
        result = fn(num1,num2)
        return result
    return inner
@logging
def sum(num1,num2):
    result = num1 + num2
    return result

result = sum(1,2)
print(result)
#coding=utf-8

#添加输出日志的功能
def logging(fn):
    def inner(*args, **kwargs):
        print("--正在努力计算--")
        result = fn(*args, **kwargs)
        return result
    return inner

#使用语法糖装饰函数
@logging
def sum_num(*args, **kwargs):
    result = 0
    for value in args:
        result += value

    for value in kwargs.values():
        result += value

    return result

@logging
def subtraction(a, b):
    result = a - b
    print(result)

result = sum_num(1,2,3,4,a=5)
print(result)

subtraction(2,3)
#coding=utf-8

def fun_out(num1):
    #定义一个内部函数
    def fun_in(num2):
        #这里本意想要修改外部num1的值，实际上是在内部函数定义一个局部变量num1
        #num1 = 10

        nonlocal num1
        num1 = 10

        #内部函数使用了外部函数的变量（num1）
        result = num1 + num2
        print("结果是：%d" % result)

    #外部函数返回了内部函数，这里返回内部函数就是闭包
    return fun_in

#创建闭包实例
f = fun_out(1)
#执行闭包
f(2)
f(3)
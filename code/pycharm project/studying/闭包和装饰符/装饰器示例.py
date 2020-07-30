#coding=utf-8
#添加一个登录验证的功能
def check(fn):
    def inner():
        print("请先登录...")
        fn()
    return inner()
def comment():
    print("发表评论")

#使用装饰器来装饰函数
comment = check(comment)

#装饰器的基本雏形
# def decorator(fn):#fn:目标函数
#     def inner():
#         '''执行函数之前'''
#         fn()#执行被装饰的函数
#         '''执行函数之后'''
#     return inner
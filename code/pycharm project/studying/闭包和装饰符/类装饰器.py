#coding=utf-8
class check(object):
    def __init__(self, fn):
        #初始化操作
        self.__fn = fn

    def __call__(self, *args, **kwargs):
        #添加装饰功能
        print("请先登录...")
        self.__fn()

@check
def comment():
    print("发表评论")

comment()
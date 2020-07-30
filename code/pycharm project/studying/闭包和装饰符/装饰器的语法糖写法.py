#coding=utf-8
def check(fn):
    print("装饰器函数执行了")
    def inner():
        print("请先登录...")
        fn()
    return inner()

@check
def comment():
    print("发表评论")


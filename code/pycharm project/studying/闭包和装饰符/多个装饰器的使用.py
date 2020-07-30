#coding=utf-8

def make_div(fn):
    '''对被装饰器的函数的返回值 div标签'''
    def inner(*args, **kwargs):
        return "<div>" + fn() + "</div>"
    return inner

def make_p(fn):
    '''对被装饰的函数的返回值 p标签'''
    def inner(*args, **kwargs):
        return "<p>" + fn() +"</p>"
    return inner

@make_div
@make_p
#上面的顺序不同，结果相应改变
def content():
    return "人生苦短"

result = content()
print(result)#<div><p>人生苦短</p></div>
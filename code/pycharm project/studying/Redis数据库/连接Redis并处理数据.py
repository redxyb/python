#coding=utf-8
from redis import *

if __name__ == '__main__':
    try:
        #创建StrictRedis对象，与redis服务器建立连接
        sr = StrictRedis(host='localhost', port=6379, password='123456', db=0)
        #修改键：如果键已经存在就修改，不存在则添加
        #添加键name，值为xyb
        #result = sr.set('name', 'xyb')

        #获取键name
        #result = sr.get('name').decode('utf-8')

        #删除键：删除成功则返回受影响的键数，否则则返回0
        #result = sr.delete('name')

        #获取所有键:返回所有键构成的列表，如果没有键则返回空列表
        result = sr.keys()

        #输出响应结果，如果添加成功则返回True
        print(result)
    except Exception as e:
        print(e)
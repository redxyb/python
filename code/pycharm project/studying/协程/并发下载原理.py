#coding=utf-8
from gevent import monkey
import gevent
import urllib.request

#有耗时操作时需要
monkey.patch_all()

def my_download(file_name, url):
    print("GET:%s" % url)
    resp = urllib.request.urlopen(url)
    data = resp.read()
    #将接收到的数据存储到文件中
    with open(file_name, 'wb') as f:
        f.write(data)

    print("%d bytes received from %s." % (len(data),url))

gevent.joinall([
    gevent.spawn(my_download, 'baidu.html', 'http://www.baidu.com/'),
    gevent.spawn(my_download, 'itcast.html', 'http://www.itcast.cn/'),
    gevent.spawn(my_download, 'itheima.html', 'http://www.itheima.com/'),
])
#coding=utf-8
from gevent import monkey
import gevent
import urllib.request

#有IO才需要这一句
monkey.patch_all()

def download(file_name, url):
    resp = urllib.request.urlopen(url)
    data = resp.read()

    with open(file_name,'wb') as f:
        f.write(data)

    print("%s bytes received" % len(data))

gevent.joinall([
    gevent.spawn(download, '回到夏天.mp3', 'https://m10.music.126.net/20200717183940/f11b88490cd3fb34d82525afac4f4b11/ymusic/obj/w5zDlMODwrDDiGjCn8Ky/2600783032/980c/dcc8/b7b8/d36c65f90dace397bb3d1a49ea9b4800.mp3'),
    gevent.spawn(download, 'summertime.mp3', 'https://m10.music.126.net/20200717184610/c63409e34842984aff57d23ab4cc79f3/ymusic/obj/w5zDlMODwrDDiGjCn8Ky/2902489405/6ae5/73ab/cefa/2d0b0485ec0da1dca59be0f7996eb669.mp3'),
])
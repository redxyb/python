#coding=utf-8
import re
'''匹配出<html><h1>www.itcast.cn</h1></html>'''

labels = ["<html><h1>www.itcast.cn</h1></html>", "<html><h1>www.itcast.cn</h2></html>"]
for label in labels:
    #ret = re.match(r'<(\w*)><(\w*)>.*</\2></\1>', label)

    #对分组起别名，再引用别名匹配到字符串
    ret = re.match(r"<(?P<name1>\w*)><(?P<name2>\w*)>.*</(?P=name2)></(?P=name1)>",
                   label)
    if ret:
        print("%s 是符合要求的标签" % ret.group())
    else:
        print("%s 不符合要求" % label)
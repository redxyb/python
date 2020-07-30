#coding=utf-8
import re

ret = re.match("([^-]*)-(\d+)", "010-12345678")
print("区号为：%s" % ret.group(1))
print("电话号码为：%s" % ret.group(2))
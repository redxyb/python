#coding=utf-8
import re
#按冒号，逗号，分号，空格进行分割
ret = re.split(r":|,|;| ", "info:xiaoZhang 33 shandong,nihao;haha")
print(ret)
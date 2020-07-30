#coding=utf-8
'''匹配出163、126、qq的邮箱地址，且@符号之前有4到20位，例如hello@163.com'''
import re

email_list = ["xiaoWang@163.com", "xiaoWang@163.comheihei", ".com.xiaowang@qq.com", "test@qq.com"]

for email in email_list:
    ret = re.match('\w{4,20}@(163|126|qq)\.com$',email)
    if ret:
        print('%s 是符合规矩的邮箱，匹配后的结果为：%s' % (email, ret.group()))
    else:
        print('%s 不符合要求' % email)
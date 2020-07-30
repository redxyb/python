'''
@Descripttion: 
@Author: xyb
@Date: 2020-06-23 10:27:52
@LastEditTime: 2020-06-23 10:46:14
'''
from functools import reduce

def str2num(s):
    try:
        return int(s)
    except ValueError:
        return float(s)
    

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x,ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

main()
#打印ns：<map object at 0x000002135659C160>
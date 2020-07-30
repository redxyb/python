from functools import reduce
def str2float(s):
    DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    n = s.index('.')
    s1 = s[:n]
    s2 = s[n+1:]#取出整数部分的字符串
    s2 = s2[::-1]#将小数部分字符串转置
    def char2num(x):
        return DIGITS[x]
    def f1(x,y):
        return x*10 + y
    def f2(x,y):
        return x*0.1 + y
    return reduce(f1,map(char2num,s1)) + 0.1 * reduce(f2,map(char2num,s2))
print(str2float('456.09988'))
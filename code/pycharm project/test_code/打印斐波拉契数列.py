def fib(max):
    n,a,b = 0,0,1
    while n < max:
        print(b)
        a,b = b,a+b#赋值语句
        n = n+1
    return 'done'
fib(6)
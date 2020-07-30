'''
@Descripttion: 
@Author: xyb
@Date: 2020-06-13 16:47:54
@LastEditTime: 2020-06-13 17:01:40
'''
def move(n,a,b,c):
    if n == 1:
        print("a-->c") #如果只有1层，就直接输出：将盘子由a位置转到c位置，函数执行结束
    move(n-1,a,c,b)#将n-1个盘子由a位置转到b位置
    move(1,a,b,c)#将1个盘子由a位置转到c位置
    move(n-1,b,a,c) #将n-1个盘子由b位置转到c位置
    return #函数执行结束
move(3,"A","B","C")

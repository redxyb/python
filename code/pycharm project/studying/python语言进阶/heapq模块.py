import heapq
'''
（堆排序）
从列表中找出最大或最小的N个元素
堆结构（大根堆/小根堆）
'''
list1 = [34,25,12,99,87,63,58,78,88,92]
list2 = [
    {'name':'IBM','shares':100,'price':91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65},
]
print(heapq.nlargest(3,list1))#依次从大到小输出列表中最大三个值
print(heapq.nsmallest(3,list1))#依次从小到大输出列表中最小三个值
print(heapq.nlargest(2,list2,key=lambda x: x['price']))
print(heapq.nsmallest(2,list2,key=lambda x: x['shares']))
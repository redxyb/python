def by_name(t):#按名字排序
    return t[0]
def by_score(t):#按成绩由高到低排序
    return -t[1]
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
L1 = sorted(L,key=by_name)
print(L1)
L2 = sorted(L,key=by_score)
print(L2)
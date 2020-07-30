class A:
    def __init__(self):
        self.num1 = 100
        self.__num2 = 200
    def __test__(self):
        print("私有方法 %d %d" % (self.num1,self.__num2))

class B:
    pass

#创建一个子类对象
b = B()
print(b)
#在外界不能直接访问私有属性和方法
#print(b.__num2)
#b.test()

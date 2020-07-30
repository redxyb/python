class A:
    def __init__(self):
        self.num1 = 100
        self.__num2 = 200
    def __test(self):
        print("私有方法 %d  %d" % (self.num1,self.__num2))
    def test(self):
        print(self.num1)

class B(A):
    def demo(self):

        #1.访问父类的私有属性
        # print("访问父类的私有属性 %d" % self.__num2)
        #2.访问父类的私有方法
        # self.__test()
        #3.访问父类的公有属性
        print(self.num1)
        pass

#创建一个子类对象
b = B()
print(b)

b.demo()
print(b.num1)

#在外界不能直接访问父类对象的私有属性和方法
# print(b._num2)
# b.__test()
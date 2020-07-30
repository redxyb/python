class A:
    def test(self):
        print("A的test方法")
    def demo(self):
        print("A的demo方法")
    pass
class B:
    def test(self):
        print("B的test方法")
    def demo(self):
        print("B的demo方法")
    pass
class C(A,B):#交换两个父类的位置观察结果
    pass
c = C()

c.demo()
c.test()
print(C.__mro__)#查看调用方法
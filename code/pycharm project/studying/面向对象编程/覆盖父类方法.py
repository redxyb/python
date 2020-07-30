class Animal:
    def run(self):
        print("跑")
    def drink(self):
        print("喝")
class Dog(Animal):
    def bark(self):
        print("汪汪叫")

class XiaoTianQuan(Dog):
    def fly(self):
        print("哮天犬飞起来了")
    # def bark(self):
    #     print("叫得跟神一样")
    def bark(self):
        #1.针对子类特有得需求，编写代码
        print("叫得跟神一样")
        #2.使用super().调用原本在父类中封装得方法
        super().bark()
        Dog.bark(self)
        #3.增加其他子类的代码
        print("@#$#$!!#@$@$@#$")

xtq = XiaoTianQuan()
xtq.bark()
class Dog(object):

    @staticmethod
    def run():#静态方法不带默认参数
        print("小狗要跑。。。")

#调用静态方法
Dog.run()
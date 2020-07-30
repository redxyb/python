class MusicPlayer(object):
    #记录第一个被创建对象的引用
    instance = None
    init_flag = False
    def __new__(cls, *args, **kwargs):
        #1.判断类属性是否是空对象
        if cls.instance is None:
            #2.调用父类的方法为第一个对象分配空间
            cls.instance = super().__new__(cls)
        #3.返回类属性保存对象引用
        return cls.instance
    def __init__(self):
        if MusicPlayer.init_flag == False:
            print("初始化播放器")
            MusicPlayer.init_flag = True
        else:
            return

#1.创建多个对象
player1 = MusicPlayer()
print(player1)

player2 = MusicPlayer()
print(player2)
#多个对象的内存地址完全一致
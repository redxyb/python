import pygame
import random

SCREEN_RECT = pygame.Rect(0,0,480,700)#屏幕大小的常量
FRAME_PER_SEC = 60#刷新帧率常量
CREATE_ENEMY_EVENT = pygame.USEREVENT#敌机出现事件
MOVE_SPEED = 5#飞机移动速度
HERO_FIRE_EVENT = pygame.USEREVENT + 1#英雄发射子弹事件

class GameSprite(pygame.sprite.Sprite):
    '''飞机大战游戏精灵'''

    def __init__(self,image_name,speed = 1):
        super().__init__()#调用父类初始化方法
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        #在屏幕垂直方向移动
        self.rect.y += self.speed

class Background(GameSprite):
    '''游戏背景精灵'''

    def __init__(self,is_alt = False):
        #1.调用父类方法实现精灵创建
        super().__init__("D:/all_code/飞机大战/images/background.png")
        #2.判断是否是交替图像，如果是，需要设置初始位置
        if is_alt:#定义初始位置，实现背景图交替滚动
            self.rect.y = -self.rect.height

    def update(self):
        #1.调用父类的方法实现
        super().update()
        #2.判断是否移出屏幕
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height

class Enemy(GameSprite):
    '''敌机精灵'''
    def __init__(self):
        #1.调用父类方法，创建敌机精灵，同时指定敌机图片
        super().__init__("D:/all_code/飞机大战/images/enemy1.png")
        #2.指定敌机的初始随机速度:1-3
        self.speed = random.randint(1,3)
        #3.指定敌机的初始位置
        self.rect.bottom = 0
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0,max_x)

    def updata(self):
        #1.调用父类方法，保持垂直方向的飞行
        super().updata()
        #2.判断是否飞出屏幕，如果是，需要从精灵组删除敌机
        if self.rect.y >= SCREEN_RECT.height:
            #print("飞机飞出屏幕，需要从精灵组删除...")
            #kill方法可以将精灵从所有精灵组中移除，精灵就会自动销毁
            self.kill()

    # def __del__(self):#对原始__del__()方法重写
    #     #print('敌机挂了 %s' % self.rect)
    #     pass

class Hero(GameSprite):
    '''英雄飞机类'''
    def __init__(self,):
        #1.调用父类方法，创建英雄飞机，并指定英雄飞机图片#英雄飞机需要上下左右移动，所以初始速度设置为0
        super().__init__("D:/all_code/飞机大战/images/me1.png",0)
        #2.指定英雄飞机初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120
        #3.创建子弹的精灵组
        self.bullets = pygame.sprite.Group()
        # 添加爆炸效果
        self.bomb_image_list = []

    def update(self):
        #限定飞机不能移出屏幕
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right
        elif self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.bottom > SCREEN_RECT.height:
            self.rect.bottom = SCREEN_RECT.height

    def fire(self):
        for i in (0,1,2):#一次发射三颗子弹
            #1.创建子弹
            bullet = Bullet()
            #2.设置子弹初始位置
            bullet.rect.bottom = self.rect.y - i * 20#设置子弹垂直位置
            bullet.rect.centerx = self.rect.centerx#将子弹水平中心位置与英雄水平中心位置保持一致
            #3.将子弹加入子弹精灵组
            self.bullets.add(bullet)


class Bullet(GameSprite):
    '''子弹类'''
    def __init__(self):
        #调用父类初始化方法，创建子弹，并指定子弹图片
        super().__init__('D:/all_code/飞机大战/images/bullet1.png',-2)

    def update(self):
        #调用父类方法，让子弹沿垂直方向飞行
        super().update()
        #判断子弹是否飞出屏幕
        if self.rect.bottom < 0:
            self.kill()#会自动调用类中自带的__del__方法

    # def __del__(self):#可对该方法进行重写
    #     pass


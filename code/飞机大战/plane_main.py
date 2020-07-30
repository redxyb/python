import pygame
from plane_sprites import *
import sys
import time

SCREEN_RECT = pygame.Rect(0,0,480,700)#屏幕大小的常量
FRAME_PER_SEC = 60#刷新帧率常量
CREATE_ENEMY_EVENT = pygame.USEREVENT#敌机出现事件
MOVE_SPEED = 5#飞机移动速度

class PlaneGame(object):
    '''飞机大战主游戏'''
    def __init__(self):
        print("游戏初始化")
        # 创建游戏屏幕
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 创建时钟对象
        self.clock = pygame.time.Clock()
        #调用私有方法，精灵和精灵组创建
        self.__create_sprites()
        #设置定时器事件-创建敌机1s
        pygame.time.set_timer(CREATE_ENEMY_EVENT,1000)#毫秒为单位
        pygame.time.set_timer(HERO_FIRE_EVENT,500)#发射子弹事件

    def start_game(self):
        print("游戏开始...")
        # 音频初始化
        pygame.mixer.init()
        # 加载音频文件路径 (路径必须真实存在，音频文件格式支持mp3/ogg等格式)
        pygame.mixer.music.load('D:/all_code/飞机大战/images/信仰-张信哲.mp3')
        pygame.mixer.music.play()
        time.sleep(2)

        #music = pygame.mixer.Sound('D:/all_code/飞机大战/images/信仰-张信哲.mp3')
        # 游戏循环：正式开始游戏
        while True:
            #1.设置刷新帧率
            self.clock.tick(FRAME_PER_SEC)  # 设定循环内代码每秒执行次数
            #2.事件监听
            self.__event_handler()
            #3.碰撞检测
            self.__check_collide()
            #4.更新/绘制精灵组
            self.__updata_sprites()
            #5.更新屏幕图像
            pygame.display.update()

    #事件监听处理
    def __event_handler(self):
        for event in pygame.event.get():#获得所有监听事件

            #判断是否退出游戏
            if event.type == pygame.QUIT:
                PlaneGame.__game_over(self)
            elif event.type == CREATE_ENEMY_EVENT:#敌机生成事件
                # print('敌机出场...')
                #创建敌机精灵
                enemy = Enemy()
                #将敌机精灵加入到敌机精灵组
                self.enemy_group.add(enemy)
            elif event.type == HERO_FIRE_EVENT:#英雄开火事件
                self.hero.fire()

        #键盘监听：监听键盘是否被摁下（此处不使用事件监听）
        get_pressed = pygame.key.get_pressed()  # 各个按键状态的列表
        right = pygame.K_d  # 将字母d键设为飞机右移
        left = pygame.K_a  # 将字母a键设为飞机左移
        up = pygame.K_w  # 将字母w键设为飞机上移
        down = pygame.K_s  # 将字母s键设为飞机下移
        # 控制飞机上下左右移动
        if get_pressed[right] == 1:
            self.hero.rect.x += MOVE_SPEED
        elif get_pressed[left] == 1:
            if self.hero.rect.x < 0:
                self.hero.rect.x = 0
            self.hero.rect.x -= MOVE_SPEED
        elif get_pressed[up] == 1:
            self.hero.rect.y -= MOVE_SPEED
        elif get_pressed[down] == 1:
            self.hero.rect.y += MOVE_SPEED

    #碰撞检测
    def __check_collide(self):
        # #方法一
        # pygame.sprite.groupcollide(group1, group2, dokill1, dokill2, collided = None)#返回一个精灵字典
        #如果将 dokill 设置为 True，则 发生碰撞的精灵将被自动移除；collided 参数是用于计算碰撞的回调函数，如果没有指定，则每个精灵必须有一个 rect 属性
        # #方法二
        # pygame.sprite.spritecollide(sprite, group, dokill, collided = None)#返回一个精灵列表
        #1.子弹摧毁敌机
        result1 = pygame.sprite.groupcollide(self.hero.bullets,self.enemy_group,True,True)

        #2.敌机与英雄飞机相撞
        result2 = pygame.sprite.groupcollide(self.hero_group,self.enemy_group,True,True)
        if len(result2) > 0:
            #英雄牺牲
            self.hero.kill()
            #游戏结束
            PlaneGame.__game_over(self)

    #更新/绘制精灵组
    def __updata_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)
        self.hero_group.update()
        self.hero_group.draw(self.screen)
        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

    @staticmethod
    def __game_over(self):#静态方法
        print("游戏结束")
        pygame.quit()
        sys.exit()#不能直接写exit()

    #创建精灵
    def __create_sprites(self):

        #创建背景精灵和精灵组
        bg1 = Background()
        bg2 = Background(True)
        self.back_group = pygame.sprite.Group(bg1,bg2)

        #创建敌机的精灵组
        self.enemy_group = pygame.sprite.Group()

        #创建英雄精灵和精灵组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

if __name__ == '__main__':
    #创建游戏对象
    game = PlaneGame()
    #启动游戏
    game.start_game()
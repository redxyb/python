import pygame
from plane_sprites import *

#游戏初始化
pygame.init()
#创建一个游戏窗口
screen = pygame.display.set_mode((480,700))
#绘制游戏窗口背景图片
bg = pygame.image.load("D:/all_code/飞机大战/images/background.png")
screen.blit(bg,(0,0))
#绘制英雄飞机
hero = pygame.image.load("D:/all_code/飞机大战/images/me1.png")
screen.blit(hero,(200,500))
#更新屏幕画面
pygame.display.update()

#创建时钟对象
clock = pygame.time.Clock()
#1.定义rect记录飞机的初始位置
hero_rect = pygame.Rect(200,500,102,126)

#创建敌机精灵
enemy = GameSprite("D:/all_code/飞机大战/images/enemy1.png")
enemy1 = GameSprite("D:/all_code/飞机大战/images/enemy1.png",2)
#将敌机精灵加入到精灵组
enemy_group = pygame.sprite.Group(enemy,enemy1)


#游戏循环：意味着游戏开始
while True:
    clock.tick(60)#循环内的代码每秒执行60次
    #捕获事件,事件监听
    for event in pygame.event.get():
        #判断用户是否点击关闭按钮
        if event.type == pygame.QUIT:
            print("游戏退出...")
            #quit卸载所有模块
            pygame.quit()
            exit()#直接终止当前正在执行的程序

    #2.修改飞机的位置
    hero_rect.y -= 1
    #判断飞机的位置
    #if hero_rect.y + hero_rect.height <= 0:
    if hero_rect.bottom <= 0:
        hero_rect.y = 700
    #3.调用blit绘制飞机
    screen.blit(bg,(0,0))#遮挡前一次飞机图像
    screen.blit(hero,hero_rect)

    #让精灵组调用两个方法
    enemy_group.update()#让组中所有的精灵更新位置
    enemy_group.draw(screen)#在screen上绘制精灵组所有的精灵

    #4.更新屏幕
    pygame.display.update()

#关闭pygame调用的所有组件
pygame.quit()
import pygame

#需求：
# 1.定义hero_rect矩形描述英雄的位置和大小
hero_rect = pygame.Rect(100,500,120,125)
#2.输出英雄的坐标原点（x,y）
print("英雄的原点：%d %d" % (hero_rect.x,hero_rect.y))
#3.输出英雄的尺寸（宽度和高度）
print("英雄的尺寸：%d %d" % (hero_rect.width,hero_rect.height))
print("英雄的尺寸：%d %d" % hero_rect.size)
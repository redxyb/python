import pygame

pygame.init()

#创建游戏的窗口480 * 700
screen = pygame.display.set_mode((480,700))
#导入图片
background = pygame.image.load("D:/all_code/飞机大战/images/background.png")
#blit 绘制图像
screen.blit(background,(0,0))
#update 更新屏幕显示
pygame.display.update()

while True:
    pass

pygame.quit()
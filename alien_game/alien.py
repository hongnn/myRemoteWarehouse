import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self,alien_settings,screen):
        super(Alien,self).__init__()
        self.screen = screen
        self.alien_settings = alien_settings

        #加载外星人图像，设置rect属性

        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #让每个外星人都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image,self.rect)      #执行位置绘制外星人


    def update(self):
        #向左 / 右移动外星人
        self.x += (self.alien_settings.alienSpeedFactor * self.alien_settings.fleetDirection)
        self.rect.x = self.x

    def chekEdges(self):
        #外星人位于屏幕边缘就返回 true
        screenRect = self.screen.get_rect()
        if self.rect.right >= screenRect.right:
            return True
        elif self.rect.left <= 0:
            return True

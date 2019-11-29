import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    '''管理飞创发射子弹的类'''
    def __init__(self,alien_settings,screen,ship):
        '''在飞船的位置创建一个子弹'''
        super(Bullet,self).__init__()
        self.screen = screen
        #在（0,0）处创建一个表示子弹的矩形，再设置正确的位置
        self.rect = pygame.Rect(0,0,alien_settings.bulletWidth,alien_settings.bulletHeight)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)
        self.color = alien_settings.bulletColor
        self.speedFactor = alien_settings.bulletSpeedFactor

        self.makingBullet = False

    def update(self):
        '''向上移动子弹'''
        self.y -= self.speedFactor
        self.rect.y = self.y

        #更新表示 子弹的位置

    def drawBullet(self):
        '''在屏幕上绘制子弹'''
        pygame.draw.rect(self.screen,self.color,self.rect)





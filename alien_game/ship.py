import pygame

class Ship():
    def __init__(self,alien_settings,screen):
        '''初始化飞船，并设置初始位置'''
        self.screen=screen
        '''加载飞船图像'''
        self.Settings = alien_settings

        self.image=pygame.image.load('images/ship.bmp')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()

        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom

        self.center = float(self.rect.centerx)      #先允许接收小数
        self.movingRight=False
        self.movingLeft=False

    def update(self):
        '''如果movingRight是True，那么一直移动飞船'''
        if self.movingRight and self.rect.right < self.screen_rect.right:
            self.center +=self.Settings.shipSpeedFactor
        if self.movingLeft and self.rect.left > self.screen_rect.left:
            self.center -=self.Settings.shipSpeedFactor

        self.rect.centerx = self.center     #储存self.center 的整数部分

    def blitme(self):
        self.screen.blit(self.image,self.rect)


    def centerShip(self):
        self.center = self.screen_rect.centerx
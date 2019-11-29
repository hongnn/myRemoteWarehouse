import pygame
from pygame import font
class Button():
    def __init__(self,alien_setting,screen,msg):
        # 初始化按钮属性
        self.screen = screen
        self.screenRect = screen.get_rect()

        #设置按钮的尺寸和其他属性
        self.width,self.height = 200,50
        self.buttonColor = (0,255,0)
        self.textColor = (255,255,255)
        self.font = font.SysFont(None,48)

        # 创建按钮的rect对象，并使其居中
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.screenRect.center

        #该按钮的标签只需要创建一次
        self.prepMsg(msg)


    def prepMsg(self,msg):
        '''将msg渲染为图像，并使其在按钮上居中'''
        self.msgImage = self.font.render(msg,True,self.textColor,self.buttonColor)
        self.msgImageRect = self.msgImage.get_rect()
        self.msgImageRect.center = self.rect.center

    def drawButton(self):
        self.screen.fill(self.buttonColor,self.rect)
        self.screen.blit(self.msgImage,self.msgImageRect)



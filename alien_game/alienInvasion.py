import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
from button import Button
from bullet import Bullet

def runGame():
    pygame.init()
    alien_settings=Settings()
    screen=pygame.display.set_mode((alien_settings.screenWidth,alien_settings.screenHeight))  #设置游戏屏幕的尺寸
    pygame.display.set_caption('alien')
    playButton = Button(alien_settings,screen,"play")
    stats = GameStats(alien_settings)
    #alien = Alien(alien_settings,screen)    #创建一个外星人
    ship=Ship(alien_settings,screen)       #创建一艘飞船
    bullet = Bullet(alien_settings,screen,ship)
    bullets  = Group()          #创建一个用于储存子弹的数组
    aliens = Group()
    gf.createFleet(alien_settings,screen,ship,aliens)
    while True:
        gf.checkEvents(alien_settings,screen,stats,playButton,ship,aliens,bullets,bullet)    #响应按键和鼠标事件
        if stats.gameActive:
            ship.update()       #修改飞船的位置
            gf.fireBullet(alien_settings,screen,ship,bullets,bullet)
            gf.updateBullets(alien_settings,screen,ship,aliens,bullets)   #检查子弹，超过屏幕后把它删除
            gf.updateAliens(alien_settings,stats,screen,ship,aliens,bullets)

        gf.updateScreen(alien_settings,screen,stats,ship,aliens,bullets,playButton)     #重新绘制屏幕


runGame()
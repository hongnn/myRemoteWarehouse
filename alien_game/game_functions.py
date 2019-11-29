import sys
from time import sleep
import pygame
from ship import Ship
from settings import Settings
from bullet import Bullet
from alien import Alien


def checkKeydownEvents(event,alien_settings,screen,stats,playButton,ship,aliens,bullets,bullet):
    if event.key==pygame.K_RIGHT:       #向右移动飞船
        ship.movingRight=True
    elif event.key == pygame.K_LEFT:
        ship.movingLeft= True
    elif event.key == pygame.K_ESCAPE:
        sys.exit()

    elif event.key == pygame.K_SPACE:
        bullet.makingBullet = True
    elif event.key == pygame.K_p and  not stats.gameActive:     #按了p键并且游戏为非活跃状态
        alien_settings.initializeDynamicSettings()      #恢复游戏初始速度
        startGame(alien_settings,screen,stats,playButton,ship,aliens,bullets)

def fireBullet(alien_settings,screen,ship,bullets,bullet):     #没有达到子弹限制，就发射子弹
    if len(bullets) < alien_settings.bulletAllowed and bullet.makingBullet:
        newBullet = Bullet(alien_settings,screen,ship)
        bullets.add(newBullet)
        # bullet.makingBullet = False


def checkKeyupEvents(event,ship,bullet):
    if event.key == pygame.K_RIGHT:
        ship.movingRight = False
    elif event.key == pygame.K_LEFT:
        ship.movingLeft = False
    elif event.key == pygame.K_SPACE:
        bullet.makingBullet = False

def checkPlayButton(alien_settings,screen,stats,playButton,ship,aliens,bullets,mouseX,mouseY):
    '''检查是否点击 play 按钮，点击了就开始游戏'''
    if playButton.rect.collidepoint(mouseX,mouseY) and not stats.gameActive:
        pygame.mouse.set_visible(False)
        alien_settings.initializeDynamicSettings()      #恢复游戏的初始速度
        startGame(alien_settings,screen,stats,playButton,ship,aliens,bullets)     #开始游戏


def startGame(alien_settings,screen,stats,playButton,ship,aliens,bullets):
    stats.resetStats()
    stats.gameActive = True
    #清空外星人列表和子弹列表
    aliens.empty()      #清空外星人
    bullets.empty()     #清空子弹
    #创建一群外星人
    createFleet(alien_settings,screen,ship,aliens)
    ship.centerShip()   #飞船放置中央


def checkEvents(alien_settings,screen,stats,playButton,ship,aliens,bullets,bullet):
    '''响应案件和鼠标事件'''
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:      #检测鼠标单击屏幕事件
            mouseX,mouseY = pygame.mouse.get_pos()      #获取鼠标点击位置的坐标存储为数组
            checkPlayButton(alien_settings,screen,stats,playButton,ship,aliens,bullets,mouseX,mouseY)
        elif event.type==pygame.KEYDOWN:
            checkKeydownEvents(event,alien_settings,screen,stats,playButton,ship,aliens,bullets,bullet)
        elif event.type==pygame.KEYUP:
            checkKeyupEvents(event,ship,bullet)

'''控制飞船和子弹'''

def updateScreen(alien_settings,screen,stats,ship,aliens,bullets,playButton):
    screen.fill(alien_settings.bgColor)        #重新绘制屏幕颜色
    for bullet in bullets.sprites():
        bullet.drawBullet()
    ship.blitme()
    aliens.draw(screen)
    if not stats.gameActive:
        playButton.drawButton()
    pygame.display.flip()       #让最近绘制的屏幕可见

    #得到一行能展示多少外星人
def getNumberAliensX(alien_settings,alienWidth):
    avaliableSpaceX = alien_settings.screenWidth - 2 * alienWidth
    numberAliensX = int(avaliableSpaceX/(2 * alienWidth))
    return numberAliensX

    #计算可以容纳多少行外星人
def getNumberRows(alien_settins,shipHeight,alienHeight):
    avaliableSpaceY = (alien_settins.screenHeight - (3 * alienHeight) - shipHeight)
    numberRows = int(avaliableSpaceY/(2 * alienHeight))
    return numberRows

    #创建一个外星人并放在当前行
def createAlien(alien_settings,screen,aliens,alienNumber,rowNumber):
    alien = Alien(alien_settings,screen)
    alienWidth = alien.rect.width
    alien.x = alienWidth + 2 * alienWidth * alienNumber
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * rowNumber
    aliens.add(alien)

    #在创建外星人群
def createFleet(alien_settings,screen,ship,aliens):
    alien = Alien(alien_settings,screen)
    numberAliensX = getNumberAliensX(alien_settings,alien.rect.width)
    numberRows = getNumberRows(alien_settings,ship.rect.height,alien.rect.height)
    for rowNumber in range (numberRows):
        for alienNumber in range (numberAliensX):
            createAlien(alien_settings,screen,aliens,alienNumber,rowNumber)

'''更新外星人群的位置'''
def chekFleetEdges(alien_settings,aliens):
    for alien in aliens.sprites():
        if alien.chekEdges():
            changeFleetDirection(alien_settings,aliens)
            break

def changeFleetDirection(alien_settings,aliens):
    #向下移动外星人，并改变他们的方向
    for alien in aliens.sprites():
        alien.rect.y +=alien_settings.fleetDropSpeed
    alien_settings.fleetDirection *= -1
'''外星人撞到飞船'''
def shipHit(alien_settings,stats,screen,ship,aliens,bullets):
    if stats.shipsLeft > 0:
        stats.shipsLeft -= 1    # 被撞到时飞船减一
        aliens.empty()      #清空外星人
        bullets.empty()     #清空子弹
        #创建一群外星人
        createFleet(alien_settings,screen,ship,aliens)
        ship.centerShip()   #飞船放置中央
        sleep(0.5) # 暂停0.5秒
    else:
        stats.gameActive = False
        pygame.mouse.set_visible(True)
'''外星人到达屏幕底端'''
def checkAliensBottom(alien_settings,stats,screen,ship,aliens,bullets):
    screenRect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screenRect.bottom:
            shipHit(alien_settings,stats,screen,ship,aliens,bullets)
            break



def updateAliens(alien_settings,stats,screen,ship,aliens,bullets):
    chekFleetEdges(alien_settings,aliens)
    checkAliensBottom(alien_settings,stats,screen,ship,aliens,bullets)
   #检查是否有外星人到达屏幕边缘
    aliens.update()
    if pygame.sprite.spritecollideany(ship,aliens):
        shipHit(alien_settings,stats,screen,ship,aliens,bullets)

#删除超过屏幕的子弹
def updateBullets(alien_settings,screen,ship,aliens,bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    chekBulletAlienCollisions(alien_settings,screen,ship,aliens,bullets)


def chekBulletAlienCollisions(alien_settings,screen,ship,aliens,bullets):
    # 检查子弹击中了外星人，删除相应子弹和外星人
    collisions = pygame.sprite.groupcollide(bullets,aliens,False,True)
    if len(aliens) == 0 :
        bullets.empty()
        alien_settings.increaseSpeed()      #加快游戏节奏
        createFleet(alien_settings,screen,ship,aliens)
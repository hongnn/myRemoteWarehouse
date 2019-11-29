from pygame import font

class ScoreBoard():
    '''显示得分信息的类'''
    def __init__(self,alien_setting,screen,stats):
        self.screen = screen
        self.screenRect = screen.get_rect()
        self.alien_setting = alien_setting
        self.stats = stats
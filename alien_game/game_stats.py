class GameStats():
    def __init__(self,alien_settings):
        # 初始化统计信息
        self.alien_setting = alien_settings
        self.resetStats()
        self.gameActive = False
    def resetStats(self):
        # 游戏运行期间可能变化的统计信息
        self.shipsLeft = self.alien_setting.shipLimit
        self.score = 0


class Settings():
    def __init__(self,width=1000,height=800,color=(230,230,230)):
        self.screenWidth = width
        self.screenHeight = height
        self.bgColor = color

        #self.shipSpeedFactor = 2.5    #飞船速度
        self.shipLimit = 3

        # 设置子弹
        #self.bulletSpeedFactor = 5
        self.bulletWidth = 3
        self.bulletHeight = 15
        self.bulletColor = 60,60,60
        self.bulletAllowed = 1000

        #外星人设置
        #self.alienSpeedFactor = 1
        self.fleetDropSpeed = 10    #外星人群向下移动速度
        #self.fleetDirection = 1 #为 1 表示向右移动，为 -1 表示向左移动
    #设置游戏加速度
        self.speedUpScale = 1.1
    #初始化随游戏变化的属性
        self.initializeDynamicSettings()

    def initializeDynamicSettings(self):
        self.shipSpeedFactor = 1.5
        self.bulletSpeedFactor = 3
        self.alienSpeedFactor = 1

        self.fleetDirection = 1

    def increaseSpeed(self):
        self.shipSpeedFactor *= self.speedUpScale
        self.bulletSpeedFactor *= self.speedUpScale
        self.alienSpeedFactor *= self.speedUpScale

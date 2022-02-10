import pygame as py
import random

class Racket(py.sprite.Sprite):
    """球拍類別，繼承自Sprite"""
    def __init__(self):
        py.sprite.Sprite.__init__(self)
        self.image = py.Surface((100,10))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
    def update(self):
        x=py.mouse.get_pos()[0]  #取得滑鼠目前座標，只取 x軸
        self.rect.center=(x,680)
        #計算滑鼠相對於上一次座標之X軸位移量，當作球拍位移速度
        self.speed_racket=py.mouse.get_rel()[0]

class Ball(py.sprite.Sprite):
    """球類別，繼承自Sprite"""
    def __init__(self,x,y,speedY):
        py.sprite.Sprite.__init__(self)
        self.image = py.Surface((20,20))
        self.image.fill((0,0,0))
        py.draw.circle(self.image,(255,0,0),(10,10),10)
        self.rect = self.image.get_rect()
        self.rect.center=(x,y)
        self.speed_x=random.randint(-5,5)
        self.speed_y=speedY
    def update(self):
        self.rect.move_ip(self.speed_x,self.speed_y)

class Brick(py.sprite.Sprite):
    def __init__(self,x,y):
        py.sprite.Sprite.__init__(self)
        self.image = py.Surface((40,20))
        self.rect = self.image.get_rect()
        self.rect.center=(x,y)
        self.bonus_ball = False
    def update(self):
        pass

class Wall(py.sprite.Group):
    def __init__(self,dimI,dimJ,x,y):
        """dimI, dimJ 牆面磚塊的行列數。x,y 牆面原點(左上角)在畫面放置之座標"""
        py.sprite.Group.__init__(self)
        bk = py.image.load('./image/brick.png')
        for i in range(dimI):
            for j in range(dimJ):
                brick = Brick(x+40*i, y+20*j)
                brick.image = bk
                self.add(brick)
    def update(self):
        pass



import random

from pico2d import *


class Map:
    def __init__(self):
        self.image = load_image('map2.png')
        self.x= 212
        self.y= 312

    def draw(self):
        self.image.draw(212,162)

    def get_bb(self):
        return self.x - 212 , self.y -50 ,self.x +212, self.y +50
    def draw_bb(self):
        draw_rectangle(*self.get_bb())

class Cloud:
    def __init__(self):
        self.image = load_image('cloud.png')
        self.x, self.y = random.randint(-100,425),random.randint(170,325)
        self.Cdir = 1
        self.Height = random.randint(20,30)
        self.Weight = random.randint(47,56)

    def draw(self):
        self.image.draw(self.x,self.y, self.Weight , self.Height)

    def update(self):
        self.x +=2

        self.Height += self.Cdir
        self.Weight += self.Cdir
        if self.Weight < 47:
            self.Cdir = 1
        if self.Weight > 52:
            self.Cdir = -1
        if self.x > 440:
            self.x = -10
            self.y = random.randint(170,325)

class Wave:


    def __init__(self):
        self.image = load_image('wave.png')
        self.x =0
        self.y = random.randint(-15,-10)
        self.wDir = 1

    def draw(self):
            self.image.draw(self.x,self.y)

    def update(self):
        self.y += self.wDir
        if self.y > 5:
            self.wDir = -1
            self.y = 5
        if self.y < -15:
            self.wDir = 1
            self.y = -15
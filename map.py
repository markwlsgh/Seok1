import random

from pico2d import *


class Map:
    def __init__(self):
        self.image = load_image('map2.png')
        self.bgm = load_music('BGM02.MID')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()
        self.x= 212
        self.y= 312

    def draw(self):
        self.image.draw(212,162)

    def get_bb(self):
        return self.x - 212 , self.y -400 ,self.x , self.y -270

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb2(self):
        return self.x  , self.y -400 ,self.x+2 , self.y -200
    def draw_bb2(self):
        draw_rectangle(*self.get_bb2())

    def get_bb3(self):
        return self.x , self.y - 400, self.x + 212, self.y - 270

    def draw_bb3(self):
        draw_rectangle(*self.get_bb3())

    def get_bb4(self):
        return self.x-2  , self.y-190  ,self.x+4 , self.y - 195
    def draw_bb4(self):
        draw_rectangle(*self.get_bb4())




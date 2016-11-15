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
        return self.x - 212 , self.y -270 ,self.x +212, self.y -400
    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_cc(self):
        return self.x - 3 , self.y -190 ,self.x +5, self.y -400
    def draw_cc(self):
        draw_rectangle(*self.get_cc())


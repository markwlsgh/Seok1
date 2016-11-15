import random

from pico2d import *

class Ball:

    image = None

    def __init__(self):
        self.x, self.y = 30, 300
        self.speed = 10
        self.frame = random.randint(0,5)
        if self.image == None:
            self.image = load_image('ball.png')

    def draw(self):
        self.image.clip_draw(self.frame*40 ,40 , 40, 40, self.x, self.y)

    def update(self, frame_time):
        self.y -= frame_time * self.speed

    def get_bb(self):
        return  self.x -20 , self.y - 20, self.x + 20 , self.y+20

    def stop(self):
        self.fall_speed =0

    def move(self, frame_time):
        self.speed = 20
        self.x -= frame_time * self.speed





class orzin_Ball:
    def __init__(self):
        self.image = load_image('ball.png')
        self.x ,self.y = 30 , 300
        self.frame = random.randint(0, 5)

    def draw(self):
        self.image.clip_draw(self.frame*40 ,40 , 40, 40, self.x, self.y)

    def update(self):
        self.frame = (self.frame+1)%5
        if self.y > 65:
            self.y -= 5

import random

from pico2d import *

class Score:
    def __init__(self):
        self.score1 = 5
        self.score2 = 0
        self.image = load_image('score.png')


    def draw(self):
        if self.score1<10:
            self.image.clip_draw(self.score1*31,0,32,32,30,300)
        if self.score1>9:
            self.image.clip_draw( 31 , 0, 32, 32, 30, 300)
            self.image.clip_draw(self.score1%10 * 31, 0, 32, 32, 55, 300)
        if self.score2<10:
            self.image.clip_draw(self.score2 * 31, 0, 32, 32, 400, 300)
        if self.score2>9:
            self.image.clip_draw( 31 , 0, 32, 32, 380, 300)
            self.image.clip_draw(self.score2%10 * 31, 0, 32, 32, 405, 300)
    def update(self):
        pass

import random
import math

from pico2d import *
from score import Score

class Ball:
    PIXEL_PER_METER = (10.0 / 0.2)  # 10 pixel 30 cm
    RUN_SPEED_KMPH = 20.0  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8
    image = None

    def __init__(self):
        self.x, self.y = 40, 300
        self.speed = 150
        self.x_dir =0
        self.y_dir = 1
        self.r = 5
        self.life_time = 0.0
        self.total_frames = 0.0
        self.frame = random.randint(0,5)
        if self.image == None:
            self.image = load_image('ball.png')

    def draw(self):
        self.image.clip_draw(self.frame*40 ,40 , 40, 40, self.x, self.y)

    def update(self, frame_time):
        def clamp(minimum, x, maximum):
            return max(minimum, min(x, maximum))

        self.life_time += frame_time
        distance = Ball.RUN_SPEED_PPS * frame_time
        self.total_frames += Ball.FRAMES_PER_ACTION * Ball.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 5
        self.x += (self.x_dir * distance)
        self.x = clamp(0, self.x, 800)
        self.y -= (self.y_dir * distance)

        if(self.y > 320 ):
            self.y_dir *= -1
        #if (self.y > 325):
        #    self.y_dir *= -1
        if (self.x > 425):
            self.x_dir *= -1
        if (self.x < 5):
            self.x_dir *= -1

    def get_bb(self):
        return  self.x -20 , self.y - 20, self.x + 20 , self.y+20

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def stop(self, frame_time):
        self.y_dir*= -1

    def move_up(self, frame_time):
        self.x_dir = random.randint(-1,1)/10
        self.y_dir = -1
    def move_right(self, frame_time):
        self.x_dir = random.randint(1,4)/3
        self.y_dir = -1

    def move_left(self, frame_time):
        self.x_dir = random.randint(-5,0)/3
        self.y_dir = -1

    def center(self,frame_time):
        self.x_dir *= -1

    def center2(self,frame_time):
            if( self.y > 130 ):
                self.y_dir*=-1
            #self.x_dir*=-1
            pass
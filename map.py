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
    PIXEL_PER_METER = (10.0 / 5.0)           # 10 pixel 30 cm
    RUN_SPEED_KMPH = 20.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8

    image = None
    def __init__(self):
        self.life_time = 0.0
        self.total_frames = 0.0
        if Cloud.image == None:
            self.image = load_image('cloud.png')
        self.x, self.y = random.randint(-100,425),random.randint(170,325)
        self.Cdir = 1
        self.speed = random.randint(3,5)
        self.Height = random.randint(20,30)
        self.Weight = random.randint(47,56)

    def draw(self):
        self.image.draw(self.x,self.y, self.Weight , self.Height)

    def update(self, frame_time):
        self.life_time += frame_time
        distance = Cloud.RUN_SPEED_PPS * frame_time
        self.total_frames += Cloud.FRAMES_PER_ACTION * Cloud.ACTION_PER_TIME * frame_time
        self.x += (self.speed * distance)
        self.x = clamp(0, self.x, 800)


        self.Height += (distance * self.Cdir)
        self.Weight += (distance * self.Cdir)
        if self.Weight < 47:
            self.Cdir = 1
        if self.Weight > 55:
            self.Cdir = -1
        if self.x > 470:
            self.x = -120
            self.y = random.randint(170,325)

class Wave:
    PIXEL_PER_METER = (10.0 / 5.0)           # 10 pixel 30 cm
    RUN_SPEED_KMPH = 20.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8

    def __init__(self):
        self.life_time = 0.0
        self.total_frames = 0.0
        self.image = load_image('wave.png')
        self.x =0
        self.y = random.randint(-15,-10)
        self.wDir = 1

    def draw(self):
            self.image.draw(self.x,self.y)

    def update(self, frame_time):
        self.life_time += frame_time
        distance = Cloud.RUN_SPEED_PPS * frame_time
        self.total_frames += Wave.FRAMES_PER_ACTION * Wave.ACTION_PER_TIME * frame_time


        self.y += (self.wDir * distance)

        if self.y > 5:
            self.wDir = -1
            self.y = 5
        if self.y < -15:
            self.wDir = 1
            self.y = -15
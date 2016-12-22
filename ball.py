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
    shadow_image = None

    SKILL , NORMAL = 0 , 1
    effect_sound = None

    def __init__(self):
        self.x, self.y = 40, 300
        self.speed = 150
        self.x_dir =0
        self.y_dir = 1
        #followball dir
        self.follow_ball_1_x_dir = 0
        self.follow_ball_1_y_dir = 1
        self.follow_ball_2_x_dir = 0
        self.follow_ball_2_y_dir = 1
        #
        self.r = 5
        self.life_time = 0.0
        self.total_frames = 0.0
        self.frame = random.randint(0,5)
        self.shadow_x = self.x + 5
        self.shadow_y = 35
        self.state = self.NORMAL
        self.t = 0
        self.follow_ball_1_x = 40
        self.follow_ball_1_y = 300
        self.follow_ball_2_x = 40
        self.follow_ball_2_y = 300
        self.effect = False

        if self.image == None:
            self.image = load_image('ball.png')

        if Ball.shadow_image == None:
            Ball.shadow_image = load_image('shadow.png')
        if Ball.effect_sound == None:
            Ball.effect_sound = load_wav('Data_6.wav')
            Ball.effect_sound.set_volume(80)

    def draw(self):
        if self.state == self.NORMAL:
            self.image.clip_draw(self.frame*40 ,40 , 40, 40, self.x, self.y)
        if self.state == self.SKILL:
            self.image.clip_draw(self.frame*40 ,40 , 40, 40, self.x, self.y)
            self.image.clip_draw(40 ,0 , 40, 40, self.follow_ball_1_x, self.follow_ball_1_y)
            self.image.clip_draw(80 ,0 , 40, 40, self.follow_ball_2_x, self.follow_ball_2_y)

        if self.effect == True:
            self.image.clip_draw(0,0,40,40,self.x, self.y)

        self.shadow_image.draw(self.shadow_x, self.shadow_y)

    def update(self, frame_time):
        def clamp(minimum, x, maximum):
            return max(minimum, min(x, maximum))

        self.life_time += frame_time
        distance = Ball.RUN_SPEED_PPS * frame_time
        self.total_frames += Ball.FRAMES_PER_ACTION * Ball.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 5
        self.x += (self.x_dir * distance)
        self.x = clamp(5, self.x, 425)
        self.y = clamp(-10, self.y, 320)
        self.y -= (self.y_dir * distance)
        self.shadow_x = self.x + 5

        self.follow_ball_1_x += (self.follow_ball_1_x_dir * distance * 0.9)
        self.follow_ball_1_y -= (self.follow_ball_1_y_dir * distance * 0.9)
        self.follow_ball_1_x = clamp(5, self.follow_ball_1_x, 425)
        self.follow_ball_1_y = clamp(-10, self.follow_ball_1_y, 320)

        self.follow_ball_2_x += (self.follow_ball_2_x_dir * distance * 0.8)
        self.follow_ball_2_y -= (self.follow_ball_2_y_dir * distance * 0.8)
        self.follow_ball_2_x = clamp(5, self.follow_ball_2_x, 425)
        self.follow_ball_2_y = clamp(-10, self.follow_ball_2_y, 320)

        if (self.effect == True):
            self.effect_sound.play()
            self.effect = False




        if(self.y >= 320 ):
            self.y_dir *= -1
        #if (self.y > 325):
        #    self.y_dir *= -1
        if (self.x >= 425):
            self.x_dir *= -1
        if (self.x <= 5):
            self.x_dir *= -1

        if (self.follow_ball_1_y >= 320):
            self.follow_ball_1_y_dir *= -1
            # if (self.y > 325):
            #    self.y_dir *= -1
        if (self.follow_ball_1_x >= 425):
            self.follow_ball_1_x_dir *= -1
        if (self.follow_ball_1_x <= 5):
            self.follow_ball_1_x_dir *= -1

        if (self.follow_ball_2_y >= 320):
            self.follow_ball_2_y_dir *= -1
            # if (self.y > 325):
            #    self.y_dir *= -1
        if (self.follow_ball_2_x >= 425):
            self.follow_ball_2_x_dir *= -1
        if (self.follow_ball_2_x <= 5):
            self.follow_ball_2_x_dir *= -1

    def get_bb(self):
        return  self.x -20 , self.y - 20, self.x + 20 , self.y+20

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def stop(self, frame_time):
        self.y_dir*= -1
        self.follow_ball_1_y_dir *= -1
        self.follow_ball_2_y_dir *= -1

    def move_up(self, frame_time):
        self.x_dir = random.randint(-1,1)/10
        self.y_dir = -1

        self.follow_ball_1_x_dir = self.x_dir
        self.follow_ball_1_y_dir = -1

        self.follow_ball_2_x_dir = self.x_dir
        self.follow_ball_2_y_dir = -1

    def move_right(self, frame_time):
        self.x_dir = random.randint(1,4)/3
        self.y_dir = -1

        self.follow_ball_1_x_dir = self.x_dir
        self.follow_ball_1_y_dir = -1

        self.follow_ball_2_x_dir = self.x_dir
        self.follow_ball_2_y_dir = -1

    def move_left(self, frame_time):
        self.x_dir = random.randint(-5,0)/3
        self.y_dir = -1

        self.follow_ball_1_x_dir = self.x_dir
        self.follow_ball_1_y_dir = -1

        self.follow_ball_2_x_dir = self.x_dir
        self.follow_ball_2_y_dir = -1

    def center(self,frame_time):
        self.x_dir *= -1
        self.follow_ball_1_x_dir *= -1
        self.follow_ball_2_x_dir *= -1

    def center2(self,frame_time):
            if( self.y > 130 ):
                self.y_dir*=-1
                self.follow_ball_1_y_dir *= -1
                self.follow_ball_2_y_dir *= -1
            #self.x_dir*=-1
            pass
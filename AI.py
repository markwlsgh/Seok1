import random

from pico2d import *

class Ai:
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    RUN_SPEED_KMPH = 20.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 5

    image = None

    STAND , JUMP , SKILL  = 0, 1, 2


    def __init__(self):
        self.x, self.y = 300, 70
        self.frame = random.randint(0, 7)
        self.life_time = 0.0
        self.total_frames = 0.0
        self.dir = 1
        self.state = self.STAND
        self.jumping = 0
        self.jumpSpeed = 280
        self.move_speed = 150
        self.dir1 = True
        self.test = True
        self.total_jump = self.y
        self.tempy = 0
        self.ch = True
        self.speed = 2
        if Ai.image == None:
            Ai.image = load_image('Pikachu.png')


    def update(self, frame_time):
        def clamp(minimum, x, maximum):
            return max(minimum, min(x, maximum))

        self.life_time += frame_time
        distance = Ai.RUN_SPEED_PPS * frame_time
        self.total_frames += Ai.FRAMES_PER_ACTION * Ai.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 5
        self.x += (self.dir * distance)
        self.x = clamp(0, self.x, 800)

        if( self.x < 240):
            self.x = 240
            self.dir *= -1
        if( self.x > 425):
            self.x =425
            self.dir *= -1
        if(self.jumping == 1):
            self.total_jump +=  self.jumpSpeed * frame_time
            self.y =  self.total_jump
            if(self.total_jump >= 180):
                self.jumping = 2
        if self.jumping == 2:
            self.total_jump -= self.jumpSpeed * frame_time
            self.y = self.total_jump
            if (self.total_jump <= self.tempy):
                self.jumping = 0
                self.test = True
                self.state = self.STAND



    def draw(self):
        self.image.clip_draw(self.frame * 65, 364 - self.state*74 , 64, 64, self.x, self.y)

    def get_bb(self):
        return self.x -20 , self.y-20  , self.x +20 , self.y +30

    def get_bb2(self):
        return self.x -10 , self.y+20 , self.x , self.y+20

    def get_bb3(self):
        return self.x +15, self.y+20 ,self.x+25, self.y+20

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def draw_bb2(self):
        draw_rectangle(*self.get_bb2())
    def draw_bb3(self):
        draw_rectangle(*self.get_bb3())



    def handle_event(self, event):
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
            if self.state in (self.STAND, self.JUMP, self.STAND):
                self.dir = -1
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
            if self.state in (self.STAND, self.JUMP, self.STAND):
                self.dir = 1
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
            if self.state in (self.STAND,):
                self.dir = 0
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):
            if self.state in (self.STAND,):
                #self.state = self.STAND
                self.dir = 0

        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_UP):
            if self.state in (self.STAND,):
                self.state = self.JUMP
            if (self.jumping == 0):
                 self.jumping = 1
                 self.tempy = self.y


    def move(self, frame_time):
        self.x -= frame_time * self.speed
        if self.jumping == 2:
            self.jumping = 0
            self.ch = False
            self.test = False
            self.tempy = self.y


    def stop(self):
        if (self.ch == False):
             self.jumping = 2
             self.tempy = 90
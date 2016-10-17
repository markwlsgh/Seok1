import os
import json
os.chdir('E:/2DGP/2016-2DGP/Labs/Pikachu')
import title_state
import game_framework
import random
from pico2d import *


name = 'GameState'


running = None

class Map:
    def __init__(self):
        self.image = load_image('map2.png')

    def draw(self):
        self.image.draw(212,162)

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
        if self.Weight > 55:
            self.Cdir = -1
        if self.x > 440:
            self.x = -10
            self.y = random.randint(170,325)


class Ball:
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

class Score:
    def __init__(self):
        self.score1 = 10
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



class Pikachu:
    image = None

    STOP,LEFT_RUN, RIGHT_RUN,JUMP = 0, 1 , 2,3

    def handle_stop(self):
        pass

    def handle_left_run(self):
        global left

        self.state = self.LEFT_RUN
        if left == True:
            self.x -= 5


    def handle_right_run(self):
        global right

        self.state = self.RIGHT_RUN
        if right == True:
            self.x += 5

    def handle_jump(self):
        global up

        self.state = self.JUMP
        if up == True:
            if self.y < 200:
                self.y += 10
        if self.y > 185:
            up = False
        if up == False:
            if self.y > 80:
                    self.y -= 10

    def handle_skill(self):
        pass


    handle_state = {
            STOP:handle_stop,
            LEFT_RUN: handle_left_run,
            RIGHT_RUN : handle_right_run,
            JUMP : handle_jump
    }


    def update(self):
        self.frame = (self.frame + 1 ) % 5
        self.handle_state[self.state](self)


    def __init__(self):
        self.x, self.y = 150,75
        self.frame = random.randint(0, 5)
        self.right, self.left = False, False
        self.state = self.STOP
        if Pikachu.image == None:
            Pikachu.image = load_image('Pikachu.png')

    def draw(self):
        self.image.clip_draw(self.frame * 65, 360, 64, 64, self.x, self.y)











def handle_events():
    global running,right,left,up
    global pikachu

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        if event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
            pikachu.state = pikachu.RIGHT_RUN
            right = True
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
            pikachu.state = pikachu.LEFT_RUN
            left = True
        if (event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
            pikachu.state = pikachu.STOP
        if (event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):
            pikachu.state = pikachu.STOP
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_UP):
            pikachu.state = pikachu.JUMP
            up = True





def enter():
    global pikachu , map, clouds, ball, score
    pikachu = Pikachu()
    map = Map()
    clouds = [Cloud() for i in range(15)]
    ball = Ball()
    score = Score()

    global running, right, left

    running = True
    right = False
    left = False
    up = False

def exit():
    global pikachu, map, clouds, ball, score
    del(pikachu)
    del(map)
    del(clouds)
    del(ball)
    del(score)


def pause():
    pass


def resume():
    pass

def update():
    pikachu.update()
    for cloud in clouds:
        cloud.update()
    ball.update()
    score.update()

    clear_canvas()

def draw():
    map.draw()
    for cloud in clouds:
        cloud.draw()
    score.draw()
    ball.draw()
    pikachu.draw()
    update_canvas()

    delay(0.04)


from pico2d import *

import game_framework

from ball import Ball # import Boy class from boy.py
from map import Map
from map import Cloud
from map import Wave
from pikachu import Pikachu
from score import  Score

name = "collision"

pikachu = None
ball = None
Map = None
Cloud = None
brick = None


def create_world():
    global pikachu , map, clouds, ball, score, waves
    pikachu = Pikachu()
    map = Map()
    ball = Ball()
    score = Score()
    waves = [Wave() for i in range(28)]
    for i in range(28):
        waves[i].x = i * 16
def destroy_world():
    global pikachu, map, clouds, ball, score,waves
    del(pikachu)
    del(map)
    del(clouds)
    del(ball)
    del(score)
    del(waves)


def enter():
    open_canvas()
    game_framework.reset_time()
    create_world()


def exit():
    destroy_world()
    close_canvas()


def pause():
    pass


def resume():
    pass


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            else:
                pikachu.handle_event(event)



def collide(a, b):
    left_a , bottom_a , right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return  False
    if right_a < left_b : return  False
    if top_a < bottom_b : return  False
    if bottom_a > top_b : return  False

    return True

def update(frame_time):
    pikachu.update(frame_time)
    for ball in balls:
        ball.update(frame_time)

    for ball in balls:
        if collide(boy, ball):
            balls.remove(ball)

    for ball in big_balls:
        if collide(grass , ball):
            ball.stop()
        if collide(brick , ball):
            ball.stop()
            ball.move(frame_time)

        if collide(boy, brick):
            boy.stop()
            boy.move(frame_time)

    brick.update(frame_time)

    #delay(0.2)



def draw(frame_time):
    clear_canvas()
    grass.draw()
    boy.draw()
    for ball in balls:
        ball.draw()

    grass.draw_bb()
    boy.draw_bb()
    for ball in balls:
        ball.draw_bb()

    brick.draw()
    brick.draw_bb()
    update_canvas()







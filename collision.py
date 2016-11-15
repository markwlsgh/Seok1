from pico2d import *

import game_framework

from ball import Ball # import Boy class from boy.py
from map import Map
from map_deko import Cloud
from map_deko import Wave
from pikachu import Pikachu
from score import  Score

name = "collision"

pikachu = None
ball = None
map = None
score = None
waves = None
clouds = None


def create_world():
    global pikachu , map, clouds, ball, score, waves
    pikachu = Pikachu()
    map = Map()
    ball = Ball()
    score = Score()
    waves = [Wave() for i in range(28)]
    clouds = [Cloud() for i in range(15)]
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
    open_canvas(425,325)
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
    for cloud in clouds:
        cloud.update(frame_time)
    ball.update(frame_time)
    score.update()
    for wave in waves:
        wave.update(frame_time)
    clear_canvas()

    if collide(pikachu, ball):
        ball.move(frame_time)

    if collide(map,ball):
        ball.move(frame_time)

def draw(frame_time):
    clear_canvas()
    map.draw()
    pikachu.draw()
    for cloud in clouds:
        cloud.draw()
    score.draw()
    ball.draw()
    pikachu.draw()
    for wave in waves:
        wave.draw()

    pikachu.draw_bb()
    map.draw_bb()
    ball.draw_bb()
    map.draw_cc()

    update_canvas()







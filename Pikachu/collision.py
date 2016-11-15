from pico2d import *

import game_framework

import title_state

from ball import Ball # import Boy class from boy.py
from map import Map
from map_deko import Cloud
from map_deko import Wave
from pikachu import Pikachu
from score import  Score
from AI import Ai

name = "collision"

pikachu = None
ball = None
map = None
score = None
waves = None
clouds = None
AI = None

def create_world():
    global pikachu , map, clouds, ball, score, waves, AI
    pikachu = Pikachu()
    map = Map()
    ball = Ball()
    score = Score()
    waves = [Wave() for i in range(28)]
    clouds = [Cloud() for i in range(15)]
    for i in range(28):
        waves[i].x = i * 16
    AI = Ai()

def destroy_world():
    global pikachu, map, clouds, ball, score,waves,AI
    del(pikachu)
    del(map)
    del(clouds)
    del(ball)
    del(score)
    del(waves)
    del(AI)

def enter():

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

def collide2(a, b):
    left_a , bottom_a , right_a, top_a = a.get_bb2()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return  False
    if right_a < left_b : return  False
    if top_a < bottom_b : return  False
    if bottom_a > top_b : return  False

    return True

def collide3(a, b):
    left_a , bottom_a , right_a, top_a = a.get_bb3()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return  False
    if right_a < left_b : return  False
    if top_a < bottom_b : return  False
    if bottom_a > top_b : return  False

    return True

def collide4(a, b):
    left_a , bottom_a , right_a, top_a = a.get_bb4()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return  False
    if right_a < left_b : return  False
    if top_a < bottom_b : return  False
    if bottom_a > top_b : return  False

    return True

def update(frame_time):

    if(score.score1 >=15 ):
        game_framework.push_state(title_state)
    if (score.score2 >= 15):
        game_framework.push_state(title_state)

    pikachu.update(frame_time)
    for cloud in clouds:
        cloud.update(frame_time)
    ball.update(frame_time)
    score.update()
    AI.update(frame_time)
    for wave in waves:
        wave.update(frame_time)
    clear_canvas()


    if collide(AI,ball):
        ball.move_left(frame_time)

    if collide(pikachu, ball):
        ball.move_up(frame_time)

    if collide2(pikachu, ball):
        ball.move_left(frame_time)

    if collide3(pikachu,ball):
        ball.move_right(frame_time)

    if collide(ball,map):
        ball.stop(frame_time)
        score.score2 +=1
        ball.x = 380
        ball.y =300
        ball.x_dir =0
        ball.y_dir =1
        pikachu.x = 0
        pikachu.y =70
        delay(0.1)

    if collide2(map,ball):
        ball.center(frame_time)

    if collide3(map,ball):
        ball.stop(frame_time)
        score.score1 +=1
        ball.x = 40
        ball.y =300
        ball.x_dir =0
        ball.y_dir =1
        pikachu.x = 0
        pikachu.y = 70
        delay(0.1)

    if collide4(map,ball):
        ball.center2(frame_time)


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
    pikachu.draw_bb2()
    pikachu.draw_bb3()
    map.draw_bb()
    ball.draw_bb()
    map.draw_bb2()
    map.draw_bb3()
    map.draw_bb4()
    AI.draw_bb()


    update_canvas()







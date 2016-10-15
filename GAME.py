import sys
sys.path.append('../LabsAll/Labs')

import random
from pico2d import *

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

    def draw(self):
        self.image.draw(self.x,self.y)

    def update(self):
        self.x +=2

        if self.x > 440:
            self.x = -10
            self.y = random.randint(170,325)

class Pikachu:
    image = None

    STOP,LEFT_RUN, RIGHT_RUN = 0, 1 , 2

    def handle_stop(self):
        pass

    def handle_left_run(self):
        global left

        self.state = self.LEFT_RUN
        if left == True:
            self.x -= 5


    def handle_right_run(self):
        global right
        global running
        self.state = self.RIGHT_RUN
        if right == True:
            self.x += 5

    handle_state = {
            STOP:handle_stop,
            LEFT_RUN: handle_left_run,
            RIGHT_RUN : handle_right_run
    }


    def update(self):
        self.frame = (self.frame+1)%5
        self.handle_state[self.state](self)


    def __init__(self):
        self.x, self.y = 150,75
        self.frame = random.randint(0, 5)
        self.right, self.left = False, False
        self.state = self.STOP
        if Pikachu.image == None:
            Pikachu.image = load_image('Pikachu.png')

    def draw(self):
        self.image.clip_draw(self.frame * 64, 360, 64, 74, self.x, self.y)











def handle_events():
    global running,right,left
    global pikachu

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
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















def main():

    open_canvas(425,325)
    global pikachu
    pikachu = Pikachu()
    map = Map()
    clouds = [Cloud() for i in range(20)]

    global running, right, left

    running = True
    right = False
    left = False

    while running:
        handle_events()


        pikachu.update()

        clear_canvas()

        map.draw()
        for cloud in clouds:
            cloud.update()
        for cloud in clouds:
            cloud.draw()
        pikachu.draw()
        update_canvas()

        delay(0.04)

    close_canvas()


if __name__ == '__main__':
    main()
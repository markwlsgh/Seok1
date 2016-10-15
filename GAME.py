import sys
sys.path.append('../LabsAll/Labs')

import random
from pico2d import *

running = None

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)


class Pikachu:
    image = None


    LEFT_RUN, RIGHT_RUN, LEFT_STAND, RIGHT_STAND = 0, 1, 2, 3


    def handle_left_run(self):
        global change
        self.x -= 5
        self.run_frames += 1
        if self.x < 0 :
            self.state = self.RIGHT_RUN
            self.x = 0
        if self.run_frames == 100:
            self.state = self.LEFT_STAND
            self.stand_frames = 0
        if change == False:
            self.state = self.RIGHT_RUN
            change = True
            self.stand_frames =0

    def handle_left_stand(self):
        global change

        self.stand_frames +=1
        if self.stand_frames == 50:
            self.state = self.LEFT_RUN
            self.run_frames = 0
        if change == False:
            self.state = self.LEFT_RUN
            change = True
            self.run_frames = 0


    def handle_right_run(self):
        global change

        self.x += 5
        self.run_frames += 1
        if self.x > 800:
            self.state = self.LEFT_RUN
            self.x = 800
        if self.run_frames == 100:
            self.state = self.RIGHT_STAND
            self.stand_frames = 0
        if change == False:
            self.state = self.LEFT_RUN
            change = True
            self.stand_frames = 0



    def handle_right_stand(self):
        global change

        self.stand_frames +=1
        if self.stand_frames == 50:
            self.state = self.RIGHT_RUN
            self.run_frames = 0
        if change == False:
                self.state = self.RIGHT_RUN
                change = True
                self.run_frames = 0



    handle_state = {
            LEFT_RUN: handle_left_run,
            RIGHT_RUN : handle_right_run,
            LEFT_STAND: handle_left_stand,
            RIGHT_STAND: handle_right_stand
    }

    def update(self):
        self.frame = (self.frame+1)%5
        self.handle_state[self.state](self)


    def __init__(self):
        self.x, self.y = random.randint(10, 500), 90
        self.frame = random.randint(0, 7)
        self.run_frames = 0
        self.stand_frames = 0
        self.state = self.RIGHT_RUN
        if Pikachu.image == None:
            Pikachu.image = load_image('Pikachu.png')

    def draw(self):
        self.image.clip_draw(self.frame * 64, 360, 64, 74, self.x, self.y)


def handle_events():
    global running ,change
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif (event.type, event.key) == (SDL_KEYDOWN , SDLK_SPACE):
            change = False




def main():

    open_canvas(425,325)

    pikachu = Pikachu()
    grass = Grass()

    global running, change
    running = True
    change = True

    while running:
        handle_events()

        pikachu.update()

        clear_canvas()
        grass.draw()
        pikachu.draw()
        update_canvas()

        delay(0.04)

    close_canvas()


if __name__ == '__main__':
    main()
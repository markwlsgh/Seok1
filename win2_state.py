import game_framework
from pico2d import *
import collision
import title_state


name = "2P_WIN"
image = None
start_sound = None

def enter():
    global image ,start_sound
    image = load_image('Wins2.jpg')
    start_sound = load_wav('Data_1.wav')
    start_sound.set_volume(64)

def exit():
    global image , start_sound
    del(image)
    del(start_sound)

def handle_events(frame_time):
    global start_sound

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                    game_framework.push_state(title_state)
                    start_sound.play()



def draw(frame_time):
    clear_canvas()
    image.draw(212,162)
    update_canvas()







def update(frame_time):
    pass


def pause():
    pass


def resume():
    pass







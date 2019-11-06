import game_framework
import main_state
from pico2d import *


name = "TitleState"
image = None


def enter():
    global image
    image = load_image('title.png')
    pass


def exit():
    global image
    del image
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(main_state)
                #elif event.type == SDL_MOUSEMOTION:
                #print("x=", event.x)
                #print('y=', event.y)
            elif event.type == SDL_MOUSEBUTTONDOWN:
                if 470 > event.x > 380 and 486 > event.y > 396:
                    game_framework.change_state(main_state)


def draw():
    clear_canvas()
    image.draw(800 // 2, 800 // 2)
    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass







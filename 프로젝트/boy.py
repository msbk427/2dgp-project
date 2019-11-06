from pico2d import *

import map
import game_world

one_space_size = 50
pixel_width = 12
pixel_height = 18
reverse_pixel_start = 160

# Boy Event
UP, DOWN, LEFT, RIGHT, ATTACK, Rest = range(6)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT,
    (SDL_KEYDOWN, SDLK_UP): UP,
    (SDL_KEYDOWN, SDLK_DOWN): DOWN,
    (SDL_KEYDOWN, SDLK_SPACE): ATTACK
}


# Boy States

class IdleState:

    @staticmethod
    def enter(boy, event):
        boy.move(event)
        boy.x = clamp(50, boy.x, 700)
        boy.y = clamp(50, boy.y, 700)
        boy.timer = 0

    @staticmethod
    def exit(boy, event):
        pass

    @staticmethod
    def do(boy):
        boy.frame_count += 1
        if boy.frame_count > 70:
            boy.frame = (boy.frame + 1) % 2
            boy.frame_count = 0

    @staticmethod
    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_draw(boy.frame * pixel_width, pixel_height, pixel_width, pixel_height, (one_space_size // 2) + boy.x,
                                (one_space_size // 2) + boy.y, one_space_size, one_space_size)
        else:
            boy.reverse_image.clip_draw(232 + (boy.frame * pixel_width), pixel_height, pixel_width, pixel_height,
                                   (one_space_size // 2) + boy.x, (one_space_size // 2) + boy.y, one_space_size, one_space_size)


class RunState:

    @staticmethod
    def enter(boy, event):
        boy.move(event)
        boy.x = clamp(50, boy.x, 700)
        boy.y = clamp(50, boy.y, 700)
        boy.timer = 0

    @staticmethod
    def exit(boy, event):
        pass

    @staticmethod
    def do(boy):
        boy.frame_count += 1
        boy.timer += 1
        if boy.frame_count > 70:
            boy.frame = (boy.frame + 1) % 6
            boy.frame_count = 0
        if boy.timer > 500:
            boy.add_event(Rest)

    @staticmethod
    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_draw((pixel_width * 2) + boy.frame * pixel_width, pixel_height, pixel_width, pixel_height,
                                (one_space_size // 2) + boy.x,
                                (one_space_size // 2) + boy.y,
                                one_space_size, one_space_size)
        else:
            boy.reverse_image.clip_draw((160) + boy.frame * pixel_width, pixel_height, pixel_width, pixel_height,
                                   (one_space_size // 2) + boy.x, (one_space_size // 2) + boy.y,
                                    one_space_size, one_space_size)


next_state_table = {
    IdleState: {UP: RunState, DOWN: RunState, LEFT: RunState, RIGHT: RunState, ATTACK: IdleState, Rest: IdleState},
    RunState: {UP: RunState, DOWN: RunState, LEFT: RunState, RIGHT: RunState, ATTACK: IdleState, Rest: IdleState}
}


class Boy:

    def __init__(self):
        self.x, self.y = 100, 100
        self.image = load_image('warrior.png')
        self.reverse_image = load_image('warrior_reverse.png')
        self.dir = 1
        self.frame = 0
        self.frame_count = 0
        self.timer = 0
        self.hp = 10
        self.turn = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)

    def attack(self):

        pass

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    def move(self, event):
        if event == UP:
            if map.Map_struct[(self.y + one_space_size)//one_space_size][(self.x//one_space_size)] == 1:
                self.y += one_space_size
        elif event == DOWN:
            if map.Map_struct[(self.y - one_space_size) // one_space_size][(self.x // one_space_size)] == 1:
                self.y -= one_space_size
        elif event == RIGHT:
            if map.Map_struct[self.y // one_space_size][((self.x + one_space_size) // one_space_size)] == 1:
                self.x += one_space_size
                self.dir = 1
        elif event == LEFT:
            if map.Map_struct[(self.y // one_space_size)][((self.x - one_space_size) // one_space_size)] == 1:
                self.x -= one_space_size
                self.dir = 0
        self.turn += 1






from pico2d import *
import main_state
import random
import map

one_space_size = 50


class Monster:

    def __init__(self, x, y):
        self.x, self.y = x, y
        self.frame = 0
        self.frame_count = 0
        self.move_count = 0
        self.hp = 10
        self.move_logic = 0
        self.image = load_image('monster.png')
        self.hp_image = load_image('hp_bar.png')

    def update(self):
        self.frame_count += 1
        if self.frame_count > 70:
            self.frame = (self.frame + 1) % 5
            self.frame_count = 0
        self.move_count += 1
        if self.move_count > 300:
            self.move_logic = random.randint(0, 1)
            if self.move_logic == 1:
                if main_state.boy.x - self.x > one_space_size:
                    if map.Map_struct[self.y // one_space_size][((self.x + one_space_size) // one_space_size)] == 1:
                        self.x += one_space_size
                elif main_state.boy.x - self.x < -one_space_size:
                    if map.Map_struct[(self.y // one_space_size)][((self.x - one_space_size) // one_space_size)] == 1:
                        self.x -= one_space_size
                elif main_state.boy.y - self.y > one_space_size:
                    if map.Map_struct[(self.y + one_space_size) // one_space_size][(self.x // one_space_size)] == 1:
                        self.y += one_space_size
                elif main_state.boy.y - self.y < -one_space_size:
                    if map.Map_struct[(self.y - one_space_size) // one_space_size][(self.x // one_space_size)] == 1:
                        self.y -= one_space_size
            elif self.move_logic == 0:
                if main_state.boy.y - self.y > one_space_size:
                    if map.Map_struct[(self.y + one_space_size) // one_space_size][(self.x // one_space_size)] == 1:
                        self.y += one_space_size
                elif main_state.boy.y - self.y < -one_space_size:
                    if map.Map_struct[(self.y - one_space_size) // one_space_size][(self.x // one_space_size)] == 1:
                        self.y -= one_space_size
                elif main_state.boy.x - self.x > one_space_size:
                    if map.Map_struct[self.y // one_space_size][((self.x + one_space_size) // one_space_size)] == 1:
                        self.x += one_space_size
                elif main_state.boy.x - self.x < -one_space_size:
                    if map.Map_struct[(self.y // one_space_size)][((self.x - one_space_size) // one_space_size)] == 1:
                        self.x -= one_space_size
            self.move_count = 0

    def draw(self):
        self.image.clip_draw(self.frame * 12, 0, 13, 16,
                             (one_space_size//2) + self.x, (one_space_size//2) + self.y, one_space_size, one_space_size)
        self.hp_image.clip_draw(self.hp, 0, self.hp * 64, 4,
                                (one_space_size//2) + self.x+5, (one_space_size//2) + self.y + (one_space_size-10),
                                (one_space_size-10), 5)

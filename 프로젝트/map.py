from pico2d import *
from monster import Monster

import game_world

one_space_size = 50

Map_struct = [[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
              [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
              [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
              [2, 1, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
              [2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
              [2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
              [2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
              [2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
              [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
              [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
              [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
              [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
              [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
              [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
              [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
              [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]]
Map_size = 16 * 16


class Map:
    image = None

    def __init__(self):
        if Map.image is None:
            Map.image = load_image('tiles_caves.png')

    def update(self):
        pass

    def add_monster(self):
        monster = Monster(600, 600)
        game_world.add_object(monster, 1)

    def draw(self):
        for i in range(Map_size):
            if Map_struct[i // 16][i % 16] == 1:  # 길
                self.image.clip_draw(0, 16*15, 16, 16,
                                     (one_space_size//2) + (i % 16) * one_space_size,
                                     (one_space_size//2) + (i // 16) * one_space_size, one_space_size, one_space_size)
            elif Map_struct[i // 16][i % 16] == 2:  # 벽
                self.image.clip_draw(0, 16*11, 16, 16,
                                     (one_space_size//2) + (i % 16) * one_space_size,
                                     (one_space_size//2) + (i // 16) * one_space_size, one_space_size, one_space_size)
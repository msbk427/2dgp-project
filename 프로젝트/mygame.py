import game_framework
import pico2d

import title_state

title_x = 800
title_y = 800


pico2d.open_canvas(title_x, title_y)
game_framework.run(title_state)
pico2d.close_canvas()
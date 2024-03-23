import pygame as game
from player import *
from screen import *

game.init()

set_fps = game.time.Clock()
game.display.set_caption("Roguelike")
set_fps.tick(60)

o_player = player(10, 5, 3, int(1/5), 0, 0)

resolution = game.display.set_mode([800, 600])
background_color = (128, 128, 128)
o_screen = screen(resolution, background_color)

while True:
    for event in game.event.get():
        if event.type == game.QUIT:
            game.quit()

    o_player.get_movement()
    o_player.rotate_player()

    o_screen.fill_screen()


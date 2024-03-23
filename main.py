import pygame as game
from player import *

game.init()



set_fps = game.time.Clock()
game.display.set_caption("Roguelike")
set_fps.tick(60)

o_player = player(10, 5, 3, 1/5, 0, 0)

while True:
    for event in game.event.get():
        if event.type == game.QUIT:
            game.quit()

    o_player.get_movement(screen)

    game.display.update()


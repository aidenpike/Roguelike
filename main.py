import pygame as game
from player import *

game.init()

screen = game.display.set_mode([800, 600])
background_color = (128, 128, 128)
set_fps = game.time.Clock()
game.display.set_caption("Roguelike")
set_fps.tick(60)

player = player(10, 5, 3, 1/5, 0, 0)

while True:
    for event in game.event.get():
        if event.type == game.QUIT:
            game.quit()
    
    screen.fill(background_color)

    player.get_movement(screen)

    game.display.update()


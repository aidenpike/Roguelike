import pygame as game

game.init()

screen = game.display.set_mode([800, 600])
background_color = (128, 128, 128)
set_fps = game.time.Clock()

while True:
    for event in game.event.get():
        if event.type == game.QUIT:
            game.quit()

    screen.fill(background_color)

    game.draw.circle(screen, (0,0,255), (250, 250), 75)

    game.display.flip()
    set_fps.tick(60)

import pygame as game

class player:
    def __init__(self, health, defense, damage, speed, pos_x, pos_y):
        self.health = health
        self.defense = defense
        self.damage = damage
        self.speed = speed
        self.pos_x = pos_x
        self.pos_y = pos_y

    def get_movement(self):
        get_key = game.key.get_pressed()

        if get_key[game.K_w]:
            self.pos_y -= self.speed
        if get_key[game.K_a]:
            self.pos_x -= self.speed
        if get_key[game.K_s]:
            self.pos_y += self.speed
        if get_key[game.K_d]:
            self.pos_x += self.speed

        game.draw.circle((game.display.set_mode([800, 600])), (0,0,255), (self.pos_x, self.pos_y), 75)
        #Hard coded screen resolution for now. Expect screen class later. 

    def draw_player(self):
        self.get_movement()

        game.display.update()
        game.display.flip()
        
    

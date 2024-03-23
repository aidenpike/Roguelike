import pygame as game
import math 

# Encompasses all player related controls 
class player:
    def __init__(self, health, defense, damage, speed, pos_x, pos_y):
        self.health = health
        self.defense = defense
        self.damage = damage
        self.speed = speed
        self.pos_x = pos_x
        self.pos_y = pos_y

    # Moves player based on input
    def get_movement(self, screen):
        get_key = game.key.get_pressed()

        if get_key[game.K_w]:
            self.pos_y -= self.speed
        if get_key[game.K_a]:
            self.pos_x -= self.speed
        if get_key[game.K_s]:
            self.pos_y += self.speed
        if get_key[game.K_d]:
            self.pos_x += self.speed
            
        game.draw.rect(screen, (0,0,255), 10, 5)
        #Expect screen class later. 

    # Point player to cursor
    # Needs debug later
    def rotate_player(self):
        mouse_x, mouse_y = game.mouse.get_pos()
        rel_x, rel_y = mouse_x - self.pos_x, mouse_y - self.pos_y
        angle = math.atan2(rel_y, rel_x)
        angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)

        self.image = game.transform.rotate(self.original_image, int(angle))
        self.rect = self.image.get_rect(center = self.position)


    def draw_player(self):
        self.get_movement()   

           
    

import pygame as game

# All general screen functions
# Needs debug later
class screen:
    def __init__(self, resolution, background_color):
        self.resolution = resolution
        self.background_color = background_color
    
    def get_resolution(self):
        return self.resolution
    
    def fill_screen(self):
        self.resolution.fill(self.background_color)
        
        game.display.update()


# Probably some filepath include here
import random

# Encompasses all weapon related functions
class weapon:
    def __init__(self, damage_boost, tier):
        self.damage_boost = damage_boost
        self.tier = tier

    def return_random_boost(self, minimum, maximum):
        random.seed(maximum - minimum / minimum)
    
        self.damage_boost += random.randomint(minimum, maximum)
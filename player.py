import pygame

class Player(pygame.Rect):

    def __init__(self, position_x, position_y):
        self.position_x = position_x
        self.position_y = position_y
        self.size_x = 20
        self.size_y = 120

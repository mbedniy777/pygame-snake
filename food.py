from random import randrange

import pygame as pg
from settings import PIXEL, WIGHT, HEIGHT


class Food(pg.Rect):
    def __init__(self, color):
        self.color = color
        super().__init__(0, 0, PIXEL, PIXEL)

    def draw(self, surface):
        pg.draw.rect(surface, self.color, self)

    def set_random_cords(self):
        self.left = randrange(0, WIGHT, PIXEL)
        self.top = randrange(0, HEIGHT, PIXEL)

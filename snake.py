import pygame as pg
from settings import PIXEL, WIDTH, HEIGHT


class Snake:
    RIGHT_VECTOR = 1
    LEFT_VECTOR = 2
    UP_VECTOR = 3
    DOWN_VECTOR = 4

    def __init__(self, color):
        self.body = [pg.Rect(WIDTH / 2, HEIGHT / 2, PIXEL, PIXEL)]
        self.vector = self.RIGHT_VECTOR
        self.color = color

    def move(self):
        snake_head = self.body[0].copy()
        self.body.pop()
        self.body.insert(0, snake_head)
        if self.vector == self.RIGHT_VECTOR:
            snake_head.left += PIXEL
        elif self.vector == self.LEFT_VECTOR:
            snake_head.left -= PIXEL
        elif self.vector == self.UP_VECTOR:
            snake_head.top -= PIXEL
        elif self.vector == self.DOWN_VECTOR:
            snake_head.top += PIXEL

    def increase(self):
        self.body.append(self.body[-1].copy())

    def draw(self, surface):
        for rect in self.body:
            pg.draw.rect(surface, self.color, rect)



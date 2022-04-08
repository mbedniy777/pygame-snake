import pygame as pg
from settings import WIGHT, HEIGHT, PIXEL
screen = pg.display.set_mode((WIGHT, HEIGHT))
is_running = True
while is_running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            is_running = False
pg.quit()

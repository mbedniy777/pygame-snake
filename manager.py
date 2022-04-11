import pygame as pg
from time import sleep
from snake import Snake
from food import Food
from color import RED, BLACK, GREEN
from settings import WIDTH, HEIGHT, PIXEL


class Manager:
    def __init__(self):
        self.is_running = True
        self.snake = Snake(RED)
        self.food = Food(GREEN)
        self.display = pg.display.set_mode((WIDTH, HEIGHT))

    def start_game_loop(self):
        """Start game."""
        while self.is_running:
            sleep(0.1)
            self.draw_objects()
            self.move_objects()
            self.process_events()
            self.process_collision_objects_with_border()

    def process_collision_objects_with_border(self):
        """Controls how objects collide with the border."""
        snake_head = self.snake.body[0]
        if snake_head.left < 0:
            snake_head.right = WIDTH
        if snake_head.right > WIDTH:
            snake_head.left = 0
        if snake_head.top < 0:
            snake_head.bottom = HEIGHT
        if snake_head.bottom > HEIGHT:
            snake_head.top = 0

    def draw_objects(self):
        """Draws objects."""
        self.display.fill(BLACK)
        self.snake.draw(self.display)
        self.food.draw(self.display)
        pg.display.flip()

    def process_events(self):
        """Handles application events."""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.is_running = False

    def process_collision_objects(self):
        snake_head = self.snake.body[1:]
        if snake_head.center == self.food.center:
            self.food.set_random_cords()

        if snake_head.center == self.snake.body.center:
            self.is_running = False

    def move_objects(self):
        self.snake.move()


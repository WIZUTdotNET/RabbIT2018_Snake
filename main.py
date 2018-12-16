from pygame.locals import *
from random import randint

from apple import Apple
from player import Player
from logic import Game

import pygame
import time

STEP = 44

class App:
    windowWidth = 800
    windowHeight = 600
    snake = 0
    apple = 0

    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self._apple_surf = None
        self.game = Game()
        self.snake = Player(3)
        self.apple = Apple(5, 5)

    def on_init(self):
        pygame.init()

        self._display_surf = pygame.display.set_mode((self.windowWidth, self.windowHeight), pygame.HWSURFACE)

        pygame.display.set_caption('Rabbit_2k18: Snake')
        self._running = True
        self._image_surf = pygame.Surface((STEP,STEP))
        self._apple_surf = pygame.Surface((STEP,STEP))

    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    def on_loop(self):
        self.snake.update()

        # does snake eat apple?
        for i in range(0, self.snake.length):
            if self.game.isCollision(self.apple.x, self.apple.y, self.snake.x[i], self.snake.y[i], STEP):
                self.apple.x = randint(2, 9) * STEP
                self.apple.y = randint(2, 9) * STEP
                self.snake.length = self.snake.length + 1
                self.snake.points = self.snake.points + 1

        # does snake collide with itself?
        for i in range(2, self.snake.length):
            if self.game.isCollision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i], 40):
                print("You lose! Collision: ")
                print("x[0] (" + str(self.snake.x[0]) + "," + str(self.snake.y[0]) + ")")
                print("x[" + str(i) + "] (" + str(self.snake.x[i]) + "," + str(self.snake.y[i]) + ")")
                print("Points: " + str(self.snake.points))
                exit(0)

        pass

    def on_render(self):

        self._display_surf.fill((0, 0, 0))

        self.snake.draw(self._display_surf, self._image_surf)
        self.apple.draw(self._display_surf, self._apple_surf)

        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while (self._running):

            pygame.event.pump()
            keys = pygame.key.get_pressed()

            if (keys[K_RIGHT]):
                self.snake.moveRight()

            if (keys[K_LEFT]):
                self.snake.moveLeft()

            if (keys[K_UP]):
                self.snake.moveUp()

            if (keys[K_DOWN]):
                self.snake.moveDown()

            if (keys[K_ESCAPE]):
                self._running = False

            self.on_loop()
            self.on_render()

            time.sleep(50.0 / 1000.0)

        self.on_cleanup()

if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
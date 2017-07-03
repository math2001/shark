# -*- encoding: utf-8 -*-

import pygame
from pygame.locals import *

pygame.init()

SIZE = WIDTH, HEIGHT = 500, 500

screen = pygame.display.set_mode(SIZE)

from ocean import Ocean
from shark import Shark

shark = Shark()
ocean = Ocean('test', 'test.txt', shark)

pygame.key.set_repeat(200, 50)

going = True
while going:

    for event in pygame.event.get():
        if event.type == QUIT:
            going = False

        if event.type == KEYDOWN:

            if event.key == K_UP:
                ocean.move((0, 1))
            elif event.key == K_DOWN:
                ocean.move((0, -1))
            elif event.key == K_LEFT:
                ocean.move((1, 0))
            elif event.key == K_RIGHT:
                ocean.move((-1, 0))


    screen.fill(0)

    ocean.render()
    shark.render()
    pygame.display.flip()
    pygame.time.wait(50)

pygame.quit()

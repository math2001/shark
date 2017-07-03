# -*- encoding: utf-8 -*-

import pygame
from pygame.locals import *

pygame.init()

class Screen:

    @staticmethod
    def init():
        """
            A static method to use the SAME rect all the time.
            Like this, it is way easier to change it when the user resize the screen
        """
        Screen.screen = pygame.display.get_surface()
        Screen.rect   = Screen.screen.get_rect()

    def __str__(self):
        return '<Screen width={} height={}>'.format(
            Screen.rect.width, Screen.rect.height)

# -*- encoding: utf-8 -*-

import pygame
from screen import Screen

Screen.init()

def load_image(filename):
    return pygame.image.load('img/' + filename)

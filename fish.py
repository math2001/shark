# -*- encoding: utf-8 -*-

from functions import *

class Fish:

    IMAGES = {
        'shark': load_image('shark.png')
    }

    def __init__(self, fish_type):
        self.surface = Fish.IMAGES[fish_type]
        self.head_position = self.surface.get_rect(centerx=Screen.rect.width / 2, centery=Screen.rect.height / 2)

    def check_position(self, position):
        """return a boolean"""
        pass

    def render(self):
        Screen.screen.blit(self.surface, self.head_position)

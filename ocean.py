# -*- encoding: utf-8 -*-

from functions import *
import math

class Ocean:

    BLOCKS = {
        'ocean': load_image('block-ocean.png'),
        'rock': load_image('block-rock.png')
    }

    CODES = {
        ' ': 'ocean',
        '0': 'rock'
    }

    BLOCK_SIZE = 50

    SPEED = 10

    def __init__(self, name, filename, shark):
        self.name = name
        with open('oceans/' + filename) as fp:
            self.ocean = [list(bit) for bit in fp.read().strip().split('\n')]
        self.position = [0, 0]
        self.shark = shark

    def get_shark_cell(self):
        cells = ''
        x = (self.shark.head_position.left - self.position[0]) / Ocean.BLOCK_SIZE
        y = (self.shark.head_position.top - self.position[1]) / Ocean.BLOCK_SIZE
        cells += self.ocean[math.floor(y)][math.floor(x)]

        x = (self.shark.head_position.right - self.position[0]) / Ocean.BLOCK_SIZE
        y = (self.shark.head_position.top - self.position[1]) / Ocean.BLOCK_SIZE
        cells += self.ocean[math.floor(y)][math.floor(x)]

        x = (self.shark.head_position.left - self.position[0]) / Ocean.BLOCK_SIZE
        y = (self.shark.head_position.bottom - self.position[1]) / Ocean.BLOCK_SIZE
        cells += self.ocean[math.floor(y)][math.floor(x)]

        x = (self.shark.head_position.right - self.position[0]) / Ocean.BLOCK_SIZE
        y = (self.shark.head_position.bottom - self.position[1]) / Ocean.BLOCK_SIZE
        cells += self.ocean[math.floor(y)][math.floor(x)]

        return cells

    def move(self, movement):
        self.position[0] += movement[0] * Ocean.SPEED
        self.position[1] += movement[1] * Ocean.SPEED
        if '0' in self.get_shark_cell():
            self.move((movement[0] * -3, movement[1] * -3))


    def render(self):
        for y, row in enumerate(self.ocean):
            for x, cell in enumerate(row):
                Screen.screen.blit(Ocean.BLOCKS[Ocean.CODES[cell]],
                                   (x * Ocean.BLOCK_SIZE + self.position[0],
                                    y * Ocean.BLOCK_SIZE + self.position[1]))

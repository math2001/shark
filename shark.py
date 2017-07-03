# -*- encoding: utf-8 -*-

from functions import *
from fish import Fish

class Shark(Fish):

    def __init__(self):
        Fish.__init__(self, 'shark')

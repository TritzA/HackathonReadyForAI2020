from Src.Models.vector2 import Vector2

class PlayerPosition:
    '''
    This class represents the positions of each body part of a player.
    '''

    def __init__(self, h=Vector2(), n=[], b=[]):
        self.Head = h
        self.Neck = n
        self.Body = b

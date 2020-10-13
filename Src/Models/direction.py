#######################################
#  ATTENTION: Do not touch this file  #  
#######################################

from Src.Models.vector2 import Vector2

class Direction():
    '''
    Those constants represents the available directions that the AI can choose from for his next move.
    ATTENTION: If you change these values, your next move will be considered invalid
    '''
    _UP = Vector2( 0,  1 )
    _DOWN = Vector2(0, -1)
    _RIGHT = Vector2(1, 0)
    _LEFT = Vector2(-1, 0)
    _NONE = Vector2(0, 0)

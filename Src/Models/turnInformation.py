#######################################
#  ATTENTION: Do not touch this file  #  
#######################################
import json

class TurnInformation():
    '''
    This class groups together information about the current turn the player can use to decide their next move.
    '''

    def __init__(self, j):
        self.SelfId = ""
        self.Map = []
        self.MapWidth = 0
        self.MaxMovement = 0
        self.MovementLeft = 0
        self.OccupiedTiles = {}
        self.__dict__.update(json.loads(j))

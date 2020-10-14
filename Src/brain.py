from Src.Helpers.singleton import Singleton
from Src.Models.direction import Direction
from Src.Models.turnInformation import TurnInformation
import random
import numpy as np


class Brain(metaclass=Singleton):

    def on_next_move(turn_info: TurnInformation):
        '''
        YOUR CODE GOES IN THIS FUNCTION. This is where your AI takes a decision on his next move.
        @param turn_info: Information from the current turn
        @return: The direction your AI chose as his next move.
        '''

        print(
            "the game server wants to know your next move and you have the following informations : the id is {0} and the current map is {1} ".format(
                turn_info.SelfId, turn_info.Map))
        
        # convertir la liste en matrice 2D
        m = turn_info.Map
        le = turn_info.MapWidth
        array = np.array(m).reshape(le, le)

        # obtenir les positions actuels
        b = turn_info.OccupiedTiles
        coordhead = b['Head'][0]
        x = le - 1 - int(coordhead['Y'])
        y = int(coordhead['X'])

        left = array[x][y - 1]
        right = array[x][y + 1]
        up = array[x - 1][y]
        down = array[x + 1][y]

        id = str(turn_info.SelfId)
        fg = 'P' + id + '*-P' + id
        fj = 'P' + id + '-P' + id + '*'
        g = 'P' + id + '*'
        d = 'P' + id

        if array[x][y] == fg or array[x][y] == fj: # si notre position actuelle est sur notre corps
            # aller dans le vide
            if left == '':
                return Direction._LEFT
            elif up == '':
                return Direction._UP
            elif right == '':
                return Direction._RIGHT
            elif down == '':
                return Direction._DOWN
            # aller sur notre corps
            elif left == d:
                return Direction._LEFT
            elif up == d:
                return Direction._UP
            elif right == d:
                return Direction._RIGHT
            elif down == d:
                return Direction._DOWN
            # aller sur le corps de l'adversaire
            elif left[0] == 'p':
                return Direction._LEFT
            elif up[0] == 'p':
                return Direction._UP
            elif right[0] == 'p':
                return Direction._RIGHT
            elif down[0] == 'p':
                return Direction._DOWN
        
        # si notre position actuelle est dans le vide
        # aller sur notre corps qui est forcément à 1 de distance
        if left == d:
            return Direction._LEFT
        elif up == d:
            return Direction._UP
        elif right == d:
            return Direction._RIGHT
        elif down == d:
            return Direction._DOWN

        # cmpt=random.randint(0,4)
        # if cmpt % 4 == 0:
        #    cmpt += 1
        #    return Direction._UP
        # elif cmpt % 4 == 1:
        #    cmpt += 1
        #    return Direction._LEFT
        # elif cmpt % 4 == 2:
        #    cmpt += 1
        #    return Direction._DOWN
        # else:
        #    cmpt += 1
        #    return Direction._RIGHT


    def on_finalized(turn_info: TurnInformation):
        '''
        Once the game is finished, this method is triggered with the final state of the map. 
        It could be used to train the AI for example.
        @param turn_info: Information from the current turn
        '''
        print("the game has ended and the received id from the game server is {0} with the following map {1}".format(
            turn_info.SelfId, turn_info.Map))

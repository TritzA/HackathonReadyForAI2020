from Src.Helpers.singleton import Singleton
from Src.Models.direction import Direction
from Src.Models.turnInformation import TurnInformation
import random
import numpy as np


def randomize(a: bool, b: bool, c: bool, d: bool):
    while True:
        cmpt = random.randint(0, 4)
        if cmpt % 4 == 0 and b:
            return Direction._UP
        elif cmpt % 4 == 1 and a:
            return Direction._LEFT
        elif cmpt % 4 == 2 and d:
            return Direction._DOWN
        elif cmpt%4 == 3 and c:
            return Direction._RIGHT


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
        e = turn_info.OccupiedTiles
        coordhead = e['Head'][0]
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
        f = 'P' + id
        a, b, c, d = False, False, False, False
        print(array)
        if array[x][y] == fg or array[x][y] == fj:  # si notre position actuelle est sur notre corps
            # aller dans le vide
            if left == '':
                a=True
            if up == '':
                b=True
            if right == '':
                c=True
            if down == '':
                d=True
            if a or b or c or d:
                print('h')
                print(randomize(a,b,c,d))
                return randomize(a,b,c,d)

            # aller sur notre corps
            if left == f:
                a=True
            if up == f:
                b=True
            if right == f:
                c=True
            if down == f:
                d=True
            if a or b or c or d:
                print('h')
                return randomize(a,b,c,d)

            # aller sur le corps de l'adversaire
            if left[0] == 'p':
                a = True
            if up[0] == 'p':
                b=True
            if right[0] == 'p':
                c=True
            if down[0] == 'p':
                d=True
            if a or b or c or d:
                print('h')
                return randomize(a,b,c,d)

        # si notre position actuelle est dans le vide
        # aller sur notre corps qui est forcément à 1 de distance
        if left == f:
            a=True
        if up == f:
            b=True
        if right == f:
            c=True
        if down == f:
            d=True
        if a or b or c or d:
            print('h')
            return randomize(a,b,c,d)

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
from Src.Helpers.singleton import Singleton
from Src.Models.direction import Direction
from Src.Models.turnInformation import TurnInformation


class Brain(metaclass=Singleton):
    cmpt = 0

    def on_next_move(turn_info: TurnInformation):
        '''
        YOUR CODE GOES IN THIS FUNCTION. This is where your AI takes a decision on his next move.
        @param turn_info: Information from the current turn
        @return: The direction your AI chose as his next move.
        '''

        print(
            "the game server wants to know your next move and you have the following informations : the id is {0} and the current map is {1} ".format(
                turn_info.SelfId, turn_info.Map))
        global cmpt
        if cmpt % 4 == 0:
            return Direction._UP
        elif cmpt % 4 == 1:
            return Direction._LEFT
        elif cmpt % 4 == 2:
            return Direction._DOWN
        else:
            return Direction._RIGHT

        # global choix prochain move
        # Fonctions utiles:
        # Calcul du nombre de bloc nous séparant de notre zone
        # retourne blocs, choix prochain move

        # Si nb_pas_restants == distance notre_tête-zone:
        # Retour en ligne droite vers notre zone

        # Si une des possibilités de prochain move == W:
        # trouver options où pas de mur next move
        # parmis ces options, trouver celle plus proche de notre zone:
        # si 2 options égales: Choisir option la plus loin de ennemi le plus proche

        # Défensive:
        # Si distance notre zone + 3 >= distance tête adversaire / - notre coup:
        #

        # Offensive:
        # Si tête adversaire dans notre zone AND notre tête dans notre zone:
        # Direction vers cou/tête adversaire

        # As a default we put that the direction to UP.

    def on_finalized(turn_info: TurnInformation):
        '''
        Once the game is finished, this method is triggered with the final state of the map. 
        It could be used to train the AI for example.
        @param turn_info: Information from the current turn
        '''
        print("the game has ended and the received id from the game server is {0} with the following map {1}".format(
            turn_info.SelfId, turn_info.Map))

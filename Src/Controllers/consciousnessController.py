
#######################################
#  ATTENTION: Do not touch this file  #  
#######################################
import json
from flask import Flask, Blueprint, request
from Src.Models.turnInformation import TurnInformation
from Src.Models.direction import Direction
from Src.brain import Brain


ConsciousnessController = Blueprint('ConsciousnessController', __name__, template_folder='templates')

@ConsciousnessController.route('/Consciousness/GetStatus/', methods = ['GET'])
def get_Status():
    '''
    Endpoint to test communication with the player.
    @return: True
    '''
    return json.dumps(True)

@ConsciousnessController.route('/Consciousness/OnNextMove/', methods = ['POST'])
def on_next_move():
    '''
    Endpoint to get the next move the AI will make.
    @return: The direction your AI chose as his next move.
    '''

    toSend = Brain.on_next_move(turn_info=TurnInformation(request.data))
    return json.dumps(toSend.__dict__)

@ConsciousnessController.route('/Consciousness/PutFinalMap/', methods = ['PUT'])
def put_final_map():
    '''
    Endpoint to provide the last state of the map to the player.
    '''

    Brain.on_finalized(turn_info=TurnInformation(request.data) )
    return json.dumps(True)


    
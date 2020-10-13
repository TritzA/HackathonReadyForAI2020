from Src.Models.playerPosition import PlayerPosition
from Src.Models.vector2 import Vector2

def get_other_players_position(self_id, map, map_width):
    '''
    Gets the positions of all other players.
    @param selfId: The id of the player calling the function.
    @param map: The map of the current turn.
    @param mapWidth: The size of a row in the map.
    '''

    other_players_position = {}
    c_counter = 0
    r_counter = map_width - 1

    for pos in map:
        if "P" in pos or "p" in pos:
            splitPos = pos.split("-")
            splitPos = filter(lambda s: ("P" in s or "p" in s) and str(self_id) not in s, splitPos )
            for v in splitPos:
                playerId = v[1]
                if playerId not in other_players_position:
                    other_players_position[playerId] = PlayerPosition(Vector2(), [], [])

                if "*" in v:
                    other_players_position[playerId].Head = Vector2(X=c_counter, Y=r_counter)
                elif "p" in v:
                    other_players_position[playerId].Neck.append(Vector2(X=c_counter, Y=r_counter))
                else:
                    other_players_position[playerId].Body.append(Vector2(X=c_counter, Y=r_counter))


        c_counter += 1
        if c_counter >= map_width:
            c_counter = 0
            r_counter -= 1

    return other_players_position

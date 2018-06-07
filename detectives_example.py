#!/bin/python

## AI for the detectives

from engine.player import Player
from engine import boardmap
from typing import List, Tuple
import random


# Play Move, takes mr x and returns the move he wishes to make
# Returns: the chosen move, a tuple ((int) new location, (string) transport type)
def play_move(detective: Player, detectives: List[Player], x_history: List[Tuple[int, str]]) -> Tuple[int, str]:
    # This fancy line just shows which tickets we have that can be used
    transport = map(lambda x: x[0], filter(lambda x: x[1] > 0 and x[0] in boardmap[detective.pos].keys(), detective.tickets.items()))
    valid_nodes = []
    for t in transport:
        for neighbor in boardmap[detective.pos][t]:
            if neighbor not in [d.pos for d in detectives]:
                valid_nodes.append((neighbor, t))
    # And return a tuple: int, string
    return random.choice(valid_nodes)

#!/bin/python

## AI for the detectives

from engine.player import Player
from engine import boardmap
from typing import List, Tuple
import random


# Play Move, takes mr x and returns the move he wishes to make
# Returns: the chosen move, a tuple ((int) new location, (string) transport type)
def play_move(detective: Player, detectives: List[Player], x_history: List[Tuple[int, str]]) -> Tuple[int, str]:
    # This fancy line just picks a random move based on the available tickets and location
    transport = random.choice(list(filter(lambda x: x[1] > 0 and x[0] in boardmap[detective.pos].keys(), detective.tickets.items())))[0]
    # And return a tuple: int, string
    return random.choice(boardmap[detective.pos][transport]), transport

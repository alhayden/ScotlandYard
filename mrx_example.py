#!/bin/python

## AI for Mr. X

from engine.player import Player
from engine import boardmap
from typing import List, Tuple
import random


# Play Move, takes mr x and returns the move he wishes to make
# Returns: the chosen move, a tuple ((int) new location, (string) transport type)
def play_move(mr_x: Player, detectives: List[Player], x_history: List[Tuple[int, str]]) -> Tuple[int, str]:
    # Only returns taxi moves in this example
    return random.choice(boardmap[mr_x.pos]["taxi"]), "taxi"

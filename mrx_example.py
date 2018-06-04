#!/bin/python

## AI for Mr. X

from engine.player import Player
from typing import List, Tuple
import random

boardmap = {}
t = "taxi"
b = "bus"
u = "undergound"
with open("board_data.txt", "r") as f:
    for line in f:
        data = [a.strip() for a in line.split("|")]
        entry = {}
        if len(data) > 1 and data[1] != '':
            entry[t] = [int(a.strip()) for a in data[1].split(" ")]
        if len(data) > 2 and data[2] != '':
            entry[b] = [int(a.strip()) for a in data[2].split(" ")]
        if len(data) > 3 and data[3] != '':
            entry[u] = [int(a.strip()) for a in data[3].split(" ")]

        blackTicket = []
        for key in entry.keys():
            blackTicket += entry[key]

        entry["black"] = blackTicket

        if len(data) > 4:
            entry["black"] += [int(a.strip()) for a in data[4].split(' ')]

        if len(data) > 0:
            boardmap[int(data[0])] = entry


# Play Move, takes mr x and returns the move he wishes to make
# Returns: the chosen move, a tuple ((int) new location, (string) transport type)
def play_move(mr_x: Player, detectives: List[Player], x_history: List[Tuple[int, str]]) -> Tuple[int, str]:
    return random.choice(boardmap[mr_x.pos]["taxi"]), "taxi"
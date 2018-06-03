#!/bin/python3

class Player:
    def __init__(self, tickets, pos):
        self.tickets = tickets
        self.pos = pos

    def __eq__(self, other):
        return self.pos == other.pos and self.tickets == other.tickets

    def move(self, transportation, new_nodeid):
        # TODO: do some validation and then move, also fix tickets
        pass

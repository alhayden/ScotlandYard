#!/bin/python3

import random
import copy
from .player import Player


class Game:
    def __init__(self, mr_x, detectives):
        self.detectives_ai = detectives
        self.mr_x_ai = mr_x
        self.boardmap = {}
        self.x_history = []
        self.detectives = []
        self.x = None
        self.load_board()
        self.round = 0
        self.turn = 0
        self.reveal_rounds = [3, 8, 13, 18, 24]
        
        
        startTickets = {"taxi" : 10, "bus" : 8, "underground" : "4"}
        
        startLocs = []
        with open("start_locations.txt", "r") as f:
            for line in f:
                startLocs.append(int(line.strip()))
        random.shuffle(startLocs)    
        
        self.x = Player({"taxi" : 100, "bus": 100, "underground" : 100, "black" : 5, "2x" : 2}, startLocs[0], "X")

        names = ["A", "B", "C", "D", "E"]

        for n in range(len(names)):
            self.detectives.append(Player(dict(startTickets), startLocs[n + 1], names[n]))
            
        
    def next_turn(self, doReset=True):
        turn = self.turn
        self.turn += 1
        
        detectives_public = [copy.deepcopy(p) for p in self.detectives]
        x_public = copy.deepcopy(self.x)

        ## Mr. X's turn
        if turn <= 0:
             self.mr_x_ai.play_move(x_public, detectives_public, copy.deepcopy(self.x_history))

        if self.x != x_public:
            self.gameEnd(False) ## X loses

        if x_public.nextMove[1] == "2x" and self.x.tickets["black"] > 0:
            self.turn = -1
            self.x.tickets["black"] = self.x.tickets["black"] - 1
            return

            if self.moveValid(x_public):
                self.x.pos = x_public.nextMove[0]
                transport = x_public.nextMove[1]
                self.x.tickets[transport] = self.x.tickets[transport] - 1
            if self.x.tickets[transport] < 0:
                self.gameEnd(False) ## X loses

            self.x_history.append((self.x.pos, transport))
            return

        ## Detective's turn
        for i in range(len(self.x_history)):
            if i in self.reveal_rounds:
                x_history_public.append(self.x_history[i])
            else:
                x_history_public.append((None, self.x_history[i][1]))

        detective_public = self.detectives_public[turn - 1]

        self.detectives_ai.play_move(detective_public, detectives_public, copy.deepcopy(x_history_public))


        detective = self.detectives[turn - 1]
        if detective != detective_public:
            self.gameEnd(True) #X wins

        if detective_public.nextMove == None and self.cantMove(detective_public):
            return

        if self.moveValid(detective_public):
            detective.pos = detective_public.nextMove[0]
            transport = detective_public.nextMove[1]
            detective.tickets[transport] = detective.tickets[transport] - 1
            if detective.tickets[transport] < 0:
                self.gameEnd(True) ## X wins

        self.checkGameOver()

        if self.turn >= 6 and doReset:
            self.turn = 0
            self.round += 1
        
 

    def next_round(self):
        self.round += 1

        self.detectives_public = [copy.deepcopy(p) for p in self.detectives]
        self.x_public = copy.deepcopy(self.x)

        self.turn = 0
        while self.turn < 6:
            self.next_turn(False)

        
    def moveValid(self, player):
        return player.nextMove[0] in self.boardmap[player.pos][player.nextMove[1]]

    def cantMove(self, player):
        for ticket in player.tickets.keys():
            if player.tickets[ticket] > 0 and ticket in self.boardmap[player.pos]:
                return False
        return True

    def checkGameOver(self):
        return any(mrx.pos == plr.pos for plr in self.detectives)

    def gameEnd(self, xwins):
        if xwins:
            print("Mr. X won!")
        else:
            prin("The Detectives Won!")

    def load_board(self):
        t = "t"
        b = "b"
        u = "u"
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
    
                entry["?"] = blackTicket
                
                if len(data) > 4:
                    entry["?"] += [int(a.strip()) for a in data[4].split(' ')]
     
                if len(data) > 0:
                    self.boardmap[int(data[0])] = entry


    # self.detectives: an array of Player objects, but only the detcvitvs
    # self.x: mr. x, a player object

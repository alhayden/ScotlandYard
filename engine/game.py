#!/bin/python3

import random


class Game:
    def __init__(self, mr_x, detectives):
        self.boardmap = {}
        self.x_history = []
        self.detectives = []
        self.x = None
        self.load_board()
        
        
        startTickets = {"taxi" : 10, "bus" : 8, "underground" : "4"}
        
        startLocs = []
        with open("start_locations.txt", "r") as f:
            for line in f:
                startLocs.append(int(line.strip()))
        random.shuffle(startLocs)    
        
        self.x = Player({"taxi" : 100, "bus": 100, "underground" : 100, "black" : 5, "2x" : 2}, startLocs[0], "X")

        names = ["A", "B", "C", "D", "E"]

        for n in range(len(names)):
            self.detectives.append(Player(startTickets[:], startLocs[n + 1], names[n]))
            
        
    def next_turn(self):
        pass # TODO: run the next turn

    def next_round(self):
        pass # TODO: run the next roundA

    def load_board(self):
        t = "t"
        b = "b"
        u = "u"
        with open("board_data.txt", "r") as f:
            for line in f:
                data = [a.strip() for a in line.split("|")]
                entry = {}
                if len(data) > 1:
                    entry[t] = [int(a.strip()) for a in data[1].split(" ")]
                if len(data) > 2:
                    entry[b] = [int(a.strip()) for a in data[2].split(" ")]
                if len(data) > 3:
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

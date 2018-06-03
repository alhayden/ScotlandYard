#!/bin/python

## Master program for running games
## Loads AIs from their respective files and starts the game

from engine.game import Game
from gui import Window

def main():
    try:
        import mrx
    except:
        print("Failed to load Mr. X AI.  Make sure it is in this directory and named 'mrx.py'")
        exit(1)
    try:
        import detectives
    except:
        print("Failed to load the detective AI.  Make sure it is in this directory and named 'detectives.py'")
        exit(1)
    the_game = Game(mrx, detectives)
    win = Window(the_game)

    win.mainloop()

if __name__ == "__main__":
    main()

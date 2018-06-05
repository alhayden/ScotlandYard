# ScotlandYard
Simple Python interface for AI playing the board game "Scotland Yard"

## Usage instructions
1. Create a module called `mrx` that will control all of Mr. X's moves.
2. Create a module called `detectives` that will control the detective's moves.
3. Run the game by by running `master.py`

** You may need to install 'Pillow', use "pip install pillow" to do so

Moves are structured as a tuple (x, y), where x is the node number the player is moving to and y is the identifier for the type of transportation moved.  e.g. (181, "taxi") or (13, "underground") or (77, "bus")
Mr. X's double moves are in the form ("2x", (x, y), (x, y)), e.g. ("2x", (112, "taxi"), (111, "taxi"))

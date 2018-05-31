#!/bin/python

## Master program for running games
## Loads AIs from their respective files


try:
    import mrx
except:
    print("Failed to load Mr. X AI.  Make sure it is in this directory and named 'mrx.py'")
try:
    import detectives
except:
    print("Failed to load the detective AI.  Make sure it is in this directory and named 'detectives.py'")


def load():
    global auto, output_level
    auto = False
    output_level = 0
    try:
        f = open("config.txt", "r")
        

        f.close()
    except:
        print("Failed to load config file, continuing with defaults...")
        f = open("config.txt", "w")
        f.write("## Scotland yard master config\n")
        
        f.write("# Ask for input before running round?\n")
        f.write("autorun: true\n")
        
        f.write("# detail of game logging, 'all', 'board', 'players'\n")
        f.write("detail: all\n")
        f.close()





def main():
    global auto

    load()
    
    ticketHistory = []
    
    

if __name__ == "__main__":
    main()

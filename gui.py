#!/bin/python3
from tkinter import Tk, Canvas, Label, Button, Scale

class Window(Tk):
    def __init__(self, game):
        Tk.__init__(self)
        self.game = game

        # create widgets
        self.board_canvas = Canvas(self)
        self.label_current_player = Label(self, text="Current Player: Mr. X")
        self.button_next_turn = Button(self, text="Next Turn", command=self.next_turn)
        self.slider_automove_speed = scale = Scale(self, orient='horizontal', from_=0, to_=10000)
        self.button_toggle_automove = Button(self, text="Start Automove", command=self.toggle_automove)
        
        # layout widgets
        self.board_canvas.grid(row=0, column=0, rowspan=5)
        self.label_current_player.grid(row=0, column=1)
        self.button_next_turn.grid(row=1, column=1)
        self.slider_automove_speed.grid(row=2, column=1)
        self.button_toggle_automove.grid(row=3, column=1)

        # for 4k
        self.tk.call('tk', 'scaling', 5.0)
        
    def next_turn(self, *args):
        print(self.winfo_pixels('1i'))
        self.game.next_turn()
        self.update_ui()
    
    def update_ui(self):
        pass

    def toggle_automove(self, *args):
        pass

    def automove(self, *args):
        pass

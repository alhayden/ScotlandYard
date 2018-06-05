#!/bin/python3
from tkinter import Tk, Canvas, Label, Button, Scale, Frame
from PIL import ImageTk, Image
from engine.game import Game


class Window(Tk):
    def __init__(self, game: Game):
        Tk.__init__(self)
        # for 4k
        self.tk.call('tk', 'scaling', '-displayof', '.', 1)
        self.game = game
        self.is_automoving = False

        # create widgets
        self.board_canvas = Canvas(self, background="white")
        self.control_frame = Frame(self)
        self.label_current_player = Label(self.control_frame, text="Current Player: Mr. X")
        self.button_next_turn = Button(self.control_frame, text="Next Turn", command=self.next_turn)
        self.slider_automove_speed = scale = Scale(self.control_frame, orient='horizontal', from_=0, to_=10000)
        self.button_toggle_automove = Button(self.control_frame, text="Start Automove", command=self.toggle_automove)

        # layout widgets
        self.board_canvas.pack(fill='both', expand=True, anchor='w')
        self.control_frame.pack(before=self.board_canvas, side='right', anchor='e')
        self.label_current_player.pack(fill='x')
        self.button_next_turn.pack(fill='x')
        self.slider_automove_speed.pack(fill='x')
        self.button_toggle_automove.pack(fill='x')

        # setup canvas
        self.board_img_pil = Image.open('board.jpg')
        self.board_img = ImageTk.PhotoImage(self.board_img_pil)
        self.img_id = self.board_canvas.create_image(300, 300, image=self.board_img)

        # move image on resize
        self.bind("<Configure>", self.update_ui)
        self.old_canvas_size = self.winfo_width(), self.winfo_height()
        self.player_rects = [self.board_canvas.create_rectangle(0, 0, 1, 1, fill="red") for _ in self.game.players]
        self.player_txts = [self.board_canvas.create_text(0, 0, text=plr.name) for plr in self.game.players]

        # create data for node locations on image
        node_locations = {}
        with open("node_locations.txt", "r") as f:
            for line in f:
                l = line.split(" ")
                node_locations[int(l[0])] = (float(l[1]), float(l[2]))

    def next_turn(self, *_):
        self.game.next_turn()
        self.update_ui()

    def update_ui(self, *_):
        width = self.board_canvas.winfo_width()
        height = self.board_canvas.winfo_height()
        if self.old_canvas_size != (width, height):  # don't update the image unless we *have* to
            print("Resizing...")
            tmp_pil = self.board_img_pil.resize((width, height))
            self.board_canvas.delete(self.img_id)
            self.board_img = ImageTk.PhotoImage(tmp_pil)
            self.img_id = self.board_canvas.create_image(int(width / 2), int(height / 2), image=self.board_img)

        for i, player in self.game.players:
            pass

    def toggle_automove(self, *_):
        if not self.is_automoving:
            self.is_automoving = True
            self.automove()
        else:
            self.is_automoving = False

    def automove(self, *_):
        if not self.is_automoving:
            return
        self.next_turn()

        self.after(self.slider_automove_speed.get(), self.automove)

from tkinter import Tk, Canvas
from PIL import ImageTk, Image

root = Tk()
cnv = Canvas(root, width=2000, height=2000)
img = Image.open("board.jpg")
img = img.resize((2000, 2000))
img = ImageTk.PhotoImage(image=img)
cnv.create_image(1000, 1000, image=img)
n = 1
def callback(evt):
    global n
    print(n, evt.x / 1000, evt.y / 1000)
    n += 1

cnv.bind("<Button-1>", callback)

cnv.pack()

root.mainloop()

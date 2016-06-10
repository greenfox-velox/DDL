from tkinter import *
from gameboard import *
from character import *
from levels import *

def main():
    root = Tk()
    canvas_width = 720
    canvas_height = 720
    canvas = Canvas(root, width = canvas_width, height = canvas_height)
    canvas.pack()

    level1 = Gameboard(canvas)
    root.bind('<KeyPress>', level1.keypress)

    root.mainloop()

main()

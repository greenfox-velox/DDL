from tkinter import*
root = Tk()

canvas_width = 300
canvas_height = 300
canvas = Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()

center_x = canvas_width / 2
center_y = canvas_height / 2

def line_drawing(x, y):
    line = canvas.create_line(x, y, center_x, center_y)

for i in range(16):
    x = i * 20
    y = i * 20
    line_drawing(x, 0)
    line_drawing(x, canvas_height)
    line_drawing(0, y)
    line_drawing(canvas_width, y)

line_drawing(0, 0)
root.mainloop()

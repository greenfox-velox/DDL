from tkinter import*
root = Tk()

canvas_width = 300
canvas_height = 300

canvas = Canvas(root, width = canvas_width, height = canvas_height, bg='olive')
canvas.pack()
a = 2
b = 3
c = 5

def yellow_fractal(x, y, z):
    canvas.create_rectangle(x+z, y, x+a*z, y+z)
    canvas.create_rectangle(x+a*z, y+z, x+b*z, y+a*z)
    canvas.create_rectangle(x, y+z, x+z, y+a*z)
    canvas.create_rectangle(x+z, y+a*z, x+a*z, y+b*z)
    if z < c:
        pass
    else:
        yellow_fractal(x+z, y, z//b)
        yellow_fractal(x, y+z, z//b)
        yellow_fractal(x+z*a, y+z, z//b)
        yellow_fractal(x+z, y+a*z, z//b)

yellow_fractal(0,0,100)

root.mainloop()

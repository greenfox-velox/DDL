from tkinter import*
root = Tk()

canvas_width = 300
canvas_height = 300

canvas = Canvas(root, width = canvas_width, height = canvas_height, bg='olive')
canvas.pack()


def yellow_fractal(x, y, size): #cord/size
    canvas.create_rectangle(x+size, y, x+2*size, y+size)
    canvas.create_rectangle(x+2*size, y+size, x+3*size, y+2*size)
    canvas.create_rectangle(x, y+size, x+size, y+2*size)
    canvas.create_rectangle(x+size, y+2*size, x+2*size, y+3*size) #draw basic rectangles

    if size < 3: #if size is less than 3, stop
        pass
    else:
        yellow_fractal(x+size, y, size//3) #x cord + size ---> , size shrink to its third
        yellow_fractal(x, y+size, size//3) #y cord + size ---> , size shrink to its third
        yellow_fractal(x+size*2, y+size, size//3) #x cord + size ---> , size shrink to its third
        yellow_fractal(x+size, y+2*size, size//3) #x cord + size ---> , size shrink to its third

yellow_fractal(0,0,100)

root.mainloop()

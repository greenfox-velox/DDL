from tkinter import *

root = Tk()
canvas = Canvas(root, width=300, height=300)
canvas.pack()

def fractal(x, y, size):
    canvas.create_rectangle(x, y, x+size, y+size, fill = 'olive')
    # canvas.create_rectangle(x, y, x+size, y+2*size, fill = 'blue')
    # canvas.create_rectangle(x, y, x+size, y+size, fill = 'yellow')
    # canvas.create_rectangle(x, y, x+size, y+size, fill = 'purple')

    # if size < 3:
    #     pass
    # else:
    #     fractal(x, y, size/3)
    #     fractal(x+size/3, y+size/3, size/3)

fractal(5, 5, 290)

root.mainloop()
# 
# def yellow_fractal(x, y, size): #cord/size
#     canvas.create_rectangle(x+size, y, x+2*size, y+size)
#     canvas.create_rectangle(x+2*size, y+size, x+3*size, y+2*size)
#     canvas.create_rectangle(x, y+size, x+size, y+2*size)
#     canvas.create_rectangle(x+size, y+2*size, x+2*size, y+3*size) #draw basic rectangles
#
#     if size < 3: #if size is less than 3, stop
#         pass
#     else:
#         yellow_fractal(x+size, y, size//3) #x cord + size ---> , size shrink to its third
#         yellow_fractal(x, y+size, size//3) #y cord + size ---> , size shrink to its third
#         yellow_fractal(x+size*2, y+size, size//3) #x cord + size ---> , size shrink to its third
#         yellow_fractal(x+size, y+2*size, size//3) #x cord + size ---> , size shrink to its third
#
# yellow_fractal(0,0,100)

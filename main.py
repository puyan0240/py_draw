import tkinter
from tkinter import ttk


mouse_x = mouse_y = 0
mouse_old_x = mouse_old_y = 0
mouse_right_click = mouse_left_click = 0


def mouse_move(e):
    global mouse_x,mouse_y
    global mouse_old_x,mouse_old_y

    mouse_old_x = mouse_x
    mouse_old_y = mouse_y
    mouse_x = e.x
    mouse_y = e.y

    canvas.create_line(mouse_x, mouse_y, mouse_old_x, mouse_old_y, fill="BLACK", width=1)


def test(e):
    print(str(e.keycode))
    print(str(e.type))
    print(str(e.keysym))
    print(e)


root = tkinter.Tk()
root.title("Draw")
#root.geometry("600x400")
root.bind("<Motion>", mouse_move)
root.bind("<Button-1>", test)
root.bind("<ButtonRelease-1>", test, "+")

canvas = tkinter.Canvas(root, width=400, height=600, bg="WHITE")
canvas.pack()

root.mainloop()
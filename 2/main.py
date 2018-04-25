from tkinter import *
from tkinter import messagebox
from math import *
import numpy as np


root = Tk()
root.title("Эпициклоида")
root.geometry('1000x600+100+100')

Canv = Canvas(root, width=800, height=600)
Canv.pack(side='left')

Buttons = Frame(root)

Transfer = Frame(Buttons)
Scale = Frame(Buttons)
Turn = Frame(Buttons)

# Перенос
TrvalueL = Label(Transfer, text='Перенос', font='Verdana 16').grid(row=0, column=0, columnspan=4)
TrxL = Label(Transfer, text='dX', font='Verdana 14').grid(row=1, column=0)
TryL = Label(Transfer, text='dY', font='Verdana 14').grid(row=1, column=2)

# Масштабирование
SvalueL = Label(Scale, text='Масштабирование', font='Verdana 16').grid(row=0, column=0, columnspan=4)
SxL = Label(Scale, text='Xc', font='Verdana 14').grid(row=1, column=0)
SyL = Label(Scale, text='Yc', font='Verdana 14').grid(row=1, column=2)
ScxL = Label(Scale, text='KX', font='Verdana 14').grid(row=2, column=0)
ScyL = Label(Scale, text='KY', font='Verdana 14').grid(row=2, column=2)

# Поворот
TuvalueL = Label(Turn, text='Поворот', font='Verdana 16').grid(row=0, column=0, columnspan=4)
TuxL = Label(Turn, text='  X', font='Verdana 14').grid(row=1, column=0)
TuyL = Label(Turn, text='Y', font='Verdana 14').grid(row=1, column=2)
TuangL = Label(Turn, text='Угол', font='Verdana 14').grid(row=2, column=0, columnspan=2)

# Перенос
TrxV = Entry(Transfer, width=5)
TryV = Entry(Transfer, width=5)


# Масштабирование
SxV = Entry(Scale, width=5)
SyV = Entry(Scale, width=5)
ScxV = Entry(Scale, width=5)
ScyV = Entry(Scale, width=5)

# Поворот
TuxV = Entry(Turn, width=5)
TuyV = Entry(Turn, width=5)
TuangV = Entry(Turn, width=10)

#Перенос
TrxV.grid(row=1, column=1)
TryV.grid(row=1, column=3)

# Масштабирование
SxV.grid(row=1, column=1)
SyV.grid(row=1, column=3)
ScxV.grid(row=2, column=1)
ScyV.grid(row=2, column=3)

# Поворот
TuxV.grid(row=1, column=1)
TuyV.grid(row=1, column=3)
TuangV.grid(row=2, column=2, columnspan=2)

def create():
    global Points, Begin_points, Square, Begin_square

    dx = 400
    dy = 300
    kx = 10
    ky = 10
    a = 1
    b = 3
    for t in np.arange(0, 2 * pi, 0.001):
        x = (a + b) * cos(t) * kx - a * cos((a + b) / a * t) * kx + dx
        y = (a + b) * sin(t) * ky - a * sin((a + b) / a * t) * ky + dy
        Points.append([x, y])
    Begin_points = Points.copy()

    Square = [[300, 200], [500, 200], [500, 400], [300, 400]]
    Begin_square = Square.copy()
    print(len(Points))

def draw():
    global Points, Canv, Square

    Canv.delete('all')

    print(Square)

    Canv.create_polygon(Square, fill='#e6e6fa', outline='black')

    Canv.create_polygon(Points, fill='#ffffff', outline='black')

    Canv.create_line(0, 3, 800, 3)
    Canv.create_text(100, 10, text='100')
    Canv.create_text(200, 10, text='200')
    Canv.create_text(300, 10, text='300')
    Canv.create_text(400, 10, text='400')
    Canv.create_text(500, 10, text='500')
    Canv.create_text(600, 10, text='600')
    Canv.create_text(700, 10, text='700')
    Canv.create_text(790, 10, text='X')
    Canv.create_line(3, 0, 3, 600)
    Canv.create_text(16, 100, text='100')
    Canv.create_text(16, 200, text='200')
    Canv.create_text(16, 300, text='300')
    Canv.create_text(16, 400, text='400')
    Canv.create_text(16, 500, text='500')
    Canv.create_text(12, 585, text='Y')
    Canv.create_text(12, 10, text='0')
    Canv.create_line(0, 596, 800, 596)
    Canv.create_line(801, 0, 801, 600)


def Transfer_ep():
    global TrxV, TryV, Canv, Points, Back_points, Back_square

    code = 0

    try:
        Trx = float(TrxV.get())
        Try = float(TryV.get())
    except ValueError:
        messagebox.showerror('Ошибка', 'Некорректный ввод коэффициентов перемещения.')
        code = 1

    if code == 0:
        Back_points.clear()
        Back_points = Points.copy()
        Points.clear()

        for i, element in enumerate(Back_points):
            x = element[0] + Trx
            y = element[1] + Try
            Points.append([x, y])

        Back_square.clear()
        Back_square = Square.copy()
        Square.clear()

        for i, element in enumerate(Back_square):
            x = element[0] + Trx
            y = element[1] + Try
            Square.append([x, y])
        print(Square)

        draw()

def Scale_ep():
    global Points, Back_points, Square, Back_square

    code = 0
    try:
        Xc = float(SxV.get())
        Yc = float(SyV.get())
    except ValueError:
        messagebox.showerror('Ошибка', 'Некорректный ввод центра масштабирования.')
        code = 1
    try:
        kx = float(ScxV.get())
        ky = float(ScyV.get())
    except ValueError:
        messagebox.showerror('Ошибка', 'Некорректный ввод коэффициентов масштабирования.')
        code = 1

    if code == 0:
        print(kx, ky)
        Back_points.clear()
        Back_points = Points.copy()
        Points.clear()

        Back_square.clear()
        Back_square = Square.copy()
        Square.clear()

        for i, element in enumerate(Back_points):
            x = kx*element[0] + (1-kx)*Xc
            y = ky*element[1] + (1-ky)*Yc
            Points.append([x, y])


        for i, element in enumerate(Back_square):
            x = kx * element[0] + (1 - kx) * Xc
            y = ky * element[1] + (1 - ky) * Yc
            Square.append([x, y])

        draw()

def Turn_ep():
    global Points, Back_points, Square, Back_square

    code = 0
    try:
        Xc = float(TuxV.get())
        Yc = float(TuyV.get())
    except ValueError:
        messagebox.showerror('Ошибка', 'Некорректный ввод центра поворота.')
        code = 1

    try:
        teta = float(TuangV.get())
    except ValueError:
        messagebox.showerror('Ошибка', 'Некорректный ввод угла поворота.')
        code = 1

    if code == 0:
        teta = radians(teta)
        #teta= degrees(teta)
        Back_points.clear()
        Back_points = Points.copy()
        Points.clear()

        for i, element in enumerate(Back_points):
            x = Xc + (element[0] - Xc)*cos(teta) + (element[1] - Yc)*sin(teta)
            y = Yc - (element[0] - Xc)*sin(teta) + (element[1] - Yc)*cos(teta)
            Points.append([x, y])

        Back_square.clear()
        Back_square = Square.copy()
        Square.clear()

        for i, element in enumerate(Back_square):
            x = Xc + (element[0] - Xc) * cos(teta) + (element[1] - Yc) * sin(teta)
            y = Yc - (element[0] - Xc) * sin(teta) + (element[1] - Yc) * cos(teta)

            Square.append([x, y])

        draw()

def Back_ep():
    global Points, Back_points, Square, Back_square

    Points = Back_points.copy()

    Square = Back_square.copy()

    draw()

def Begin_ep():
    global Points, Begin_points, Square, Begin_square

    Points = Begin_points.copy()

    Square = Begin_square.copy()

    draw()




Points = []
Begin_points = []
Back_points = []
Square = []
Back_square = []
Begin_square = []

create()
draw()

TransferButton = Button(Buttons, text='Перенос', font='Verdana 14', command=Transfer_ep, width=8)                    # +
ScaleButton = Button(Buttons, text='Масштаб', font='Verdana 14', command=Scale_ep, width=8)                          # +
TurnButton = Button(Buttons, text='Поворот', font='Verdana 14', command=Turn_ep, width=8)                            # +
BackButton = Button(Buttons, text='Назад', font='Verdana 14', command=Back_ep, width=12, height=1)                   # +
BeginButton = Button(Buttons, text='В начало', font='Verdana 14', command=Begin_ep, width=12, height=1)              # +


Transfer.grid(row=0, column=0, columnspan=2)
TransferButton.grid(row=1, column=0, columnspan=2)
Label(Buttons, text='~~~~~~~~~~~~~~').grid(row=2, column=0, columnspan=4)
Label(Buttons, text='~~~~~~~~~~~~~~').grid(row=3, column=0, columnspan=4)

Scale.grid(row=4, column=0, columnspan=2)
ScaleButton.grid(row=5, column=0, columnspan=2)
Label(Buttons, text='~~~~~~~~~~~~~~').grid(row=6, column=0, columnspan=4)
Label(Buttons, text='~~~~~~~~~~~~~~').grid(row=7, column=0, columnspan=4)

Turn.grid(row=8, column=0, columnspan=2)
TurnButton.grid(row=9, column=0, columnspan=2)
Label(Buttons, text='~~~~~~~~~~~~~~').grid(row=10, column=0, columnspan=4)
Label(Buttons, text='~~~~~~~~~~~~~~').grid(row=11, column=0, columnspan=4)
BackButton.grid(row=12, column=0, columnspan=4)
BeginButton.grid(row=13, column=0, columnspan=4)

Buttons.pack(side='top')
Canv.pack()

root.mainloop()

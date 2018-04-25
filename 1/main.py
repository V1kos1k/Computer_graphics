# На плоскости дано множество точек. Найти такой треугольник с вершинами в этих точках,
# для которого разность количества точек этого множества, попавших внутрь треугольника
# и за его пределы, но врутри описанной окружности, минимальна


from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from math import *
import numpy as np

k = a = b = 0

def Add_a_few():
    AddWin = Tk()
    AddWin.title("Добавление точек")
    AddWin.geometry("400x150+50+50")
    Input = Label(AddWin, text='Введите координаты точки: ')
    Input.grid(row=1,column=0, columnspan=2)
    frameX = Frame(AddWin)
    valueX = Label(frameX, width=1, text='X', anchor='w')
    frameX.grid(row=2,column=0)
    valueX.grid(row=1,column=0)

    frameY = Frame(AddWin)
    valueY = Label(frameY, width=1, text='Y', anchor='w')
    frameY.grid(row=2,column=1)
    valueY.grid(row=1,column=0)

    entryX = Entry(frameX)
    entryY = Entry(frameY)


    win = Tk()
    win.title('Точки')
    win.geometry('485x200+50+250')

    table = ttk.Treeview(win)
    table["columns"] = ("one", "two")
    table.column("one", width=140, stretch=True, anchor='c')
    table.column("two", width=140, stretch=True, anchor='c')
    table.heading("one", text='X', anchor='w')
    table.heading("two", text='Y', anchor='w')
    table.grid()

    def inputX(event):
        valueX.configure(text='X ' + str(eval(entryX.get())))

    entryX.bind("<Return>", inputX)
    entryX.grid()

    def inputY(event):
        valueY.configure(text='Y ' + str(eval(entryY.get())))

    entryY.bind("<Return>", inputY)
    entryY.grid()

    OK = Button(AddWin, text='OK', width=5, height=5)
    cancel = Button(AddWin, text='Закрыть', width=7, height=5)

    global count
    count = 0

    def consent(event):
        global count
        try:
            Points.append([float(eval(entryX.get())), float(eval(entryY.get()))])
            entryX.delete(0, END)
            entryY.delete(0, END)


            for i in range(count, len(Points)):
                table.insert("", 0, text='№'+str(int(i)+1), values=(Points[i][0], Points[i][1]))

            table.grid()
            win.update()
            count += 1
        except:
            messagebox.showinfo('Ошибка', 'Некорректный ввод')

    OK.bind("<Button-1>", consent)
    OK.bind("<Return>", consent)
    OK.grid(row=3,column=0)

    def Cancel(event):
        AddWin.destroy()
        win.destroy()

    cancel.bind("<Button-1>", Cancel)
    cancel.grid(row=3,column=1)
    AddWin.update()

def Delete():
    if len(Points) == 0:
        messagebox.showinfo("Ошибка", "Список точек пуст")
        return
    AddWin = Tk()
    AddWin.title("Удаление точки")
    AddWin.geometry("400x150+50+50")
    Input = Label(AddWin, text='Введите координаты точки: ')

    Input.grid(row=1, column=0, columnspan=2)
    frameX = Frame(AddWin)
    valueX = Label(frameX, width=1, text='X', anchor='w')
    frameX.grid(row=2, column=0)
    valueX.grid(row=1, column=0)

    frameY = Frame(AddWin)
    valueY = Label(frameY, width=1, text='Y', anchor='w')
    frameY.grid(row=2, column=1)
    valueY.grid(row=1, column=0)

    entryX = Entry(frameX)
    entryY = Entry(frameY)

    win = Tk()
    win.title('Точки')
    win.geometry('485x200+50+250')

    table = ttk.Treeview(win)
    table["columns"] = ("one", "two")
    table.column("one", width=140, stretch=True, anchor='c')
    table.column("two", width=140, stretch=True, anchor='c')
    table.heading("one", text='X', anchor='w')
    table.heading("two", text='Y', anchor='w')
    for i in range(len(Points)):
        table.insert("", 0, text='№' + str(int(i) + 1), values=(Points[i][0], Points[i][1]))
    table.grid()

    def inputX(event):
        valueX.configure(text='X ' + str(eval(entryX.get())))

    entryX.bind("<Return>", inputX)
    entryX.grid()

    def inputY(event):
        valueY.configure(text='Y ' + str(eval(entryY.get())))

    entryY.bind("<Return>", inputY)
    entryY.grid()

    OK = Button(AddWin, text='Удалить', width=5, height=5)
    cancel = Button(AddWin, text='Отмена', width=7, height=5)

    def consent(event):
        i = 0
        count = 0
        try:
            while i < len(Points):
                if ((Points[i][0] == eval(entryX.get())) and (Points[i][1] == eval(entryY.get()))):
                    count = 1
                    break
                i += 1
            if count == 0:
                messagebox.showinfo("Ошибка", "Точка не найдена")
                return
            Points.pop(i)
            AddWin.destroy()
            win.destroy()
        except:
            messagebox.showinfo('Ошибка', 'Некорректный ввод')

    OK.bind("<Button-1>", consent)
    OK.bind("<Return>", consent)
    OK.grid(row=3, column=0)

    def Cancel(event):
        AddWin.destroy()
        win.destroy()

    cancel.bind("<Button-1>", Cancel)
    cancel.grid(row=3, column=1)
    AddWin.update()

def Delete_all():
    if len(Points) == 0:
        messagebox.showinfo("Ошибка", "Список точек пуст")
        return
    if (messagebox.askyesno("Удаление точек", "Вы точно хотите удалить все точки?") == True):
        Points.clear()
        Answer.clear()

def Change():
    if len(Points) == 0:
        messagebox.showinfo("Ошибка", "Список точек пуст")
        return
    AddWin = Tk()
    AddWin.title("Изменение координат")
    AddWin.geometry("300x280+50+50")
    Input = Label(AddWin, text='Введите координаты точки: ')
    Input.pack()
    frameX = Frame(AddWin)
    valueX = Label(frameX, width=12, text='X', anchor='w')
    frameX.pack(side=TOP, fill=X, padx=5, pady=5)
    valueX.pack(side='left')

    frameY = Frame(AddWin)
    valueY = Label(frameY, width=12, text='Y', anchor='w')
    frameY.pack(side=TOP, fill=X, padx=5, pady=5)
    valueY.pack(side='left')

    inp = Label(AddWin, text='Введите новые координаты точки')
    inp.pack()

    frameXx = Frame(AddWin)
    valueXx = Label(frameXx, width=12, text='X', anchor='w')
    frameXx.pack(side=TOP, fill=X, padx=5, pady=5)
    valueXx.pack(side='left')

    frameYy = Frame(AddWin)
    valueYy = Label(frameYy, width=12, text='Y', anchor='w')
    frameYy.pack(side=TOP, fill=X, padx=5, pady=5)
    valueYy.pack(side='left')

    entryX = Entry(frameX)
    entryY = Entry(frameY)
    entryXx = Entry(frameXx)
    entryYy = Entry(frameYy)


    win = Tk()
    win.title('Точки')
    win.geometry('485x200+50+350')

    table = ttk.Treeview(win)
    table["columns"] = ("one", "two")
    table.column("one", width=140, stretch=True, anchor='c')
    table.column("two", width=140, stretch=True, anchor='c')
    table.heading("one", text='X', anchor='w')
    table.heading("two", text='Y', anchor='w')

    for i in range(len(Points)):
        table.insert("", 0, text='№' + str(int(i) + 1), values=(Points[i][0], Points[i][1]))
    table.pack()


    def inputX(event):
        valueX.configure(text='X ' + str(eval(entryX.get())))

    entryX.bind("<Return>", inputX)
    entryX.pack()

    def inputY(event):
        valueY.configure(text='Y ' + str(eval(entryY.get())))

    entryY.bind("<Return>", inputY)
    entryY.pack()

    def inputXx(event):
        valueXx.configure(text='X ' + str(eval(entryXx.get())))

    entryXx.bind("<Return>", inputXx)
    entryXx.pack()

    def inputYy(event):
        valueYy.configure(text='Y ' + str(eval(entryYy.get())))

    entryYy.bind("<Return>", inputYy)
    entryYy.pack()

    OK = Button(AddWin, text='Изменить', width=7, height=5)
    cancel = Button(AddWin, text='Отмена', width=7, height=5)

    def consent(event):
        i = 0
        count = 0
        try:
            while i < len(Points):
                if ((Points[i][0] == eval(entryX.get())) and (Points[i][1] == eval(entryY.get()))):
                    count = 1
                    Points[i][0] = float(eval(entryXx.get()))
                    Points[i][1] = float(eval(entryYy.get()))
                    break
                i += 1
            if count == 0:
                messagebox.showinfo("Ошибка", "Точка не найдена")
                return
            AddWin.destroy()
            win.destroy()
        except:
            messagebox.showinfo('Ошибка', 'Некорректный ввод')

    OK.bind("<Button-1>", consent)
    OK.pack(side='left')

    def Cancel(event):
        AddWin.destroy()

    cancel.bind("<Button-1>", Cancel)
    cancel.pack(side='right')
    AddWin.update()

def Table():
    if len(Points) == 0:
        messagebox.showinfo('Ошибка', 'Список точек пуст')
        return

    win = Tk()
    win.title('Таблица')
    win.geometry('485x200+50+250')

    table = ttk.Treeview(win)
    table["columns"] = ("one", "two")
    table.column("one", width=140, stretch=True, anchor='c')
    table.column("two", width=140, stretch=True, anchor='c')
    table.heading("one", text='X', anchor='w')
    table.heading("two", text='Y', anchor='w')

    for i in range(len(Points)):
        table.insert("", 0, text='№' + str(int(i) + 1), values=(Points[i][0], Points[i][1]))

    table.grid()
    win.update()

def Draw():
    if len(Points) < 3:
        messagebox.showinfo("Ошибка", "Слишком мало точек!\nДля построения треугольника, необходимо минимум 3 точки.")
        print("Треугольник может быть построен только из 3х и более точек: 343")
        return

    Find_triangle()
    if len(Answer) < 6:
        messagebox.showinfo("Ошибка", "Все точки лежат на одной прямой.")
        return

    Sketch = Tk()
    Sketch.title("Ответ")
    Sketch.geometry('250x250+50+50')
    text = Text(Sketch, width=100, height=100, font='Times12')
    text.delete('1.0', END)
    text.insert(1.0, "\t      Ответ: \n\n Координата 1-й точки: ({0:.2f};{1:.2f})\n"
                     " Координата 2-й точки: ({2:.2f};{3:.2f})\n"
                     " Координата 3-й точки: ({4:.2f};{5:.2f})\n"
                     " Разность количества точек: {6:d}".format(Answer[0][0], Answer[0][1], Answer[1][0],
                                                                 Answer[1][1], Answer[2][0], Answer[2][1],Answer[5]))
    text.pack()

    global Canv, top
    top = Tk()
    top.title("Рисунок")

    Canv = Canvas(top, bg='White', width=500, height=600)

    if Canv.winfo_height() < top.winfo_height():
        Canv.config(height=top.winfo_height())
    if Canv.winfo_width() < top.winfo_width():
        Canv.config(width=top.winfo_width())

    Canv.delete('all')

    # круг

    # левая координата
    x1 = Answer[3][0] - Answer[4] * 1.40
    y1 = Answer[3][1]

    # нижняя координата
    x2 = Answer[3][0]
    y2 = Answer[3][1] + Answer[4] * 1.40

    # правая координата
    x3 = Answer[3][0] + Answer[4] * 1.40
    y3 = Answer[3][1]

    # верхняя координата
    x4 = Answer[3][0]
    y4 = Answer[3][1] - Answer[4] * 1.40


    minX = min(x1, x2, x3, x4)
    minY = min(y1, y2, y3, y4)

    global k, a, b, Circle

    if minX <= 0:
        a = minX
        x1 -= a
        x2 -= a
        x3 -= a
        x4 -= a

    if minY <= 0:
        b = minY
        y1 -= b
        y2 -= b
        y3 -= b
        y4 -= b

    k = 500 / max(x1, x2, x3, x4)
    if k * max(y1, y2, y3, y4) > 400:
        k = 400 / max(y1, y2, y3, y4)

    for i in range(len(Points)):
        Canv.create_oval([(Points[i][0]-a)*k - 3, 600 - (Points[i][1]-b)*k + 3],
                         [(Points[i][0]-a)*k + 3, 600 - (Points[i][1]-b)*k - 3], fill='blue')
        Canv.create_text((Points[i][0]-a)*k, 600 - (Points[i][1]-b)*k, text=str(Points[i]),
                         font="Verdana 12", anchor="n", justify=LEFT)
    for i in range(3):
        Canv.create_oval([(Answer[i][0] - a) * k - 3, 600 - (Answer[i][1] - b) * k + 3],
                         [(Answer[i][0] - a) * k + 3, 600 - (Answer[i][1] - b) * k - 3], fill='red')

    Canv.create_line((Answer[0][0] - a) * k, 600 - (Answer[0][1] - b) * k,
                     (Answer[1][0] - a) * k, 600 - (Answer[1][1] - b) * k)

    Canv.create_line((Answer[1][0] - a) * k, 600 - (Answer[1][1] - b) * k,
                     (Answer[2][0] - a) * k, 600 - (Answer[2][1] - b) * k)

    Canv.create_line((Answer[2][0] - a) * k, 600 - (Answer[2][1] - b) * k,
                     (Answer[0][0] - a) * k, 600 - (Answer[0][1] - b) * k)

    Circle.clear()
    for t in np.arange(0, 2*pi, 0.1):
        x = Answer[3][0] + Answer[4]*cos(t)
        y = Answer[3][1] + Answer[4]*sin(t)
        Circle.append([(x-a)*k, 600-(y-b)*k])

    Canv.create_polygon(Circle, fill='', outline='green')
    print(len(Circle))

    '''Canv.create_polygon(x1*k, 600-(y1)*k,
                        x2*k, 600-(y2)*k,
                        x3*k, 600-(y3)*k, x4*k, 600-(y4)*k,
                        fill='', outline='green', smooth=1)'''

    Answer.clear()

    Canv.pack()

# поиск треугольника с минимальной разницей
def Find_triangle():
    n = len(Points)
    p1 = []
    p2 = []
    p3 = []
    diff = 1000  # начальная разница
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                tmp = Difference_point(Points[i], Points[j], Points[k])
                if tmp < diff:
                    p1 = Points[i] # +
                    p2 = Points[j] # +
                    p3 = Points[k] # +
                    diff = tmp # +

    if diff == 1000:
        return -1
    Find_center_circle(p1, p2, p3)
    R = Len_segment(p1, Center)
    Answer.append(p1)
    Answer.append(p2)
    Answer.append(p3)
    Answer.append(Center)
    Answer.append(R)
    Answer.append(diff)
    print("OK")
    print("точка 1: ", Answer[0], "\nточка 2: ", Answer[1], "\nточка 3: ", Answer[2],
          "\nразница: ", diff, "\nцентр: ", Center, "\nрадиус: ", R)

# поиск разницы точек внутри треугольника и
# за пределами треугольника внутри описанной окружности
def Difference_point(p1, p2, p3):
    S = Sign_square(p1, p2, p3)
    if compare(S, 0) == 0:
        print("ОШИБКА: 520")
        return 1000                                     # точки лежат на одной прямой, но не все, а те которые проверяют
    Find_center_circle(p1, p2, p3)
    R = Len_segment(p1, Center)
    N1 = Count_point_triangle(p1, p2, p3)
    N2 = Count_point_circle(R)
    in1 = N1
    out1 = N2 - N1 + 3
    return abs(in1 - out1)

# количество точек в окружности (с контуром)
def Count_point_circle(R):
    r = R*R
    Res = 0
    for i in range(len(Points)):
        lenn = (Points[i][0]-Center[0])*(Points[i][0]-Center[0]) + (Points[i][1]-Center[1])*(Points[i][1]-Center[1])
        if compare(lenn, r) <= 0:  # для включения контура
            Res += 1
    return Res

# количество точек в треугольнике (c контуром)
def Count_point_triangle(p1, p2, p3):
    res = 0
    S = fabs(Sign_square(p1, p2, p3))
    for i in range(len(Points)):
        tmp = fabs(Sign_square(p1, p2, Points[i])) + fabs(Sign_square(Points[i], p2, p3))\
              + fabs(Sign_square(p1, Points[i], p3))
        if compare(tmp, S) == 0:
            res += 1
    return res

# доина отрезка
def Len_segment(p1, p2):
    return sqrt((p1[0]-p2[0])*(p1[0]-p2[0]) + (p1[1]-p2[1])*(p1[1]-p2[1]))
    #return sqrt((a-c)**2 + (b-d)**2)

# центр окружности, проходящей через точки 1,2,3
def Find_center_circle(p1, p2, p3):
    """a = p2[0]-p1[0]
    b = p2[1]-p1[1]
    c = p3[0]-p1[0]
    d = p3[1]-p1[1]
    e = a*(p1[0]+p2[0])+b*(p1[1]+p2[1])
    f = c*(p1[0]+p3[0])+d*(p1[1]+p3[1])
    g = 2*(a*(p3[1]-p2[1])-b*(p3[0]-p2[0]))
    if g == 0:
        print('ERROR: 580')
        return -1
    Cx = (d*e-b*f)/g
    Cy = (a*f-c*e)/g
    Center.clear()
    Center.append(Cx)
    Center.append((Cy))
    print("Cx Cy  ", Cx, Cy)"""

    x0 = -1/2*(p1[1]*(p2[0]**2 + p2[1]**2 - p3[0]**2 - p3[1]**2) + p2[1]*(p3[0]**2 + p3[1]**2 - p1[0]**2 - p1[1]**2) +
               p3[1]*(p1[0]**2 + p1[1]**2 - p2[0]**2 - p2[1]**2))/(p1[0]*(p2[1] - p3[1]) + p2[0]*(p3[1] - p1[1]) +
                                                                   p3[0]*(p1[1] - p2[1]))
    y0 = 1/2*(p1[0]*(p2[0]**2 + p2[1]**2 - p3[0]**2 - p3[1]**2) + p2[0]*(p3[0]**2 + p3[1]**2 - p1[0]**2 - p1[1]**2) +
               p3[0]*(p1[0]**2 + p1[1]**2 - p2[0]**2 - p2[1]**2))/(p1[0]*(p2[1] - p3[1]) + p2[0]*(p3[1] - p1[1]) +
                                                                   p3[0]*(p1[1] - p2[1]))
    Center.clear()
    Center.append(x0)
    Center.append(y0)

# знаковая площадь треугольника 123
def Sign_square(p1, p2, p3):
    S =(p2[0]-p1[0])*(p3[1]-p1[1]) - (p3[0]-p1[0])*(p2[1]-p1[1])
    return S/2

def compare(a, b):
    if fabs(a - b) < 0.000001:
        return 0
    if a > b:
        return 1
    return -1

Points = []
Center = []  # центр окружности
Result = []
Answer = [] # конечный результат
Circle = []

root = Tk()
root.title("Информация")
root.geometry('400x300+550+100')
q = Label(root, text="Вариант №13\n\n\nНа плоскости дано множество точек.\n "
                 "Найти такой треугольник с вершинами в этих точках, \n"
                 "для которго разность количеств точек этого множества, \n"
                 " попавших внутрь треугольникаи за его пределы, \n"
                 "но внутри описанной окружности, минимальна.\n\n\nМхитарян В.К.")
q.pack()

m = Menu(root)
root.config(menu=m)

cm = Menu(m)
m.add_cascade(label="Меню", menu=cm)
cm.add_command(label="Добавить точки", command=Add_a_few)   # +
cm.add_command(label="Удалить точку", command=Delete)                 # +
cm.add_command(label="Удалить все точки", command=Delete_all)         # +
cm.add_command(label="Изменить координаты точки", command=Change)     # +
cm.add_command(label="Таблица точек", command=Table)                  # +
cm.add_command(label="Нарисовать", command=Draw)
cm.add_command(label="Выход", command=quit)                           # +


root.mainloop()

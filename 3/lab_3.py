from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QImage, QPen, QColor, QPixmap
from PyQt5.QtCore import Qt
import sys
import time
import numpy as np
import math

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        uic.loadUi('test.ui', self)
        self.scene = QtWidgets.QGraphicsScene(0, 0, 711, 551)
        self.graphicsView.setScene(self.scene)
        self.image = QImage(711, 551, QImage.Format_ARGB32)
        self.pen = QPen()
        self.color_line = QColor(Qt.black)
        self.color_bgfont = QColor(Qt.white)
        #self.image.fill(self.color_bgfont)
        self.LineButton.clicked.connect(lambda: Line_build(self))
        self.RangeButton.clicked.connect(lambda: Range_build(self))
        #self.StepButton.clicked.connect(lambda: Grading_build(self))
        self.CleanButton.clicked.connect(lambda: Delete_all(self))


def sign(x):
    if x == 0:
        return 0
    else:
        return x/abs(x)

def CDA(win, d1, d2):
    deltaX = d1[0] - d2[0]
    deltaY = d1[1] - d2[1]

    # Считаем минимальное количество итераций, необходимое для отрисовки отрезка.
    # Выбирая максимум из длины и высоты линии, обеспечиваем связность линии
    L = max(abs(deltaX), abs(deltaY))

    if L == 0:
        # нужно закрасить один пиксель
        return

    # приращение на каждом шаге по осям
    dX = (d2[0] - d1[0]) / L
    dY = (d2[1] - d1[1]) / L

    # начальные значения
    x = d1[0] + 0.5 * sign(dX)
    y = d1[1] + 0.5 * sign(dY)

    while L > 0:
        # отображение точки
        win.image.setPixel(x, y, win.pen.color().rgb())
        #print(x, y)
        x += dX
        y += dY
        L -= 1

    return

def Bres_int(win, d1, d2):
    if d1 == d2:
        win.image.setPixel(d1[0], d1[1], win.pen.color().rgb())
    else:
        dX = d2[0] - d1[0]
        dY = d2[1] - d1[1]
        SX = sign(dX)
        SY = sign(dY)
        dX = abs(dX)
        dY = abs(dY)
        x = d1[0]
        y = d1[1]

        change = False

        if dX < dY:
            dX, dY = dY, dX
            change = True

        e = 2*dY - dX

        i = 1

        while i <= dX:
            win.image.setPixel(x, y, win.pen.color().rgb())
            #print(x, y)
            if e >= 0:
                if change == False:
                    y += SY
                else:
                    x += SX
                e -= 2*dX
            if e < 0:
                if change == False:
                    x += SX
                else:
                    y += SY
                e += 2*dY

            i += 1

def Bres_float(win, d1, d2):
    if d1 == d2:
        win.image.setPixel(d1[0], d1[1], win.pen.color().rgb())
    else:
        dX = d2[0] - d1[0]
        dY = d2[1] - d1[1]
        SX = sign(dX)
        SY = sign(dY)
        dX = abs(dX)
        dY = abs(dY)
        x = d1[0]
        y = d1[1]

        change = False

        if dX < dY:
            dX, dY = dY, dX
            change = True

        m = dY/dX
        e = m - 0.5

        i = 1

        while i <= dX:
            win.image.setPixel(x, y, win.pen.color().rgb())
            print(x, y)
            if e >= 0:
                if change == False:
                    y += SY
                else:
                    x += SX
                e -= 1
            if e < 0:
                if change == False:
                    x += SX
                else:
                    y += SY
                e += m

            i += 1

def Bres_smooth(win, p1, p2):
    '''if d1 == d2:
        win.image.setPixel(d1[0], d1[1], win.pen.color().rgb())
    else:
        dX = d2[0] - d1[0]
        dY = d2[1] - d1[1]
        SX = sign(dX)
        SY = sign(dY)
        dX = abs(dX)
        dY = abs(dY)
        x = d1[0]
        y = d1[1]

        change = False
        black = False

        try:
            m = dY/dX
        except ZeroDivisionError:
            m = 0

        if win.pen.color() == Qt.black:
            Imax = 256
            black = True
        else:
            Imax = 100

        if dY > dX:
            dX, dY = dY, dX
            change = True
            if m:
                m = 1/m

        m *= Imax
        e = Imax*0.5
        m *= Imax
        w = Imax - m

        i = 1
        while i <= dX:
            if not black:
                new = win.pen.color()
                new.lighter(100+e)
                win.pen.setColor(new)
                win.image.setPixel(x, y, win.pen.color().rgba())
            else:
                new = QColor()
                new.setRgb(0, 0, 0, alpha=255-e)
                win.pen.color(new)
                win.image.setPixel(x, y, win.pen.color().rgba())
            if e >= w:
                x += SX
                y += SY
                e -= w
            else:
                if change:
                    y += SY
                else:
                    x += SX
                e += m
            i += 1'''

    if p1 == p2:
        win.image.setPixel(p1[0], p1[1], win.pen.color().rgb())
        return

    #win.pen.setColor(win.color_line)
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    sx = sign(dx)
    sy = sign(dy)
    dx = abs(dx)
    dy = abs(dy)
    x = p1[0]
    y = p1[1]

    try:
        h = dy / dx
    except ZeroDivisionError:
        h = 0


    isBlack = False

    '''if win.pen.color() == Qt.black:
        i_max = 256
        isBlack = True
        print('true')
    else:'''
    i_max = 100

    change = False

    if dy > dx:
        dx, dy = dy, dx
        change = True
        if h:
            h = 1 / h

    h *= i_max
    e = i_max/2
    w = i_max - h
    i = 1
    while i <= dx:
        if not isBlack:
            new = win.pen.color()
            new.lighter(100 + e)
            win.pen.setColor(new)
            win.image.setPixel(x, y, win.pen.color().rgba())
        else:
            new = QColor()
            new.setRgb(0, 0, 0, alpha=255 - e)
            win.pen.setColor(new)
            win.image.setPixel(x, y, win.pen.color().rgba())
        if e <= w:
            if change:
                y += sy
            else:
                x += sx
            e += h
        else:
            x += sx
            y += sy
            e -= w
        i += 1

def create_color(c):
    if c == 'Черный':
        c = 'black'
    elif c == 'Красный':
        c = 'red'
    elif c == 'Синий':
        c = 'blue'
    elif c == 'Фон':
        c = 'white'
    return c


def Range_build(win):
    Algorithm = str(win.Range_algorithm.currentText())
    Color = str(win.Range_color.currentText())
    Color = create_color(Color)
    c = QColor(Color)
    win.pen.setColor(c)
    #s = QtWidgets.QGraphicsScene(0, 0, 10, 10)
    #s.setBackgroundBrush(c)

    d = win.Range_diam.value()
    step = win.Range_angl.value()

    x1 = 355
    y1 = 255

    ST = False

    begin = time.clock()
    for i in np.arange(0, 360, step):
        x2 = math.cos(math.radians(i))*d + 355
        y2 = math.sin(math.radians(i)) * d + 255

        if Algorithm == 'Стандартный метод':
            ST = True
            win.scene.addLine(x1, y1, x2, y2, win.pen)
        elif Algorithm == 'Метод ЦДА':
            CDA(win, [x1, y1], [x2, y2])
        elif Algorithm == 'Брезенхейм с целыми числами':
            Bres_int(win, [x1, y1], [x2, y2])
        elif Algorithm == 'Брезенхейм с действительными числами':
            Bres_float(win, [x1, y1], [x2, y2])
        elif Algorithm == 'Брезенхейм с устранением ступенчатости':
            Bres_smooth(win, [x1, y1], [x2, y2])
    end = time.clock()

    if not ST:
        #print("=", ST)
        pix = QPixmap(711, 551)
        pix.convertFromImage(win.image)
        win.scene.addPixmap(pix)
    win.label_10.setText("{0:.3f}msc".format((end - begin) * 1000))



def Line_build(win):
    Algorithm = str(win.Line_algorithm.currentText())
    #print(Algorithm)
    Color = str(win.Line_color.currentText())
    Color = create_color(Color)
    #print(Color)
    c = QColor(Color)
    #print(c)
    win.pen.setColor(c)
    s = QtWidgets.QGraphicsScene(0, 0, 10, 10)
    s.setBackgroundBrush(c)
    x1 = win.Line_x1.value()
    y1 = win.Line_y1.value()
    x2 = win.Line_x2.value()
    y2 = win.Line_y2.value()

    ST = False

    if Algorithm == 'Стандартный метод':
        ST = True
        begin = time.clock()
        win.scene.addLine(x1, y1, x2, y2, win.pen)
        end = time.clock()
    elif Algorithm == 'Метод ЦДА':
        begin = time.clock()
        CDA(win, [x1, y1], [x2, y2])
        end = time.clock()
    elif Algorithm == 'Брезенхейм с целыми числами':
        begin = time.clock()
        Bres_int(win, [x1, y1], [x2, y2])
        end = time.clock()
    elif Algorithm == 'Брезенхейм с действительными числами':
        begin = time.clock()
        Bres_float(win, [x1, y1], [x2, y2])
        end = time.clock()
    elif Algorithm == 'Брезенхейм с устранением ступенчатости':
        begin = time.clock()
        Bres_smooth(win, [x1, y1], [x2, y2])
        end = time.clock()

    if not ST:
        #print("=", ST)
        pix = QPixmap(711, 551)
        pix.convertFromImage(win.image)
        win.scene.addPixmap(pix)
    win.label_10.setText("{0:.3f}msc".format((end - begin) * 1000))

def Delete_all(win):
    #win.image.fill(win.color_bgfont)
    win.scene.clear()
    #win.image.fill(win.color_bgfont)
    #win.scene.update()
    win.image = QImage(711, 551, QImage.Format_ARGB32_Premultiplied)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())

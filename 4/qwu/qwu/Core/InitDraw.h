//
//  InitDraw.h
//  qwu
//
//  Created by Виктория on 31.03.2018.
//  Copyright © 2018 ytrewq. All rights reserved.
//

#ifndef InitDraw_h
#define InitDraw_h

#include <stdio.h>
#include <stdbool.h>
#include "CoreGraphics/CoreGraphics.h"

typedef enum Screen {
    CIRCLE_HEIGHT = -574
}Screen;

typedef enum Color {
    WHITE,
    BLACK,
    RED
} COLOR;

typedef struct Rgb {
    CGFloat red;
    CGFloat green;
    CGFloat blue;
} RGB;

typedef enum Metod {
    LIB,
    PARAM,
    CANON,
    BRES,
    DOTS
} METHOD;

typedef enum Object {
    CIRCLE,
    CIRCLE_C,
    ELLIPSE,
    ELLIPSE_C,
    CLEAR,
    NOTHING
} OBJECT;

typedef CGContextRef _context;

RGB set_color(COLOR color);

void Draw_circle(_context context, METHOD method, int x, int y, int radius, COLOR color);
void Draw_circle_c(_context context, METHOD method, int step, int count, COLOR color);

void Draw_ell(_context context, METHOD method, int x, int y, int A, int B, COLOR color);
void Draw_ell_c(_context context, METHOD method, int stepA, int stepB, int count, COLOR color);




#endif /* InitDraw_h */

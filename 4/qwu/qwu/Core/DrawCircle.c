//
//  DrawCircle.c
//  qwu
//
//  Created by Виктория on 03.04.2018.
//  Copyright © 2018 ytrewq. All rights reserved.
//

#include "InitDraw.h"
#include "Methods.h"

void Draw_circle(_context context, METHOD method, int x, int y, int radius, COLOR color) {
    if (method == LIB)
        Lib_circle(context, x, 574-y, radius, color);
    else if (method == PARAM)
        Param_circle(context, x, 574-y, radius, color);
    else if (method == CANON)
        Canon_circle(context, x, 574-y, radius, color);
    else if (method == BRES)
        Bres_circle(context, x, 574-y, radius, color);
    else if (method == DOTS)
        Middle_circle(context, x, 574-y, radius, color);
}

void Draw_circle_c(_context context, METHOD method, int step, int count, COLOR color) {
    int radius = 0;
    int centre = 280;
    for (int i = 0; i < count; i++) {
        radius += step;
        if (method == LIB)
            Lib_circle(context, centre, 574-centre, radius, color);
        else if (method == PARAM)
            Param_circle(context, centre, 574-centre, radius, color);
        else if (method == CANON)
            Canon_circle(context, centre, 574-centre, radius, color);
        else if (method == BRES)
            Bres_circle(context, centre, 574-centre, radius, color);
        else if (method == DOTS)
            Middle_circle(context, centre, 574-centre, radius, color);
    }
}

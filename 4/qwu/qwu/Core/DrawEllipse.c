//
//  DrawEllipse.c
//  qwu
//
//  Created by Виктория on 04.04.2018.
//  Copyright © 2018 ytrewq. All rights reserved.
//

#include "Methods.h"
#include "InitDraw.h"

void Draw_ell(_context context, METHOD method, int x, int y, int A, int B, COLOR color) {
    if (method == LIB)
        Lib_ell(context, x, 574-y, A, B, color);
    else if (method == PARAM)
        Param_ell(context, x, 574-y, A, B, color);
    else if (method == CANON)
        Canon_ell(context, x, 574-y, A, B, color);
    else if (method == BRES)
        Bres_ell(context, x, 574-y, A, B, color);
    else if (method == DOTS)
        Middle_ell(context, x, 574-y, A, B, color);
}

void Draw_ell_c(_context context, METHOD method, int stepA, int stepB, int count, COLOR color) {
    int A = 0, B = 0;
    int centre = 280;
    for (int i = 0; i < count; i++) {
        A += stepA;
        B += stepB;
        if (method == LIB)
            Lib_ell(context, centre, 574-centre, A, B, color);
        if (method == PARAM)
            Param_ell(context, centre, 574-centre, A, B, color);
        if (method == CANON)
            Canon_ell(context, centre, 574-centre, A, B, color);
        if (method == BRES)
            Bres_ell(context, centre, 574-centre, A, B, color);
        if (method == DOTS)
            Middle_ell(context, centre, 574-centre, A, B, color);
    }
}

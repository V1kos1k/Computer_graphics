//
//  Methods.h
//  qwu
//
//  Created by Виктория on 03.04.2018.
//  Copyright © 2018 ytrewq. All rights reserved.
//

#ifndef Methods_h
#define Methods_h

#include "InitDraw.h"

void Lib_circle(_context context, int x, int y, int R, COLOR cir_color);
void Bres_circle(_context context, int xc, int yc, int R, COLOR cir_color);
void Param_circle(_context context, int xc, int yc, int R, COLOR cir_color);
void Canon_circle(_context context, int xc, int yc, int R, COLOR cir_color);
void Middle_circle(_context context, int xc, int yc, int R, COLOR cir_color);

void Lib_ell(_context context, int x, int y, int A, int B, COLOR ell_color);
void Param_ell(_context context, int xc, int yc, int A, int B, COLOR ell_color);
void Canon_ell(_context context, int xc, int yc, int A, int B, COLOR ell_color);
void Bres_ell(_context context, int xc, int yc, int A, int B, COLOR ell_color);
void Middle_ell(_context context, int xc, int yc, int A, int B, COLOR ell_color);

#endif /* Methods_h */

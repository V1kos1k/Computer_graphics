//
//  Methods.c
//  qwu
//
//  Created by Виктория on 03.04.2018.
//  Copyright © 2018 ytrewq. All rights reserved.
//

#include "Methods.h"
#include "InitDraw.h"
#include <math.h>
#include <stdlib.h>
#include <stdio.h>

#define PI 3.14159265358979323846
#define MAX(x, y) ((x) > (y) ? (x) : (y))

void Lib_circle(_context context, int x, int y, int R, COLOR cir_color) {
    RGB color = set_color(cir_color);
    CGContextSetRGBStrokeColor(context, color.red, color.green, color.blue, 1.0);
    CGContextStrokeEllipseInRect(context, CGRectMake(x-R, y-R, 2*R, 2*R));
}

void Lib_ell(_context context, int x, int y, int A, int B, COLOR ell_color) {
    RGB color = set_color(ell_color);
    CGContextSetRGBStrokeColor(context, color.red, color.green, color.blue, 1.0);
    CGContextStrokeEllipseInRect(context, CGRectMake(x-A, y-B, 2*A, 2*B));
}

void Param_circle(_context context, int xc, int yc, int R, COLOR cir_color) {
    double d = ceil(PI*R/2);
    RGB color = set_color(cir_color);
    CGContextSetRGBFillColor(context, color.red, color.green, color.blue, 1.0);
    for (double t = 0; t < d+1; t++) {
        int x = (int)ceil(R*cos(t/R));
        int y = (int)ceil(R*sin(t/R));
        CGContextFillRect(context, CGRectMake(xc+x, yc+y, 1, 1));
        CGContextFillRect(context, CGRectMake(xc+x, yc-y, 1, 1));
        CGContextFillRect(context, CGRectMake(xc-x, yc-y, 1, 1));
        CGContextFillRect(context, CGRectMake(xc-x, yc+y, 1, 1));
    }
}

void Param_ell(_context context, int xc, int yc, int A, int B, COLOR ell_color) {
    int m;
    m = MAX(A,B);
    double d = ceil(PI*m/2);
    RGB color = set_color(ell_color);
    CGContextSetRGBFillColor(context, color.red, color.green, color.blue, 1.0);
    for (double t = 0; t < d+1; t++) {
        int x = (int)ceil(A*cos(t/m));
        int y = (int)ceil(B*sin(t/m));
        CGContextFillRect(context, CGRectMake(xc+x, yc+y, 1, 1));
        CGContextFillRect(context, CGRectMake(xc+x, yc-y, 1, 1));
        CGContextFillRect(context, CGRectMake(xc-x, yc-y, 1, 1));
        CGContextFillRect(context, CGRectMake(xc-x, yc+y, 1, 1));
    }
}


void Canon_circle(_context context, int xc, int yc, int R, COLOR cir_color) {
    RGB color = set_color(cir_color);
    CGContextSetRGBFillColor(context, color.red, color.green, color.blue, 1.0);
    for (int x = 0; x < R+1; x++) {
        int y = ceil(sqrt(R*R - x*x));
        CGContextFillRect(context, CGRectMake(xc+x, yc+y, 1, 1));
        CGContextFillRect(context, CGRectMake(xc+x, yc-y, 1, 1));
        CGContextFillRect(context, CGRectMake(xc-x, yc-y, 1, 1));
        CGContextFillRect(context, CGRectMake(xc-x, yc+y, 1, 1));
    }
    for (int y = 0; y < R+1; y++) {
        int x = ceil(sqrt(R*R - y*y));
        CGContextFillRect(context, CGRectMake(xc+x, yc+y, 1, 1));
        CGContextFillRect(context, CGRectMake(xc+x, yc-y, 1, 1));
        CGContextFillRect(context, CGRectMake(xc-x, yc-y, 1, 1));
        CGContextFillRect(context, CGRectMake(xc-x, yc+y, 1, 1));
    }
}

void Canon_ell(_context context, int xc, int yc, int A, int B, COLOR ell_color) {
    RGB color = set_color(ell_color);
    CGContextSetRGBFillColor(context, color.red, color.green, color.blue, 1.0);
    
    int rx2 = A*A;//a^2
    int ry2 = B*B;//b^2
    
    //Производная при y`=-1 , является границей для оптимального рисования
    //y`=-b/a*x/sqrt(a^2-x^2)
    int rdel2 =(int)ceil(rx2 / sqrt(rx2 + ry2));
    
    int x = 0, y = 0;
    double m = (double)B / A;//b/a
    for (x = 0; x <= rdel2; x++)
    {
        y = (int)ceil(sqrt(rx2 - x * x) * m);  //y=b/a*sqrt(a^2-x^2)
        
        CGContextFillRect(context, CGRectMake(xc+x, yc+y, 1, 1));
        CGContextFillRect(context, CGRectMake(xc+x, yc-y, 1, 1));
        CGContextFillRect(context, CGRectMake(xc-x, yc-y, 1, 1));
        CGContextFillRect(context, CGRectMake(xc-x, yc+y, 1, 1));
    }
    
    //Производная , является границей для оптимального рисования
    rdel2 = (int)ceil(ry2 / sqrt(rx2 + ry2));
    m = 1 / m;//переворачиваем m
    
    for (y = 0; y <= rdel2; y++)
    {
        x = (int)ceil(sqrt(ry2 - y * y) * m);//аналогично выше
        CGContextFillRect(context, CGRectMake(xc+x, yc+y, 1, 1));
        CGContextFillRect(context, CGRectMake(xc+x, yc-y, 1, 1));
        CGContextFillRect(context, CGRectMake(xc-x, yc-y, 1, 1));
        CGContextFillRect(context, CGRectMake(xc-x, yc+y, 1, 1));
    }
}

void Bres_circle(_context context, int xc, int yc, int R, COLOR cir_color) {
    int x = 0;
    int y = R;
    int d = 2 - 2*R; // D(x, y) при (0, R) // первоначальная ошибка
    int d1, d2;
    RGB color = set_color(cir_color);
    CGContextSetRGBFillColor(context, color.red, color.green, color.blue, 1.0);
    while (y >= 0) {
        CGContextFillRect(context, CGRectMake(xc+x, yc+y, 1, 1));
        CGContextFillRect(context, CGRectMake(xc+x, yc-y, 1, 1));
        CGContextFillRect(context, CGRectMake(xc-x, yc-y, 1, 1));
        CGContextFillRect(context, CGRectMake(xc-x, yc+y, 1, 1));
        
        if (d < 0) {  // диагональная точка внутри окружности => ближайшими точками мб только диагональная и правая
            d1 = 2*d + 2*y -1;
            x++;
            if (d1 > 0) {// диагональный шаг
                y--;
                d += 2*(x - y + 1); // новое расстояние до точки по диагонали
            } else  // горизонтальный шаг
                d += 2*x + 1;
        } else if (d == 0){  // диагональный шаг // пиксель лежит на окружности
            x++;
            y--;
            d += 2*(x - y + 1);
        } else { // диагональная точка все окружности
            d2 = 2*d - 2*x - 1;
            if (d2 < 0) { // диагональный шаг
                y --;
                x++;
                d += 2*(x - y + 1);
            } else { // вертикальный
                y--;
                d += -2*y + 1;
            }
        }
    }
}

void Bres_ell(_context context, int xc, int yc, int A, int B, COLOR ell_color) {
    RGB color = set_color(ell_color);
    CGContextSetRGBFillColor(context, color.red, color.green, color.blue, 1.0);
    int x = 0, y = B;
    //f(x,y)=x^2*b^2+a^2y^2-a^2*b^2=0 из каноического
    
    
    //error=b^2*(x+1)^2 + a^2*(y-1)^2-a^2*b^2=
    int d = A*A + B*B - 2*A*A * y;
    int d1, d2;
    
    while (y >= 0)
    {
        CGContextFillRect(context, CGRectMake(xc+x, yc+y, 1, 1));
        CGContextFillRect(context, CGRectMake(xc+x, yc-y, 1, 1));
        CGContextFillRect(context, CGRectMake(xc-x, yc-y, 1, 1));
        CGContextFillRect(context, CGRectMake(xc-x, yc+y, 1, 1));
        
        if (d < 0)//гор и диаг  // внетри эллипса
        {
            d1 = 2 * d + 2*A*A * y - 1;
            if (d1 > 0) //диагональная
            {
                y -= 1;
                x += 1;
                d += 2*B*B * x + B*B + A*A - 2*A*A * y;//b^2 (2x+1)+a^2(1-2y)
            }
            else     //гор
            {
                x += 1;
                d += 2*B*B * x + B*B;    //+b^2 (2x+1)
            }
        }
        else if (d == 0)//диагональная  // на эллипсе
        {
            x += 1;
            y -= 1;
            d += 2*B*B * x + B*B + A*A - 2*A*A * y;
        }
        else  // вне эллипса
        {
            d2 = 2 * d - 2*B*B * x - 1; //2d-b^2x-1
            if (d2 < 0) //диагональная
            {
                y -= 1;
                x += 1;
                d += 2*B*B * x + B*B + B*B - 2*A*A * y;
            }
            else//вертикальная
            {
                y -= 1;
                d += A*A - 2*A*A * y;  //a^2(1-2y)
            }
        }
    }
    
    
}

void Middle_circle(_context context, int xc, int yc, int R, COLOR cir_color) {
    RGB color = set_color(cir_color);
    CGContextSetRGBFillColor(context, color.red, color.green, color.blue, 1.0);
    int x = 0;
    int y = R;
    int p = 1 - R;
    
    while (x < y) {
        CGContextFillRect(context, CGRectMake(xc+x, yc+y, 1, 1));
        CGContextFillRect(context, CGRectMake(xc+x, yc-y, 1, 1));
        CGContextFillRect(context, CGRectMake(xc-x, yc-y, 1, 1));
        CGContextFillRect(context, CGRectMake(xc-x, yc+y, 1, 1));
        
        CGContextFillRect(context, CGRectMake(xc+y, yc+x, 1, 1));
        CGContextFillRect(context, CGRectMake(xc+y, yc-x, 1, 1));
        CGContextFillRect(context, CGRectMake(xc-y, yc-x, 1, 1));
        CGContextFillRect(context, CGRectMake(xc-y, yc+x, 1, 1));
        
        x++;
        
        if (p < 0) // средняя точка внутри окружности // ближе верхняя точка // горизонтальный шаг
            p += 2*x + 1;
        else { // средняя точка все окружности // ближе диагональный пиксель // диагональный шаг
            y--;
            p += 2*(x - y) + 1;
        }
    }
}

void Middle_ell(_context context, int xc, int yc, int A, int B, COLOR ell_color) {
    RGB color = set_color(ell_color);
    CGContextSetRGBFillColor(context, color.red, color.green, color.blue, 1.0);
    int a = A*A;
    int b = B*B;
    int a2 = 2*a;
    int b2 = 2*b;
    int del = (int)(a/sqrt(a + b));  // производная для ограничения
    
    int x = 0;
    int y = B;
    int df = 0;
    int f = (int)(b - a*y + 0.25*a + 0.5);
    int delta = -a2*y;
    
    for (x = 0; x <= del; x++) {
        //printf("\n%d + %d    %d + %d", xc,x, yc,y);
        CGContextFillRect(context, CGRectMake(xc+x, yc+y, 1, 1));
        CGContextFillRect(context, CGRectMake(xc+x, yc-y, 1, 1));
        CGContextFillRect(context, CGRectMake(xc-x, yc-y, 1, 1));
        CGContextFillRect(context, CGRectMake(xc-x, yc+y, 1, 1));
        if (f >= 0) {
            y--;
            delta += a2;
            f += delta;
        }
        df += b2;
        f += df + b;
    }
    delta = b2*x;
    f += (int)(-b*(x + 0.75) - a*(y - 0.75));
    df = -a2*y;
    
    for (; y >= 0; y--) {
        CGContextFillRect(context, CGRectMake(xc+x, yc+y, 1, 1));
        CGContextFillRect(context, CGRectMake(xc+x, yc-y, 1, 1));
        CGContextFillRect(context, CGRectMake(xc-x, yc-y, 1, 1));
        CGContextFillRect(context, CGRectMake(xc-x, yc+y, 1, 1));
        if (f < 0) {
            x++;
            delta += b2;
            f += delta;
        }
        df += a2;
        f += df + a;
    }
}

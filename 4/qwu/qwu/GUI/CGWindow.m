//
//  CGWindow.m
//  qwu
//
//  Created by Виктория on 31.03.2018.
//  Copyright © 2018 ytrewq. All rights reserved.
//

#import "CGWindow.h"

CIR circle_array[100];
CIR_C circle_array_c[150];

ELL ell_array[100];
ELL_C ell_array_c[150];

@implementation CGWindow

- (void)drawRect:(NSRect)dirtyRect {
    [super drawRect:dirtyRect];
    
    CGContextRef context = [[NSGraphicsContext currentContext] graphicsPort];
    
    if (_check == CIRCLE) {
        RGB color = set_color(_background_circle_color);
        CGContextSetRGBFillColor(context, color.red/255, color.green/255, color.blue/255, 1.0);
        CGContextFillRect(context, self.bounds);
        
        if (ell_array->size != 0)
            for (int i = 0; i <= ell_array->size; i++)
                Draw_ell(context, ell_array[i].method, ell_array[i].x, ell_array[i].y, ell_array[i].A, ell_array[i].B, ell_array[i].color);
        
        size_t k = circle_array->size;
        circle_array[k].x = _circle_x;
        circle_array[k].y = _circle_y;
        circle_array[k].radius = _circle_radius;
        circle_array[k].method = _method_circle;
        circle_array[k].color = _circle_color;
        circle_array->size++;
        
        for (int i = 0; i <= k; i++)
            Draw_circle(context, circle_array[i].method, circle_array[i].x, circle_array[i].y, circle_array[i].radius, circle_array[i].color);
    } else if (_check == CIRCLE_C) {
        
        CGContextClearRect(context, self.bounds);
        size_t k = circle_array->size;
        for (int i = 0; i <= k; i++) {
            circle_array[i].x = 0;
            circle_array[i].y = 0;
            circle_array[i].radius = 0;
            circle_array[i].size = 0;
        }
        k = ell_array->size;
        for (int i = 0; i <= k; i++) {
            ell_array[i].x = 0;
            ell_array[i].y = 0;
            ell_array[i].A = 0;
            ell_array[i].B = 0;
            ell_array[i].size = 0;
        }
        
        RGB color = set_color(_background_circle_color);
        CGContextSetRGBFillColor(context, color.red/255, color.green/255, color.blue/255, 1.0);
        CGContextFillRect(context, self.bounds);
        
        k = circle_array_c->size;
        circle_array_c[k].step = _circle_step;
        circle_array_c[k].count = _circle_count;
        circle_array_c[k].method = _method_circle;
        circle_array_c[k].color = _circle_color;
        circle_array_c->size++;
        
        for (int i = 0; i <= k; i++)
            Draw_circle_c(context, circle_array_c[i].method, circle_array_c[i].step, circle_array_c[i].count, circle_array_c[i].color);
    } else if (_check == ELLIPSE) {
        RGB color = set_color(_background_ell_color);
        CGContextSetRGBFillColor(context, color.red/255, color.green/255, color.blue/255, 1.0);
        CGContextFillRect(context, self.bounds);
        
        if (circle_array->size != 0) {
            for (int i = 0; i <= circle_array->size; i++)
                Draw_circle(context, circle_array[i].method, circle_array[i].x, circle_array[i].y, circle_array[i].radius, circle_array[i].color);
        }
        
        size_t k = ell_array->size;
        ell_array[k].x = _ell_x;
        ell_array[k].y = _ell_y;
        ell_array[k].A = _ell_A;
        ell_array[k].B = _ell_B;
        ell_array[k].method = _method_ell;
        ell_array[k].color = _ell_color;
        ell_array->size++;
        
        for (int i = 0; i <= k; i++)
            Draw_ell(context, ell_array[i].method, ell_array[i].x, ell_array[i].y, ell_array[i].A, ell_array[i].B, ell_array[i].color);
    } else if (_check == ELLIPSE_C) {
        CGContextClearRect(context, self.bounds);
        size_t k = circle_array->size;
        for (int i = 0; i <= k; i++) {
            circle_array[i].x = 0;
            circle_array[i].y = 0;
            circle_array[i].radius = 0;
            circle_array[i].size = 0;
        }
        k = ell_array->size;
        for (int i = 0; i <= k; i++) {
            ell_array[i].x = 0;
            ell_array[i].y = 0;
            ell_array[i].A = 0;
            ell_array[i].B = 0;
            ell_array[i].size = 0;
        }
        
        RGB color = set_color(_background_ell_color);
        CGContextSetRGBFillColor(context, color.red/255, color.green/255, color.blue/255, 1.0);
        CGContextFillRect(context, self.bounds);
        
        k = ell_array_c->size;
        ell_array_c[k].stepA = _ell_step_A;
        ell_array_c[k].stepB = _ell_step_B;
        ell_array_c[k].count = _ell_count;
        ell_array_c[k].method = _method_ell;
        ell_array_c[k].color = _ell_color;
        ell_array_c->size++;
        for (int i = 0; i <= k; i++)
            Draw_ell_c(context, ell_array_c[i].method, ell_array_c[i].stepA, ell_array_c[i].stepB, ell_array_c[i].count, ell_array_c[i].color);
    } else if (_check == CLEAR) {
        CGContextClearRect(context, self.bounds);
        size_t k = circle_array->size;
        for (int i = 0; i <= k; i++) {
            circle_array[i].x = 0;
            circle_array[i].y = 0;
            circle_array[i].radius = 0;
            circle_array[i].size = 0;
        }
        
        k = circle_array_c->size;
        for (int i = 0; i <= k; i++) {
            circle_array_c[i].step = 0;
            circle_array_c[i].count = 0;
            circle_array_c[i].size = 0;
        }
        
        k = ell_array->size;
        for (int i = 0; i <= k; i++) {
            ell_array[i].x = 0;
            ell_array[i].y = 0;
            ell_array[i].A = 0;
            ell_array[i].B = 0;
            ell_array[i].size = 0;
        }
        
        k = ell_array_c->size;
        for (int i = 0; i <= k; i++) {
            ell_array_c[i].stepA = 0;
            ell_array_c[i].stepB = 0;
            ell_array_c[i].count = 0;
            ell_array_c[i].size = 0;
        }
    } else if (_check == NOTHING) {}
}

@end


//
//  CGWindow.h
//  qwu
//
//  Created by Виктория on 31.03.2018.
//  Copyright © 2018 ytrewq. All rights reserved.
//

# import<Cocoa/Cocoa.h>
# include "InitDraw.h"

@interface CGWindow : NSView

@property (nonatomic) METHOD method_circle;
@property (nonatomic) METHOD method_ell;

@property (nonatomic) OBJECT check;

@property (nonatomic) COLOR background_circle_color;
@property (nonatomic) COLOR circle_color;
@property (nonatomic) COLOR background_ell_color;
@property (nonatomic) COLOR ell_color;

@property (nonatomic) int circle_x;
@property (nonatomic) int circle_y;
@property (nonatomic) int circle_radius;

@property (nonatomic) int circle_step;
@property (nonatomic) int circle_count;


@property (nonatomic) int ell_x;
@property (nonatomic) int ell_y;
@property (nonatomic) int ell_A;
@property (nonatomic) int ell_B;

@property (nonatomic) int ell_step_A;
@property (nonatomic) int ell_step_B;
@property (nonatomic) int ell_count;

@end

typedef struct circle {
    int x;
    int y;
    int radius;
    METHOD method;
    COLOR color;
    size_t size;
} CIR;

typedef struct circle_c {
    int step;
    int count;
    METHOD method;
    COLOR color;
    size_t size;
} CIR_C;

typedef struct ellipse {
    int x;
    int y;
    int A;
    int B;
    METHOD method;
    COLOR color;
    size_t size;
} ELL;

typedef struct ellipse_c {
    int stepA;
    int stepB;
    int count;
    METHOD method;
    COLOR color;
    size_t size;
} ELL_C;

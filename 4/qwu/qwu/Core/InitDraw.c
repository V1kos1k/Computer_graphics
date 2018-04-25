//
//  InitDraw.c
//  qwu
//
//  Created by Виктория on 31.03.2018.
//  Copyright © 2018 ytrewq. All rights reserved.
//

#include "InitDraw.h"

RGB set_color(COLOR color) {
    RGB rgb_color;
    if (color == WHITE) {
        rgb_color.red = 255;
        rgb_color.green = 255;
        rgb_color.blue = 255;
    } else if (color == RED) {
        rgb_color.red = 255;
        rgb_color.green = 0;
        rgb_color.blue = 0;
    } else {
        rgb_color.red = 0;
        rgb_color.green = 0;
        rgb_color.blue = 0;
    }
    return rgb_color;
}

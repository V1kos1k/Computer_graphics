//
//  CGWindowCallector.m
//  qwu
//
//  Created by Виктория on 31.03.2018.
//  Copyright © 2018 ytrewq. All rights reserved.
//

#import "CGWindowController.h"

@interface CGWindowController ()

@end

@implementation CGWindowController

- (void)viewDidLoad {
    [super viewDidLoad];
    // Method
    self.LineViewWindow.method_circle = LIB;
    self.LineViewWindow.method_ell = LIB;
    //Color
    self.LineViewWindow.background_circle_color = WHITE;
    self.LineViewWindow.circle_color = BLACK;
    self.LineViewWindow.background_ell_color = WHITE;
    self.LineViewWindow.ell_color = BLACK;
    // Circle(x, y, radius)
    self.LineViewWindow.circle_x = 280;
    self.LineViewWindow.circle_y = 280;
    self.LineViewWindow.circle_radius = 100;
    // Concentr(step, count)
    self.LineViewWindow.circle_step = 10;
    self.LineViewWindow.circle_count = 30;
    // Ellipse(x, y, A, B)
    self.LineViewWindow.ell_x = 280;
    self.LineViewWindow.ell_y = 280;
    self.LineViewWindow.ell_A = 100;
    self.LineViewWindow.ell_B = 50;
    self.LineViewWindow.ell_step_A = 10;
    self.LineViewWindow.ell_step_B = 10;
    self.LineViewWindow.ell_count = 30;
    // Состояние
    self.LineViewWindow.check = NOTHING;
}

// Buttons

- (IBAction)DrawCircle:(id)sender {
    self.LineViewWindow.circle_x = [_Circle_x intValue];
    self.LineViewWindow.circle_y = [_Circle_y intValue];
    self.LineViewWindow.circle_radius = [_Circle_radius intValue];
    self.LineViewWindow.check = CIRCLE;
    
    [self.view setNeedsDisplay:YES];
}

- (IBAction)DrawCircleC:(id)sender {
    self.LineViewWindow.circle_step = [_Circle_step intValue];
    self.LineViewWindow.circle_count = [_Circle_count intValue];
    
    self.LineViewWindow.check = CIRCLE_C;
    
    [self.view setNeedsDisplay:YES];
}

- (IBAction)DrawEllipse:(id)sender {
    self.LineViewWindow.ell_x = [_Ell_y intValue];
    self.LineViewWindow.ell_y = [_Ell_y intValue];
    self.LineViewWindow.ell_A = [_Ell_A intValue];
    self.LineViewWindow.ell_B = [_Ell_B intValue];
    
    self.LineViewWindow.check = ELLIPSE;
    
    [self.view setNeedsDisplay:YES];
}

- (IBAction)DrawEllipseC:(id)sender {
    self.LineViewWindow.ell_step_A = [_Ell_stepA intValue];
    self.LineViewWindow.ell_step_B = [_Ell_stepB intValue];
    self.LineViewWindow.ell_count = [_Ell_count intValue];
    
    self.LineViewWindow.check = ELLIPSE_C;
    
    [self.view setNeedsDisplay:YES];
}

- (IBAction)ClearWindow:(id)sender {
    self.LineViewWindow.check = CLEAR;
    [self.view setNeedsDisplay:YES];
}


// Colors CIRCLE

- (IBAction)BackgroundWhiteC:(id)sender {
    self.LineViewWindow.background_circle_color = WHITE;
}

- (IBAction)BackgroundBlackC:(id)sender {
    self.LineViewWindow.background_circle_color = BLACK;
}
- (IBAction)BackgroundRedC:(id)sender {
    self.LineViewWindow.background_circle_color = RED;
}

- (IBAction)ColorBlackC:(id)sender {
    self.LineViewWindow.circle_color = BLACK;
}

- (IBAction)ColorRedC:(id)sender {
    self.LineViewWindow.circle_color = RED;
}

- (IBAction)ColorWhiteC:(id)sender {
    self.LineViewWindow.circle_color = WHITE;
}

// Colors ELLIPSE

- (IBAction)BackgroundWhiteE:(id)sender {
    self.LineViewWindow.background_ell_color = WHITE;
}

- (IBAction)BackgroundBlackE:(id)sender {
    self.LineViewWindow.background_ell_color = BLACK;
}

- (IBAction)BackgroundRedE:(id)sender {
    self.LineViewWindow.background_ell_color = RED;
}

- (IBAction)ColorBlackE:(id)sender {
    self.LineViewWindow.ell_color = BLACK;
}

- (IBAction)ColorRedE:(id)sender {
    self.LineViewWindow.ell_color = RED;
}

- (IBAction)ColorWhiteE:(id)sender {
    self.LineViewWindow.ell_color = WHITE;
}
    


// Methods CIRCLE

- (IBAction)CirLibMethod:(id)sender {
    self.LineViewWindow.method_circle = LIB;
}

- (IBAction)CirParamMethod:(id)sender {
    self.LineViewWindow.method_circle = PARAM;
}

- (IBAction)CirCanonMethod:(id)sender {
    self.LineViewWindow.method_circle = CANON;
}

- (IBAction)CirBresMethod:(id)sender {
    self.LineViewWindow.method_circle = BRES;
}

- (IBAction)CirDotMethod:(id)sender {
    self.LineViewWindow.method_circle = DOTS;
}

// Method ELLIPSE

- (IBAction)EllLibMethod:(id)sender {
    self.LineViewWindow.method_ell = LIB;
}

- (IBAction)EllParamMethod:(id)sender {
    self.LineViewWindow.method_ell = PARAM;
}

- (IBAction)EllCanonMethod:(id)sender {
    self.LineViewWindow.method_ell = CANON;
}

- (IBAction)EllBresMethod:(id)sender {
    self.LineViewWindow.method_ell = BRES;
}

- (IBAction)EllDotMethod:(id)sender {
    self.LineViewWindow.method_ell = DOTS;
}

@end

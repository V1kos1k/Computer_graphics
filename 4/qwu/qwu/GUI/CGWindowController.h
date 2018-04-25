//
// CGWindowCallector.h
//  qwu
//
//  Created by Виктория on 31.03.2018.
//  Copyright © 2018 ytrewq. All rights reserved.
//

#import <Cocoa/Cocoa.h>
#import "CGWindow.h"

@interface CGWindowController : NSViewController

@property (nonatomic, strong) IBOutlet CGWindow *LineViewWindow;
@property (nonatomic, weak) IBOutlet NSTextField *Circle_x;

@property (nonatomic, weak) IBOutlet NSTextField *Circle_y;

@property (nonatomic, weak) IBOutlet NSTextField *Circle_radius;

@property (nonatomic, weak) IBOutlet NSTextField *Circle_step;

@property (nonatomic, weak) IBOutlet NSTextField *Circle_count;

@property (nonatomic, weak) IBOutlet NSTextField *Ell_x;

@property (nonatomic, weak) IBOutlet NSTextField *Ell_y;

@property (nonatomic, weak) IBOutlet NSTextField *Ell_A;

@property (nonatomic, weak) IBOutlet NSTextField *Ell_B;

@property (nonatomic, weak) IBOutlet NSTextField *Ell_stepA;

@property (nonatomic, weak) IBOutlet NSTextField *Ell_stepB;

@property (nonatomic, weak) IBOutlet NSTextField *Ell_count;

@end

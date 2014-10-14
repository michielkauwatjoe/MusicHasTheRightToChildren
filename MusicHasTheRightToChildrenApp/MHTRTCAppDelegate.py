#-*- coding: utf-8 -*-
#
#  MusicHasTheRightToChildrenAppAppDelegate.py
#  MusicHasTheRightToChildrenApp
#
#  Created by Michiel on 19/05/14.
#  Copyright (c) 2014 Factful. All rights reserved.
#

from Foundation import *
from AppKit import *
from musichastherighttochildren.extract import Extract

class MHTRTCAppDelegate(NSObject):
    u"""
    Application delegate called by run event loop.
    Model should be delegated from here.
    """

    def applicationDidFinishLaunching_(self, sender):
        NSLog("Application did finish launching.")
        e = Extract()

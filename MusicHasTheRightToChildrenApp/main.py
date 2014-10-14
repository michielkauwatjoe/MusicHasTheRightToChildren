#-*- coding: utf-8 -*-
#
#  main.py
#  MusicHasTheRightToChildrenApp
#
#  Created by Michiel on 19/05/14.
#  Copyright (c) 2014+ Factful. All rights reserved.
#

# Import modules required by application.
import objc
import Foundation
import AppKit

from PyObjCTools import AppHelper

# import modules containing classes required to start application and load MainMenu.nib
import MHTRTCAppDelegate

# pass control to AppKit
AppHelper.runEventLoop()

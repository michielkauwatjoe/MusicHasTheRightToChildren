#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# https://github.com/michielkauwatjoe/MusicHasTheRightToChildren

import os
from musichastherighttochildren.mhtrtcglobals import MHTRTCGlobals

class FolderScanner(MHTRTCGlobals):
    u"""
    Compares folder structure of iTunes collection to backup repository.
    """

    def __init__(self):
        pass


    def main(self):
        print self.COLLECTION
        for root, dirs, files in os.walk(self.COLLECTION):
            print root, dirs, files

if __name__ == '__main__':
    scanner = FolderScanner()
    scanner.main()

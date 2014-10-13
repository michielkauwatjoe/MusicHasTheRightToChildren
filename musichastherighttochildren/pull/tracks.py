#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# https://github.com/michielkauwatjoe/MusicHasTheRightToChildren

from os import listdir
from musichastherighttochildren.mhtrtcglobals import MHTRTCGlobals
from musichastherighttochildren.aux.shell import Shell

class Tracks(MHTRTCGlobals):
    u"""
    Checks folder integrity for given path.
    """

    def __init__(self, path):
        self.path = self.COLLECTION + path
        self.tracks = {}
        self.load()

    def load(self):
        Shell.printAlbum(self.path)
        for track in listdir(self.path):
            print track

if __name__ == '__main__':
    tracks = Tracks()

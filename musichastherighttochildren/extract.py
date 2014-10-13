#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# https://github.com/michielkauwatjoe/MusicHasTheRightToChildren

from mhtrtcglobals import MHTRTCGlobals
from pull.albums import Albums
from pull.tracks import Tracks
from musichastherighttochildren.aux.shell import Shell

class Extract(MHTRTCGlobals):

    MAX = 8

    def __init__(self):
        Shell.initColorama()
        self.albums = Albums()
        i = 0

        for path in sorted(self.albums.asPaths()):
            if i > self.MAX:
                break
            i += 1
            tracks = Tracks(path)

    def cacheArtwork(self):
        u"""
        Extract artwork from local files or else from the web.
        """
        pass

    def toJSON(self):
        u"""
        Store as JSON dictionary for D3JS visualization.
        """
        pass

if __name__ == '__main__':
    e = Extract()

    # Testing.
    '''
    for artist, albums in e.albums.asDict().items():
        Shell.printArtist(artist)
    for a in sorted(e.albums.asPaths()):
        print a
    '''

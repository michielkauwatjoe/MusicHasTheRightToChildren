#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# https://github.com/michielkauwatjoe/MusicHasTheRightToChildren

from mhtrtcglobals import MHTRTCGlobals
from retrieval.collection import Collection
from retrieval.tracks import Tracks
from musichastherighttochildren.aux.shell import Shell
from settings.settings import Settings

class Extract(MHTRTCGlobals):

    MAX = 8

    def __init__(self):
        Shell.initColorama()
        settings = Settings()
        self.collection = Collection(settings.COLLECTION)
        i = 0

        for path in sorted(self.collection.asPaths()):
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

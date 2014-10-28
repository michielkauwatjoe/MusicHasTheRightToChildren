#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# https://github.com/michielkauwatjoe/MusicHasTheRightToChildren

from mhtrtc import MHTRTC
from retrieval.collection import Collection
from retrieval.tracks import Tracks

class Extract(MHTRTC):

    MAX = 8

    def __init__(self):
        super(Extract, self).__init__()
        self.collection = Collection(self.settings.COLLECTION)
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

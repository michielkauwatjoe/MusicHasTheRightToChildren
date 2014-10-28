#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# https://github.com/michielkauwatjoe/MusicHasTheRightToChildren

from mhtrtcglobals import MHTRTCGlobals
from pull.albums import Albums
from pull.tracks import Tracks
from pull.itunes import iTunes
from aux.shell import Shell
from settings.settings import Settings

class Backups(MHTRTCGlobals):

    MAX = 8

    def __init__(self):
        # TODO: move init to super, remove Globals from base name.
        self.settings = Settings()
        Shell.initColorama()
        self.albums = Albums(self.settings.BACKUP)

        '''
        i = 0

        for path in sorted(self.albums.asPaths()):
            if i > self.MAX:
                break
            i += 1
            tracks = Tracks(path)
        '''

if __name__ == '__main__':
    b = Backups()

    # Testing.
    '''
    for artist, albums in e.albums.asDict().items():
        Shell.printArtist(artist)
    for a in sorted(e.albums.asPaths()):
        print a
    '''

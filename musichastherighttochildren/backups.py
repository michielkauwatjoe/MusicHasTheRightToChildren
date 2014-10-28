#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# https://github.com/michielkauwatjoe/MusicHasTheRightToChildren

from mhtrtcglobals import MHTRTCGlobals
from pull.albums import Albums
from pull.itunes import iTunes
from aux.shell import Shell
from settings.settings import Settings

class Backups(MHTRTCGlobals):

    MAX = 8

    def __init__(self):
        # TODO: move init to super, remove Globals from base name.
        self.settings = Settings()
        Shell.initColorama()
        itunes = iTunes(self.settings.BACKUP_LIBRARY)
        collection = Albums(self.settings.BACKUP, verbose=True)

        for artist, albums in collection.asDict().items():
            if artist not in itunes.asDict():
                print 'Missing artist %s' % artist
            else:
                for album in albums:
                    if album not in itunes.asDict()[artist]:
                        print 'Missing album %s for artist %s' % (album, artist)

if __name__ == '__main__':
    b = Backups()

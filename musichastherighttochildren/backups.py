#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# https://github.com/michielkauwatjoe/MusicHasTheRightToChildren
import os, json

from mhtrtc import MHTRTC
from retrieval.collection import Collection
from retrieval.itunes import iTunes
from aux.shell import Shell
from settings.settings import Settings

class Backups(MHTRTC):

    MAX = 8
    ITUNES_JSON = 'data/itunes.json'
    COLLECTION_JSON = 'data/collection.json'

    def __init__(self):
        u"""
        """
        super(Backups, self).__init__()
        itunes = self.getITunes()
        print itunes
        #itunes = iTunes(self.settings.BACKUP_LIBRARY)
        #collection = Collection(self.settings.BACKUP, verbose=True)

    def compare(self, collection, itunes):
        for artist, albums in collection.asDict().items():
            if artist not in itunes.asDict():
                print 'Missing artist %s' % artist
            else:
                for album in albums:
                    if album not in itunes.asDict()[artist]:
                        print 'Missing album %s for artist %s' % (album, artist)

    def getITunes(self):
        if not os.path.exists(self.ITUNES_JSON):
            itunes = iTunes(self.settings.BACKUP_LIBRARY)
            self.writeJSON(self.ITUNES_JSON, itunes.asDict())
        else:
            itunes = self.readJSON(self.ITUNES_JSON)
        return itunes

if __name__ == '__main__':
    b = Backups()

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

    def walk(self, path):
        collection = {}

        for artist, albums, _ in os.walk(path):
            if artist == self.COLLECTION:
                # Skips base folder.
                continue
            if len(albums) > 0:
                collection[self.stripArtist(artist)] = albums

        return collection

    def stripArtist(self, artist):
        return artist.replace(self.COLLECTION, '')

    def backupPath(self, artist, album):
        return self.BACKUP + artist + '/' + album

    def backedUp(self, path):
        if os.path.exists(path):
            return True
        return False

    def main(self):
        if not os.path.exists(self.BACKUP):
            print 'Backup path %s does not exist, you might need to mount the harddrive.' % self.BACKUP
            return

        itunes = self.walk(self.COLLECTION)

        for artist, albums in itunes.items():
            for album in albums:
                path = self.backupPath(artist, album)
                if not self.backedUp(path):
                    print 'Please back up %s' % path

if __name__ == '__main__':
    scanner = FolderScanner()
    scanner.main()

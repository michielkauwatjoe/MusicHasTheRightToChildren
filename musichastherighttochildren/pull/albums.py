#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# https://github.com/michielkauwatjoe/MusicHasTheRightToChildren

import os
from colorama import init as colorinit
from musichastherighttochildren.mhtrtcglobals import MHTRTCGlobals
from musichastherighttochildren.aux.shell import Shell

class Albums(MHTRTCGlobals):
    u"""
    Collects all album titles and stores them under the (sort) artist name.
    Optionally compares folder structure of iTunes collection to backup repository.
    """

    def __init__(self, check=False, verbose=False):
        u"""
        """
        colorinit(autoreset=True)
        self.collection = {}
        self.load()

        if check:
            self.checkBackedUp()

        if verbose:
            self.printVerbose()

    def asDict(self):
        return self.collection

    def asPaths(self):
        u"""
        Returns relative paths for artist-album combinations.
        """
        l = []
        for artist, albums in self.collection.items():
            for album in albums:
                l.append(artist + '/' + album)
        return l

    def printVerbose(self):
        for artist in sorted(self.collection.keys()):
            Shell.printArtist(artist)
            for album in sorted(self.collection[artist]):
                Shell.printAlbum(album)

    def walk(self, path):

        for artist, albums, _ in os.walk(path):
            if artist == self.COLLECTION:
                # Skips base folder.
                continue
            if len(albums) > 0:
                self.collection[self.stripArtist(artist)] = albums

    def stripArtist(self, artist):
        return artist.replace(self.COLLECTION, '')

    def backupPath(self, artist, album):
        return self.BACKUP + artist + '/' + album

    def backedUp(self, path):
        if os.path.exists(path):
            return True
        return False

    def load(self):
        if not os.path.exists(self.BACKUP):
            print 'Backup path %s does not exist, you might need to mount the harddrive.' % self.BACKUP
            return
        self.walk(self.COLLECTION)

    def checkBackedUp(self):
        for artist, albums in self.collection.items():
            for album in albums:
                path = self.backupPath(artist, album)
                if not self.backedUp(path):
                    print 'Please back up %s' % path

if __name__ == '__main__':
    albums = Albums(check=True, verbose=True)


#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# https://github.com/michielkauwatjoe/MusicHasTheRightToChildren

import os
from colorama import init as colorinit
from musichastherighttochildren.aux.shell import Shell
from musichastherighttochildren.settings.settings import Settings

class Collection(object):
    u"""
    Collects all album titles and stores them under the (sort) artist name.
    Optionally compares folder structure of iTunes collection to backup repository.
    """
    def __init__(self, parent, root, check=False, verbose=False):
        u"""
        """
        self.root = root
        colorinit(autoreset=True)
        self.collection = {}
        self.load()

        '''
        # TODO: move outside object, compare two Albums objects, one for
        # local, one for remote respectively.
        if check:
            self.checkBackedUp()
        '''

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
        u"""
        Walks through collection folder to build artist-album dictionary.
        """
        max_count = 32
        count = 0
        total_count = 0

        for artist, albums, _ in os.walk(path):
            if count > max_count:
                print 'Scanned %d folders' % total_count
                total_count += max_count
                count = 0
            if artist == self.root:
                # Skips base folder.
                continue
            if len(albums) > 0:
                self.collection[self.stripArtist(artist)] = albums
            count += 1

    def stripArtist(self, artist):
        return artist.replace(self.root, '')

    def load(self):
        self.walk(self.root)

    '''
    #if not os.path.exists(self.BACKUP):
    #    print 'Backup path %s does not exist, you might need to mount the harddrive.' % self.BACKUP
    #        return
    # TODO: convert to compare.
    def checkBackedUp(self):
        for artist, albums in self.collection.items():
            for album in albums:
                path = self.backupPath(artist, album)
                if not self.backedUp(path):
                    print 'Please back up %s' % path

    def backupPath(self, artist, album):
        return self.BACKUP + artist + '/' + album

    def backedUp(self, path):
        if os.path.exists(path):
            return True
        return False
    '''

if __name__ == '__main__':
    settings = Settings()
    Collection(settings.COLLECTION, check=True, verbose=True)


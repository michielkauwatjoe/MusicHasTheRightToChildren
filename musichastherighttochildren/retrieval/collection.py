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
    File-based collection representation. Collects all album titles and stores
    them under the (sort) artist name. Assumes Root - Artist - Album structure.
    """

    def __init__(self, root, check=False, verbose=False):
        u"""
        """
        self.root = root
        colorinit(autoreset=True)
        self.collection = {}
        self.load()

        if verbose:
            self.printVerbose()

    def asDict(self):
        u"""
        Returns dictionary contents only.
        """
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

        for artist in os.listdir(path):
            albums = []

            if artist.startswith('.'):
                continue

            # Feedback while scanning, could be a lot of folders.
            if count > max_count:
                print 'Scanned %d folders' % total_count
                total_count += max_count
                count = 0

            for album in os.listdir(path + '/' + artist):
                albums.append(album)

            if len(albums) > 0:
                self.collection[artist] = albums

            count += 1

    def load(self):
        self.walk(self.root)

if __name__ == '__main__':
    settings = Settings()
    Collection(settings.COLLECTION, check=True, verbose=True)

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
            if len(albums) > 0:
                print self.stripArtist(artist), albums


    def stripArtist(self, artist):
        return artist.replace(self.COLLECTION, '')

    def main(self):
        itunes = self.walk(self.COLLECTION)

if __name__ == '__main__':
    scanner = FolderScanner()
    scanner.main()

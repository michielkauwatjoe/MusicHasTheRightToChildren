#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# https://github.com/michielkauwatjoe/MusicHasTheRightToChildren

import os
from musichastherighttochildren.mhtrtcglobals import MHTRTCGlobals

class FileScanner(MHTRTCGlobals):
    u"""
    Checks folder integrity for given path.
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

    def main(self):
        itunes = self.walk(self.COLLECTION)
        print itunes

if __name__ == '__main__':
    scanner = FileScanner()
    scanner.main()

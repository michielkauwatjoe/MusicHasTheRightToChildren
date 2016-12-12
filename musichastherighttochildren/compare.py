#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# https://github.com/michielkauwatjoe/MusicHasTheRightToChildren
import difflib

from mhtrtc import MHTRTC
from aux.shell import Shell

class Compare(MHTRTC):
    u"""
    Compares local iTunes library to remote network library.
    """

    MAX = 8

    def __init__(self, verbose=False, log=True):
        u"""
        Holds local iTunes collection to library on network.
        """
        super(Compare, self).__init__()
        self.verbose = verbose
        itunes = self.getITunes()
        collection = self.getCollection()
        self.compareCollection(collection, itunes)

    def compareCollection(self, collection, itunes):
        for artist, albums1 in collection.items():
            artist = self.compareArtists(artist, itunes.keys())

            if not artist is None:
                albums2 = itunes[artist]

                if self.verbose:
                    self.printCompare(artist, albums1, albums2)

                self.compareAlbums(artist, albums1, albums2)
                self.compareAlbums(artist, albums2, albums1)

    def printCompare(self, artist, albums1, albums2):
        print sorted(albums1)
        print sorted(albums2.keys())

    def compareArtists(self, artist, artists):
        u"""
        """
        if artist in artists:
            return artist

        artist = artist.replace('_', '/')
        if artist in artists:
            return artist


        matches = difflib.get_close_matches(artist, artists, 3, 0.75)

        if len(matches) >= 1:
            #d = difflib.Differ()
            #diff = d.compare(artist, matches)
            #print ''.join(diff)
            match = (', '.join(matches))
            Shell.printArtist(u'Found match(es) for artist')
            Shell.printArtist(u' * %s' % artist)
            Shell.printArtist(u' * %s' % match)
            artist = matches[0]
            return artist

        Shell.printArtist('Missing artist %s' % artist)

    def compareAlbums(self, artist, albums1, albums2):
        u"""
        TODO: also check album artist.
        """
        found = False

        for album in albums1:
            if album in albums2:
                found = True

            if not found:
                slash_album = album.replace('_', '/')
                if slash_album in albums2:
                    found = True

            if not found:
                matches = difflib.get_close_matches(album, albums2)
                if len(matches) > 0:
                    #print 'Found match(es) for %s:' % album, ', '.join(matches)
                    found = True

        if not found:
            Shell.printAlbum('Missing album %s for artist %s' % (album, artist))

if __name__ == '__main__':
    Compare()

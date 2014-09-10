#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# https://github.com/michielkauwatjoe/MusicHasTheRightToChildren
import sys
import os
import Foundation

from musichastherighttochildren.mhtrtcglobals import MHTRTCGlobals

class iTunesScanner(MHTRTCGlobals):
    u"""
    PyObjc solution for access to the iTunes library.
    """

    def scan(self, library_file=None):
        u"""
        """
        libfile = library_file or self.LIBRARY

        # Load iTunes library
        db = Foundation.NSDictionary.dictionaryWithContentsOfFile_(libfile)

        self.checkFilesExist(db)

    def checkFilesExist(self, db):
        # Check track info.
        for track in db[u'Tracks'].itervalues():
            print track

            if u'Location' not in track:
                print 'No location info in track info', track
                continue

            # Resolve location
            nsurl = Foundation.NSURL.URLWithString_(track[u'Location'])

            # Check local file paths
            if nsurl.scheme() == u'file' and nsurl.host() == u'localhost':
                if not os.path.exists(nsurl.path()):
                    print "Location does not exist:", nsurl.path(), 'from track', track
            else:
                print "Don't know how to check", nsurl

if __name__ == '__main__':
    scanner = iTunesScanner()
    scanner.scan()

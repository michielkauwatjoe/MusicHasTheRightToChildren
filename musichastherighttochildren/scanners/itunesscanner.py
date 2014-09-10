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
        Loads iTunes library.
        Database keys:

        "Library Persistent ID",
        Tracks,
        "Minor Version",
        Date,
        Features,
        Playlists,
        "Major Version",
        "Show Content Ratings",
        "Application Version",
        "Music Folder"
        """
        libfile = library_file or self.LIBRARY
        self.db = Foundation.NSDictionary.dictionaryWithContentsOfFile_(libfile)
        self.tracks = self.db['Tracks'] # objective-c class __NSCFDictionary
        self.titleindex = {}
        self.buildTitleIndex()
        self.checkFilesExist()

    def buildTitleIndex(self):
        """

        Example track values:

        Album = "Footwork EP";
        "Album Artist" = "Jamie Grind";
        Artist = "Jamie Grind";
        "Artwork Count" = 1;
        "Bit Rate" = 320;
        "Date Added" = "2014-05-16 12:14:37 +0000";
        "Date Modified" = "2011-01-17 13:55:31 +0000";
        "Disc Count" = 1;
        "Disc Number" = 1;
        "File Folder Count" = 5;
        Genre = Electronic;
        Kind = "MPEG audio file";
        "Library Folder Count" = 1;
        Location = "file://localhost/Users/michiel/Music/iTunes/iTunes%20Media/Music/Jamie%20Grind/Footwork%20EP/01%20Footwork.mp3";
        Name = Footwork;
        "Persistent ID" = 5FE4748CF01018FD;
        "Sample Rate" = 44100;
        Size = 12740768;
        "Total Time" = 314148;
        "Track Count" = 4;
        "Track ID" = 2974;
        "Track Number" = 1;
        "Track Type" = File;
        Year = 2011;
        """
        for track in self.tracks.itervalues():
            tid = track['Track ID']

            if 'Album Artist' in track:
                artist = track['Album Artist']
            elif 'Artist' in track:
                artist = track['Artist']
            else:
                print 'Unknown artist for track ID %d' % tid
                continue

            album = track['Album']
            title = track['Name']

            if 'Track Number' in track:
                nr = track['Track Number']
            else:
                print 'Unknown number for track %d (ID), %s' % (tid, title)
                continue

            if 'Disc Number' in track:
                disc = track['Disc Number']
            else:
                print 'Unknown number for track %d (ID), %s' % (tid, title)
                disc = 1
                print 'Assuming disc number is %d' % disc

            if artist not in self.titleindex:
                self.titleindex[artist] = {}

            if album not in self.titleindex[artist]:
                self.titleindex[artist][album] = {}

            if disc not in self.titleindex[artist][album]:
                self.titleindex[artist][album][disc] = {}

            self.titleindex[artist][album][disc][nr] = {'title': title, 'tid': tid}

        print self.titleindex.items()

    def checkFilesExist(self):
        # Check track info.
        for track in self.tracks.itervalues():

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

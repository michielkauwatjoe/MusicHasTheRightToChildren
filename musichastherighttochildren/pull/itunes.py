#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# https://github.com/michielkauwatjoe/MusicHasTheRightToChildren
import sys
import os
import Foundation
from colorama import init as colorinit
from colorama import Fore, Back, Style

'''
Colorama options:

Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Style: DIM, NORMAL, BRIGHT, RESET_ALL
'''

from musichastherighttochildren.mhtrtcglobals import MHTRTCGlobals

class iTunes(MHTRTCGlobals):
    u"""
    PyObjc solution for access to the iTunes library.
    """

    def __init__(self):
        colorinit(autoreset=True)

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
            compilation = False
            artist = None

            if 'Artist' in track:
                artist = track['Artist']

            if 'Compilation' in track and track['Compilation'] == 1:
                albumartist = 'Compilation'
                compilation = True
            elif 'Album Artist' in track:
                albumartist = track['Album Artist']
            elif artist:
                albumartist = artist
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
                disc = 1
                #print 'Unknown number for track %d (ID), %s' % (tid, title)
                #print 'Assuming disc number is %d' % disc

            if artist not in self.titleindex:
                self.titleindex[artist] = {}

            if album not in self.titleindex[artist]:
                self.titleindex[artist][album] = {}

            if disc not in self.titleindex[artist][album]:
                self.titleindex[artist][album][disc] = {}

            if not compilation:
                self.titleindex[artist][album][disc][nr] = {'title': title, 'tid': tid}
            else:
                self.titleindex[artist][album][disc][nr] = {'title': title, 'tid': tid, 'artist': artist}

        self.printVerbose()

    def printVerbose(self):
        u"""
        Nested text output.
        TODO: HTML output.
        """
        for artist, albums in self.titleindex.items():
            print Fore.BLUE + Back.RED + 'Artist: %s' % artist
            if isinstance(albums, dict):
                for album, discs in albums.items():
                    print Fore.BLACK + Back.BLUE + Style.DIM + 'Album: %s' % album
                    if isinstance(discs, dict):
                        for discnr, disc in discs.items():
                            print Fore.BLACK + Back.YELLOW + 'Disc #%s' % discnr
                            for tracknr, track in disc.items():
                                print Fore.WHITE + Back.YELLOW + 'Track 0%s-%s - %s' % (discnr, tracknr, track['title'])

                    '''
                    if isinstance(v, dict):
                        for track, v in value.items():
                        print '  -> Track: %s' % k
                    '''

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
    itunes = iTunes()
    itunes.scan()

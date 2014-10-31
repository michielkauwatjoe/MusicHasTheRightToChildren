#!/usr/bin/env python # -*- coding: utf-8 -*- #
# https://github.com/michielkauwatjoe/MusicHasTheRightToChildren

import sys
import os
import Foundation
from colorama import init as colorinit

from musichastherighttochildren.aux.shell import Shell
from musichastherighttochildren.mhtrtc import MHTRTC
from musichastherighttochildren.settings.settings import Settings

class iTunes(MHTRTC):
    u"""
    PyObjc solution for access to the iTunes library.
    """

    def __init__(self, library_file):
        self.settings = Settings()
        colorinit(autoreset=True)
        self.titleindex = {}
        self.db = Foundation.NSDictionary.dictionaryWithContentsOfFile_(library_file)
        self.scan(library_file)

    def asDict(self):
        return self.titleindex

    def scan(self, library_file, checkfiles=False, checkxml=False, verbose=False):
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
        self.tracks = self.db['Tracks'] # objective-c class __NSCFDictionary
        self.buildTitleIndex()

        if verbose is True:
            self.printVerbose()

        print sorted(self.titleindex.keys())

        if checkfiles:
            self.checkFilesExist()

        if checkxml:
            self.checkXML()

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
                artist = track['Artist'].encode('utf-8')

            if 'Compilation' in track and track['Compilation'] == 1:
                albumartist = 'Compilation'
                compilation = True
            elif 'Album Artist' in track:
                albumartist = track['Album Artist'].encode('utf-8')
            elif artist:
                albumartist = artist
            else:
                print 'Unknown artist for track ID %d' % tid
                continue

            try:
                album = track['Album'].encode('utf-8')
            except Exception, e:
                print track['Location']
                print track['Kind']
                continue

            title = track['Name'].encode('utf-8')

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

            if albumartist not in self.titleindex:
                self.titleindex[albumartist] = {}

            if album not in self.titleindex[albumartist]:
                self.titleindex[albumartist][album] = {}

            if disc not in self.titleindex[albumartist][album]:
                self.titleindex[albumartist][album][disc] = {}

            if not compilation:
                self.titleindex[albumartist][album][disc][nr] = {'title': title, 'tid': tid}
            else:
                self.titleindex[albumartist][album][disc][nr] = {'title': title, 'tid': tid, 'artist': artist}

    def printVerbose(self):
        u"""
        Nested text output.
        TODO: HTML output.
        """
        for artist, albums in self.titleindex.items():
            Shell.printArtist(artist)
            if isinstance(albums, dict):
                for album, discs in albums.items():
                    Shell.printAlbum(album)
                    if isinstance(discs, dict):
                        for discnr, disc in discs.items():
                            Shell.printDiscNr(discnr)
                            for tracknr, track in disc.items():
                                Shell.printTrack(discnr, tracknr, track['title'])

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
    settings = Settings()
    itunes = iTunes(settings.LIBRARY)
    itunes = iTunes(settings.BACKUP_LIBRARY)

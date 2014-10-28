#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# https://github.com/michielkauwatjoe/MusicHasTheRightToChildren

from os import listdir
from musichastherighttochildren.mhtrtcglobals import MHTRTCGlobals
from musichastherighttochildren.aux.shell import Shell
from musichastherighttochildren.formats.mp3 import EmPeeThree
from musichastherighttochildren.formats.m4a import EmFourAy

class Tracks(MHTRTCGlobals):
    u"""
    Scans music files located at a path, generally consisting a single album.
    """

    def __init__(self, root, verbose=True):
        self.root = self.COLLECTION + root
        self.verbose = verbose
        self.tracks = {}
        self.tracks['root'] = root
        self.load()

    def asDict(self):
        return self.tracks

    def load(self):
        if self.verbose:
            Shell.printAlbum(self.root)
        for filename in listdir(self.root):
            self.tracks[filename] = self.loadTrack(filename)

    def loadTrack(self, filename):
        if filename.startswith('.'):
            return
        elif '.' in filename:
            path = self.root + '/' + filename
            parts = filename.split('.')
            ext = parts[-1]

            if ext in self.EXTENSIONS:
                if ext.lower() == self.EXTENSION_MP3:
                    track = EmPeeThree(path)
                elif ext.lower() == self.EXTENSION_M4A:
                    track = EmFourAy(path)

                return track
            else:
                print 'Unsupported extension %s, path is %s' % (ext, path)

if __name__ == '__main__':
    tracks = Tracks()

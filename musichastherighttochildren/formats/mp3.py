#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# https://github.com/michielkauwatjoe/MusicHasTheRightToChildren

from mutagen.mp3 import MP3
from fileformat import FileFormat
from musichastherighttochildren.aux.shell import Shell

class EmPeeThree(FileFormat):
    u"""
    Retrieves MPEG-1 or MPEG-2 Audio Layer III (MP3) metadata from files.
    http://id3.org/id3v2.4.0-frames
    """

    key_musicbrainz = 'TXXX:MusicBrainz'
    key_musicbrainz_album_id = key_musicbrainz + ' ' + 'Album Id'
    key_date = 'TDRC'

    def __init__(self, path):
        self.path = path
        self.audio = MP3(path)
        self.metadata = {'format': 'mp3'}
        self.loadMetadata()

        Shell.printTrack('', '0', self.path)

    def loadMetadata(self):
        u"""
        Adds fields to metadata dictionary.
        """
        #for key, value in self.audio.items():
        #    print key, value
        print self.audio.keys()

        if self.key_date in self.audio:
            self.metadata['date'] = str(self.audio[self.key_date])
        else:
            print 'No date information in %s' % self.path
        if self.key_musicbrainz_album_id in self.audio:
            self.metadata['musicbrainz_id'] = str(self.audio[self.key_musicbrainz_album_id])

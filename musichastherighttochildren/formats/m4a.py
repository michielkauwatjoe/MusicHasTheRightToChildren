#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# https://github.com/michielkauwatjoe/MusicHasTheRightToChildren

from mutagen.m4a import M4A
from fileformat import FileFormat

class EmFourAy(FileFormat):
    u"""
    Retrieves MPEG-4 Audio Layer (M4A) metadata from files.
    """

    key_musicbrainz_album_id = '----:com.apple.iTunes:MusicBrainz Release Group Id'
    key_date = '\xa9day'

    def __init__(self, path):
        self.path = path
        self.audio = M4A(path)
        self.metadata = {'format': 'm4a'}
        self.addMetadata()

    def addMetadata(self):
        u"""
        Adds fields to metadata dictionary.
        """
        if self.key_date in self.audio:
            self.metadata['date'] = self.audio[self.key_date]
        else:
            print 'No date information in %s' % self.path

        if self.key_musicbrainz_album_id in self.audio:
            self.metadata['musicbrainz_id'] = str(self.audio[self.key_musicbrainz_album_id])

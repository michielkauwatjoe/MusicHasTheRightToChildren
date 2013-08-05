#!/usr/bin/env python
# -*- coding: utf-8 -*- 
#
# https://github.com/michielkauwatjoe/MusicHasTheRightToChildren

from mutagen.m4a import M4A

class EmFourAy:

    key_musicbrainz_album_id = '----:com.apple.iTunes:MusicBrainz Release Group Id'
    key_date = '\xa9day'

    def __init__(self, path):
        self.audio = M4A(path)
        self.metadata = {'format': 'm4a'}
        self.addMetadata()

    def addMetadata(self):
        self.metadata['date'] = self.audio[self.key_date]
        if self.key_musicbrainz_album_id in self.audio:
            self.metadata['musicbrainz_id'] = str(self.audio[self.key_musicbrainz_album_id])

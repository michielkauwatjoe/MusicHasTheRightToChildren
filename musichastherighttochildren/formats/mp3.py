#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# https://github.com/michielkauwatjoe/MusicHasTheRightToChildren

from mutagen.mp3 import MP3
from mutagen.id3 import APIC
from fileformat import FileFormat
from musichastherighttochildren.aux.shell import Shell

class EmPeeThree(FileFormat):
    u"""
    Retrieves MPEG-1 or MPEG-2 Audio Layer III (MP3) metadata from files.
    https://mutagen.readthedocs.org/en/latest/api/id3.html
    http://id3.org/id3v2.4.0-frames
    """


    txxx = 'TXXX:'
    key_musicbrainz = 'TXXX:MusicBrainz'
    key_musicbrainz_album_id = key_musicbrainz + ' ' + 'Album Id'
    key_date = 'TDRC'

    def __init__(self, path):
        self.artist = None
        self.album = None
        self.track = None
        self.tracknr = None
        self.tracktotal = None
        self.discnr = None
        self.disctotal = None
        self.fileformat = 'mp3'
        self.path = path
        self.metadata = MP3(path)
        self.loadMetadata()

        ######Shell.printTrack('', '0', self.path)

    def loadMetadata(self):
        u"""
        Adds fields to metadata dictionary.
        """

        self.artist = self.metadata['TPE1']
        self.album = self.metadata['TALB']
        Shell.printArtist(self.artist)
        Shell.printAlbum(self.album)
        frame = self.metadata['TRCK']
        tracknr, numberoftracks = str(frame).split('/')
        print tracknr
        #print frame.pprint()
        #print frame.__dict__


        '''
        for key, value in self.audio.items():
            #print key, type(value)
            if key.startswith(self.txxx):
                #print key.replace(self.txxx, '').lower(), value
                pass
            else:
                if key.startswith('APIC') or key.startswith('MCDI'):
                    print key, type(value)
                else:
                    print key, value
                #print key.lower(), value
        '''



        '''
        if self.key_date in self.audio:
            self.metadata['date'] = str(self.audio[self.key_date])
        else:
            print 'No date information in %s' % self.path
        if self.key_musicbrainz_album_id in self.audio:
            self.metadata['musicbrainz_id'] = str(self.audio[self.key_musicbrainz_album_id])
        '''

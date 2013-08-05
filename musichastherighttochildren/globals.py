# -*- coding: UTF-8 -*-

from configuration.configuration import Configuration

class Globals(Configuration):
    EXTENSION_MP3 = 'mp3'
    EXTENSION_M4A = 'm4a'
    EXTENSIONS = [EXTENSION_MP3, EXTENSION_M4A]
    
    KEY_MUSICBRAINZ = 'TXXX:MusicBrainz'
    KEY_MUSICBRAINZ_ALBUMID = KEY_MUSICBRAINZ + ' ' + 'Album Id'
    KEY_MP3_YEAR = 'TDRC'
    SDB_DOMAIN_NAME = 'musichastherighttochildren'

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# https://github.com/michielkauwatjoe/MusicHasTheRightToChildren

import json, os

from musichastherighttochildren.aux.shell import Shell
from settings.settings import Settings
from retrieval.itunes import iTunes
from retrieval.collection import Collection

class MHTRTC(object):
    u"""
    Base object.
    """
    EXTENSION_MP3 = 'mp3'
    EXTENSION_M4A = 'm4a'
    EXTENSIONS = [EXTENSION_MP3, EXTENSION_M4A]
    SDB_DOMAIN_NAME = 'musichastherighttochildren'

    ITUNES_JSON = 'data/itunes.json'
    COLLECTION_JSON = 'data/collection.json'
    DISCOGS_JSON = 'data/discogs.json'

    def __init__(self):
        u"""
        Loads colorama for color output in shell, loads personal settings.
        """
        Shell.initColorama()
        self.settings = Settings()

    def writeJSON(self, path, data):
        u"""
        Writes JSON data to file at path.
        """
        with open(path, 'w') as outfile:
            json.dump(data, outfile, sort_keys=True, indent=4, ensure_ascii=False)

    def readJSON(self, path):
        u"""
        Reads JSON data from file at path.
        """
        with open(path) as file:
            d = json.load(file)
            return d

    def getCollection(self, force=False):
        if not os.path.exists(self.COLLECTION_JSON) or force:
            collection = Collection(self, self.settings.BACKUP, verbose=True).asDict()
            self.writeJSON(self.COLLECTION_JSON, collection)
        else:
            collection = self.readJSON(self.COLLECTION_JSON)
        print 'Finished loading %s' % self.COLLECTION_JSON
        return collection

    def getITunes(self, force=False):
        if not os.path.exists(self.ITUNES_JSON) or force:
            print 'Retrieving iTunes library.'
            itunes = iTunes(self, self.settings.BACKUP_LIBRARY).asDict()
            self.writeJSON(self.ITUNES_JSON, itunes)
        else:
            itunes = self.readJSON(self.ITUNES_JSON)
        print 'Finished loading %s' % self.ITUNES_JSON
        return itunes

    def getDiscogs(self, force=False):
        if not os.path.exists(self.DISCOGS_JSON) or force:
            print 'Retrieving Discogs collection.'
            discogs = Discogs().asDict()
            self.writeJSON(self.DISCOGS_JSON, itunes)
        else:
            itunes = self.readJSON(self.DISCOGS_JSON)
        print 'Finished loading %s' % self.ITUNES_JSON
        return itunes

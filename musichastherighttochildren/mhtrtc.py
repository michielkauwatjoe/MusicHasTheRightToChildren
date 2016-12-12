#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# https://github.com/michielkauwatjoe/MusicHasTheRightToChildren

import json, os
import difflib

from aux.shell import Shell
from settings.settings import Settings
from retrieval.itunes import iTunes
from retrieval.collection import Collection

class MHTRTC(object):
    u"""
    Scans digital music collection and does various comparison and enhancement
    operations on metadata.
    """
    EXTENSION_MP3 = 'mp3'
    EXTENSION_M4A = 'm4a'
    EXTENSIONS = [EXTENSION_MP3, EXTENSION_M4A]
    SDB_DOMAIN_NAME = 'musichastherighttochildren'

    # Place where collection data is buffered for faster comparison.
    ITUNES_JSON = 'data/itunes.json'
    LOCALITUNES_JSON = 'data/localitunes.json'
    COLLECTION_JSON = 'data/collection.json'
    DISCOGS_JSON = 'data/discogs.json'

    def __init__(self):
        u"""
        Loads colorama for color output in shell, loads personal settings.
        """
        Shell.initColorama()
        self.settings = Settings()
        itunesCollection = self.getITunes(pathXML=self.settings.BACKUP_LIBRARY, pathJSON=self.ITUNES_JSON)
        localItunesCollection = self.getITunes(pathXML=self.settings.LOCAL_LIBRARY, pathJSON=self.LOCALITUNES_JSON, force=True)
        #filesCollection = self.getCollection(pathFiles=self.settings.BACKUP, pathJSON=self.COLLECTION_JSON)
        self.compareCollection(localItunesCollection, itunesCollection)

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

    # Load.
    def getCollection(self, pathFiles=None, pathJSON=None, force=False):
        u"""
        Loads and buffers entire collection stored on network. Stores files
        in JSON format.
        """
        if not os.path.exists(pathJSON) or force:
            collection = Collection(pathFiles, verbose=True).asDict()
            self.writeJSON(pathJSON, collection)

        # Reopen from file. NOTE: direct read gives Unicode errors.
        collection = self.readJSON(pathJSON)
        print 'Finished loading %s' % pathJSON
        return collection

    def getITunes(self, pathXML=None, pathJSON=None, force=False):
        u"""
        Loads and buffers local iTunes collection.
        """
        if not os.path.exists(pathJSON) or force:
            print 'Retrieving iTunes library.'
            itunes = iTunes(pathXML).asDict()
            self.writeJSON(pathJSON, itunes)

        itunes = self.readJSON(pathJSON)
        print 'Finished loading %s' % self.ITUNES_JSON
        return itunes

    def getDiscogs(self, force=False):
        u"""
        Loads and buffers Discogs collection.
        TODO: finish.
        """
        if not os.path.exists(self.DISCOGS_JSON) or force:
            print 'Retrieving Discogs collection.'
            discogs = Discogs().asDict()
            self.writeJSON(self.DISCOGS_JSON, itunes)
        else:
            itunes = self.readJSON(self.DISCOGS_JSON)

        print 'Finished loading %s' % self.ITUNES_JSON
        return itunes

    # Compare.

    def compareCollection(self, collection1, collection2):
        #print '\n'.join(sorted(collection2.keys()))
        artists = sorted(collection1.keys())

        for artist in artists:
            albums1 = collection1[artist]
            artist = self.compareArtists(artist, collection2.keys())

            if not artist is None:
                albums2 = collection2[artist]
                #self.printCompare(artist, albums1, albums2)
                self.compareAlbums(artist, albums1, albums2)
                self.compareAlbums(artist, albums2, albums1)

    def printCompare(self, artist, albums1, albums2):
        print sorted(albums1)
        print sorted(albums2.keys())

    def compareArtists(self, artist, artists):
        u"""
        """
        if artist in artists:
            return artist

        artist = artist.replace('_', '/')

        if artist in artists:
            return artist

        matches = difflib.get_close_matches(artist, artists, 3, 0.75)

        if len(matches) >= 1:
            #d = difflib.Differ()
            #diff = d.compare(artist, matches)
            #print ''.join(diff)
            match = (', '.join(matches))
            #Shell.printArtist(u'Found match(es) for artist')
            #Shell.printArtist(u' * %s' % artist)
            #Shell.printArtist(u' * %s' % match)
            artist = matches[0]
            return artist

        special_characters = [(u'é', 'e'), (u'ü', 'u')]
        escape_artist = ''

        '''
        #Testing for accents, seem to be separate characters.
        for c in artist:
            found = False

            for sc in special_characters:
                print c, sc[0], c == sc[0]
                if c == sc[0]:
                    escape_artist += sc[1]
                    found = True
                    break

            if found is False:
                escape_artist += c
        '''

        Shell.printArtist('Missing artist %s' % artist)

    def compareAlbums(self, artist, albums1, albums2):
        u"""
        TODO: also check album artist.
        """
        found = False

        for album in albums1:
            if album in albums2:
                found = True

            if not found:
                slash_album = album.replace('_', '/')
                if slash_album in albums2:
                    found = True

            if not found:
                matches = difflib.get_close_matches(album, albums2)
                if len(matches) > 0:
                    #print 'Found match(es) for %s:' % album, ', '.join(matches)
                    found = True

        if not found:
            Shell.printAlbum('Missing album %s for artist %s' % (album, artist))

if __name__ == '__main__':
    Mhtrtc = MHTRTC()
    #Mhtrtc.getCollection(force=True)

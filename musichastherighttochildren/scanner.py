# -*- coding: UTF-8 -*-

import os
import pylast
from mutagen.mp3 import MP3
from mutagen.m4a import M4A
import musicbrainz2.webservice as ws
import pyechonest

from globals import Globals
from simpledb import SimpleDB

class Scanner(Globals):
    u"""
    Scans local music collection and stores found metadata in the database.
    """

    years = []

    def main(self):
        self.SimpleDB = SimpleDB(self.AWS_ACCESS_KEY, self.AWS_SECRET_KEY, self.SDB_DOMAIN_NAME)
        self.scanCollection()
        self.SimpleDB.dumpCollection()
        n = self.SimpleDB.numberOfItems()
        print 'Number of items is %d.' % n
        #if self.HAS_LASTFM:
        #    self.scanLastFM()

    def getAlbum(self, path, files):
        name = path.split('/')[-1]
        for f in files:
            if f.startswith('.'):
                continue
            else:
                for extension in self.EXTENSIONS:
                    if f.endswith(extension):
                        return name
        return None

    def scanCollection(self):
        u"""
        Walks through iTunes folders, prints metadata.
        TODO: run in a separate process.
        """
        max = 3000
        i = 0

        for root, dirs, files in os.walk(self.COLLECTION):
            if i > max:
                return
            album = self.getAlbum(root, files)
            print album
            dict = self.scanFolder(root, files)
            #self.add(dict)

            i += 1

    def add(self, *args, **kwargs):
        self.SimpleDB.add(*args, **kwargs)

    def scanFolder(self, root, files):
        dict = {}
        
        for f in files:
            d = self.scanFile(root, f)
            for key in d:
                if not key in dict:
                    dict[key] = d[key]

        return dict

    def scanFile(self, root, f):
        dict = {}

        if '.' in f:
            parts = f.split('.')
            ext = parts[-1]
            
            if ext in self.EXTENSIONS:
                dict['format'] = ext
                path = root + '/' + f

                if ext == self.EXTENSION_MP3:
                    audio = MP3(path)
                    dict['year'] = str(audio[self.KEY_MP3_YEAR])

                    if self.KEY_MUSICBRAINZ_ALBUMID in audio:
                        dict['musicbrainz_id'] = str(audio[self.KEY_MUSICBRAINZ_ALBUMID])
                elif ext == self.EXTENSION_M4A:
                    audio = M4A(path)
                    print audio
        return dict

    def scanLastFM(self):
        pass

                            
    # Metadata functionality.
                            
    def getReleaseId(self, folder):
        pass
    
    # Datastore interface.
    
    def storeId(self, id):
        pass
    
if __name__ == '__main__':
    scanner = Scanner()
    scanner.main()

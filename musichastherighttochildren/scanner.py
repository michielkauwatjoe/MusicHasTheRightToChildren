# -*- coding: UTF-8 -*-

import os
import pylast
from mutagen.mp3 import MP3
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
            id, format = self.scanFolder(root, files)
            album = root.split('/')[-1]

            if format and id:
                #print 'Found metadata for', album, id
                self.updateDatabase(album, id)
            elif format and not id:
                print album, "doesn't contain any files that have MusicBrainz metadata."

            i += 1

    def updateDatabase(self, album, id):
        self.SimpleDB.addID(album, id)

    def scanFolder(self, root, files):
        id = None
        format = None
        
        for f in files:
            id, format = self.scanFile(root, f)
            if id and format:
                break

        return id, format
        
    def scanFile(self, root, f):
        id = None
        format = None
        
        if '.' in f:
            parts = f.split('.')
            ext = parts[-1]
            
            if ext in self.EXTENSIONS:
                if ext == self.EXTENSION_MP3:
                    format = self.EXTENSION_MP3
                    path = root + '/' + f
                    audio = MP3(path)

                    for key, value in audio.items():
                        if key.startswith(self.KEY_MUSICBRAINZ_ALBUMID):
                            id = value
                            break
        return id, format

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

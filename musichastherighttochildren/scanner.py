#!/usr/bin/env python
# -*- coding: utf-8 -*- 
#
# https://github.com/michielkauwatjoe/MusicHasTheRightToChildren

import os, codecs
import pylast

import musicbrainz2.webservice as ws
import pyechonest

from globals import Globals
from simpledb import SimpleDB
from formats.mp3 import EmPeeThree
from formats.m4a import EmFourAy

class Scanner(Globals):
    u"""
    Scans local music collection and stores found metadata in the database.
    """

    years = []

    def main(self):
        self.logfile = codecs.open('log.txt', 'a', 'UTF-8')
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

    def printReport(self, list):
        self.addToLog('Processed albums:')
        for l in list:
            self.addToLog(' - %s' % l)

    def scanCollection(self):
        u"""
        Walks through iTunes folders, prints metadata.
        TODO: run in a separate process.
        """
        i = 0
        limit = 10
        report = []

        for root, dirs, files in os.walk(self.COLLECTION):

            if i > limit:
                self.printReport(report)
                i = 0
                limit = 10
                report = []

            album = self.getAlbum(root, files)

            if album:
                report.append(album)
                dict = self.scanFolder(root, files)
                if dict:
                    dict['album'] = album
                    self.add(**dict)
                i += 1

    def add(self, *args, **kwargs):
        self.SimpleDB.add(*args, **kwargs)

    def scanFolder(self, root, files):
        dict = {}
        
        for f in files:
            d = self.scanFile(root, f)
            if d:
                for key in d:
                    if not key in dict:
                        dict[key] = d[key]

        return dict

    def scanFile(self, root, f):
        if f.startswith('.'):
            return
        elif '.' in f:
            path = root + '/' + f
            parts = f.split('.')
            ext = parts[-1]

            if ext in self.EXTENSIONS:
                try:
                    if ext.lower() == self.EXTENSION_MP3:
                        file = EmPeeThree(path)
                    elif ext.lower() == self.EXTENSION_M4A:
                        file = EmFourAy(path)
                except Exception, e:
                    self.addToLog(str(e))
                    self.addToLog(self.path)
                    return

                return file.metadata
            else:
                print 'Unknown extension %s, path is %s' % (ext, path)

    def scanLastFM(self):
        pass

                            
    # Metadata functionality.
                            
    def getReleaseId(self, folder):
        pass
    
    # Datastore interface.
    
    def storeId(self, id):
        pass

    def addToLog(self, line):
        u"""
        <doc>Appends some feedback to log file.</doc>
        """
        self.logfile.write(line)
        self.logfile.write('\n')

if __name__ == '__main__':
    scanner = Scanner()
    scanner.main()

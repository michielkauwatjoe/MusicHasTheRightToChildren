#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# https://github.com/michielkauwatjoe/MusicHasTheRightToChildren

import oauth2 as oauth
import urlparse
import csv
import json

from musichastherighttochildren.aux.shell import Shell
from musichastherighttochildren.mhtrtcglobals import MHTRTCGlobals

class Discogs(MHTRTCGlobals):
    u"""
    http://www.discogs.com/developers/
    https://github.com/jesseward/discogs-oauth-example/blob/master/discogs_example.py
    """

    def __init__(self):
        discogs = self.readCSV()
        f = open('records.json', 'wb')
        discogs_json = json.dump(discogs, f, indent=2)
        f.close()

    def readCSV(self):
        u"""
        Catalog#, Artist, Title, Label, Format, Rating, Released, release_id, CollectionFolder, Date Added, Collection Media Condition, Collection Sleeve Condition, Collection Notes
        """
        discogs = []
        with open('../data/al-khwarizmi-collection-20141013-1124.csv', 'rb') as f:
            reader = csv.reader(f)
            for row in reader:
                artist = row[1]
                album = row[2]
                label = row[3]
                discformat = row[4]
                released = row[6]
                url = 'http://www.discogs.com/release/%s' % row[7]
                row = {'artist': artist, 'album': album, 'label': label, 'discformat': discformat, 'released': released, 'url': url}
                discogs.append(row)
        return discogs

if __name__ == '__main__':
    discogs = Discogs()

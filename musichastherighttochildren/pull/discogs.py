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
        discogs_json = json.dumps(discogs)
        print discogs_json


    def readCSV(self):
        discogs = {}
        with open('../data/al-khwarizmi-collection-20141013-1124.csv', 'rb') as f:
            reader = csv.reader(f)
            for row in reader:
                artist = row[1]
                album = '%s (%s)' % (row[2], row[4])

                if not artist in discogs:
                    discogs[artist] = []
                discogs[artist].append(album)
        return discogs

if __name__ == '__main__':
    discogs = Discogs()

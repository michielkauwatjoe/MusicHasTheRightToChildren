#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# https://github.com/michielkauwatjoe/MusicHasTheRightToChildren
import os, difflib

from mhtrtc import MHTRTC
from aux.shell import Shell
from cloud.esthree import EsThree

class Sync(MHTRTC):

    def __init__(self, verbose=False, log=True):
        u"""
        """
        super(Sync, self).__init__()
        self.verbose = verbose
        self.getITunes()
        self.getCollection()
        self.getDiscogs()

        files = [self.ITUNES_JSON, self.COLLECTION_JSON, self.DISCOGS_JSON]
        self.sync(files)

    def sync(self, files):
        pass

if __name__ == '__main__':
    s = Sync(verbose=True)

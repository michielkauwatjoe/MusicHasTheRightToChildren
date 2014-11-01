#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# https://github.com/michielkauwatjoe/MusicHasTheRightToChildren

from musichastherighttochildren.aux.shell import Shell
from settings.settings import Settings

class MHTRTC(object):
    u"""
    Base object.
    """
    EXTENSION_MP3 = 'mp3'
    EXTENSION_M4A = 'm4a'
    EXTENSIONS = [EXTENSION_MP3, EXTENSION_M4A]
    SDB_DOMAIN_NAME = 'musichastherighttochildren'

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


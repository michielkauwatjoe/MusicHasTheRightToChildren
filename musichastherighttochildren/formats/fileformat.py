#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# https://github.com/michielkauwatjoe/MusicHasTheRightToChildren

class FileFormat(object):
    u"""
    Abstract base class for audio file formats containing metadata.
    """

    def addMetadata(self):
        print '[This function is required should be overridden in subclass]'
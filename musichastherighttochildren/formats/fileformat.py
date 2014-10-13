#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# https://github.com/michielkauwatjoe/MusicHasTheRightToChildren

class FileFormat(object):
    u"""
    Abstract base class for audio file formats containing metadata.
    """

    def __init__(self):
        pass

    def addMetadata(self):
        print '[This function is required and should be overridden in subclass]'

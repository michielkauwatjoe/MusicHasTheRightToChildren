#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# https://github.com/michielkauwatjoe/MusicHasTheRightToChildren
import difflib

from mhtrtc import MHTRTC
from aux.shell import Shell

class Compare(MHTRTC):
    u"""
    Compares local iTunes library to remote network library.
    """

    def __init__(self, verbose=False, log=True):
        u"""
        Holds local iTunes collection to library on network.
        """
        super(Compare, self).__init__()

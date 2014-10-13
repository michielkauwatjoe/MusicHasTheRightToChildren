#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# https://github.com/michielkauwatjoe/MusicHasTheRightToChildren

from colorama import init as colorinit
from colorama import Fore, Back, Style

'''
Colorama options:

Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Style: DIM, NORMAL, BRIGHT, RESET_ALL
'''

class Shell(object):
    u"""
    Some shell utilities.
    """

    @classmethod
    def initColorama(cls):
        colorinit(autoreset=True)

    @classmethod
    def printArtist(cls, artist):
        print Fore.BLUE + Back.RED + 'Artist: %s' % artist

    @classmethod
    def printAlbum(cls, album):
        print Fore.BLACK + Back.BLUE + Style.DIM + 'Album: %s' % album

    @classmethod
    def printDiscNr(cls, discnr):
        print Fore.BLACK + Back.YELLOW + 'Disc #%s' % discnr

    @classmethod
    def printTrack(cls, discnr, tracknr, title):
        print Fore.WHITE + Back.YELLOW + 'Track %s-%02d - %s' % (discnr, int(tracknr), title)

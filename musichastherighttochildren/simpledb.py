#!/usr/bin/env python
# -*- coding: utf-8 -*- 
#
# https://github.com/michielkauwatjoe/MusicHasTheRightToChildren

import boto
from boto.exception import SDBResponseError


class SimpleDB:
    u"""
    Connection to Amazon AWS SimpleDB (light weight NoSQL). Uses the boto interface:
    http://boto.readthedocs.org/en/latest/ref/sdb.html
    http://boto.readthedocs.org/en/latest/simpledb_tut.html
    """
    CONNECTION = None
    DOMAIN = None

    def __init__(self, awsaccesskey, awssecretkey, domainname):
        u"""
        Opens the connection or initializes a new domain on SimpleDB if it doesn't exist.
        """
        self.CONNECTION = boto.connect_sdb(awsaccesskey, awssecretkey)

        try:
            self.DOMAIN = self.CONNECTION.get_domain(domainname)
            print 'Established connection to SimpleDB domain %s' % domainname
        except SDBResponseError, e:
            print u'SimpleDB domain doesn’t exist yet, creating domain with name %s' % domainname
            self.DOMAIN = self.CONNECTION.create_domain(domainname)

    def listItems(self):
        pass

    def numberOfItems(self):
        meta = self.getMetadata()
        return meta.item_count

    def dumpCollection(self):
        f = open("dump.xml", 'w')
        fd = self.DOMAIN.to_xml(f=f)

    def getMetadata(self):
        return self.DOMAIN.get_metadata()

    def add(self, *args, **kwargs):
        u"""
        """
        self.writeItem(*args, **kwargs)

    def writeItem(self, *args, **kwargs):
        u"""
        Writes key-value pairs to database.
        """
        # Always needs album name and year to initialize item.
        album = kwargs['album']
        attrs = {'format': kwargs['format']}

        fields = ['date', 'musicbrainz_id']

        for f in fields:
            if f in kwargs:
                attrs[f] = kwargs[f]

        self.DOMAIN.put_attributes(album, attrs)

# -*- coding: UTF-8 -*-

import boto
from boto.exception import SDBResponseError


class SimpleDB:
    CONNECTION = None
    DOMAIN = None

    def __init__(self, awsaccesskey, awssecretkey, domainname):
        self.CONNECTION = boto.connect_sdb(awsaccesskey, awssecretkey)
        try:
            self.DOMAIN = self.CONNECTION.get_domain(domainname)
            print 'Established connection to SimpleDB domain %s' % domainname
        except SDBResponseError, e:
            print u'SimpleDB domain doesn’t exist yet, creating domain with name %s' % domainname
            self.DOMAIN = self.CONNECTION.create_domain(domainname)
    
    def addID(self, album, id):
        #"""
        #if 
        #
        #else:
        self.writeItem(album = album, musicbrainzid =  id)
        #"""

    def writeItem(self, *args, **kwargs):
        item = self.DOMAIN.new_item('item')
        
        for key, value in attributes.items():
            item[key] = value
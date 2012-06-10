# -*- coding: UTF-8 -*-

import boto
from boto.exception import SDBResponseError


class SimpleDB:
    SDB = None
    DOMAIN = None

    def __init__(self, awsaccesskey, awssecretkey, domainname):
        self.SDB = boto.connect_sdb(awsaccesskey, awssecretkey)
        try:
            self.DOMAIN = self.SDB.get_domain(domainname)
        except SDBResponseError, e:
            print u'SimpleDB domain doesn’t exist yet, creating domain with name %s' % domainname
            self.DOMAIN = self.SDB.create_domain(domainname)

    def writeItem(self, **attributes):
        item = self.DOMAIN.new_item('item')
        
        for key, value in attributes.items():
            item[key] = value
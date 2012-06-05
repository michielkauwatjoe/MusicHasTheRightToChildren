# -*- coding: UTF-8 -*-

import boto

class SimpleDB:
    SDB = None
    DOMAIN = None

    def __init__(self, awsaccesskey, awssecretkey, domainname):
        self.SDB = boto.connect_sdb(awsaccesskey, awssecretkey)
        self.DOMAIN = sdb.get_domain(domainname)

    def writeItem(self, **attributes):
        item = self.DOMAIN.new_item('item')
        
        for key, value in attributes.items():
            item[key] = value
# -*- coding: UTF-8 -*-

class Settings():
    u"""
    Copy file to configuration.py, which is ignored by version control, and add user credentials &c.
    """

    # Local.
    COLLECTION = '/Users/<username>/Music/iTunes/iTunes Media/Music/'
    BACKUP = '/Volumes/Family/Music/'
    LIBRARY = '/Users/<username>/Music/iTunes/iTunes Library.xml'
    BACKUP_LIBRARY = '/Volumes/Family/iTunes/iTunes Music Library.xml'

    # Last FM.
    HAS_LASTFM = True

    # Discogs.
    HAS_DISCOGS = True
    CONSUMER_KEY = ''
    CONSUMER_SECRET = ''

    # Amazon.
    AWS_ACCESS_KEY = ''
    AWS_SECRET_KEY = ''

    # PostGreSQL.
    # ...

# -*- coding: UTF-8 -*-

import os
import pylast
from mutagen.mp3 import MP3
import musicbrainz2.webservice as ws
import pyechonest

from musichastherighttochildren.globals import Globals
from musichastherighttochildren.simpledb import SimpleDB

class Scanner(Globals):
	u"""
	Scans local music collection and stores found metadata in the database.
	"""

	years = []


	def main(self):
		self.SDB = SimpleDB(self.AWS_ACCESS_KEY, self.AWS_SECRET_KEY, self.SDB_DOMAIN_NAME)
		self.scanCollection()
		if self.HAS_LASTFM:
			self.scanLastFM()

	# Setup.
			
	def scanCollection(self):
		u"""
		Walks through iTunes folders, prints metadata.
		TODO: run in a separate process.
		"""
		for root, dirs, files in os.walk(self.COLLECTION):
			id, format = self.scanFolder(root, files)
			album = root.split('/')[-1]
			album = '"' + album + '"'
			if format and id:
				print album, id
			elif format and not id:
				print album, "doesn't contain any files that have MusicBrainz metadata."
				
	def scanFolder(self, root, files):
		id = None
		format = None
		
		for f in files:
			id, format = self.scanFile(root, f)
			if id and format:
				break

		return id, format
		
	def scanFile(self, root, f):
		id = None
		format = None
		
		if '.' in f:
			parts = f.split('.')
			ext = parts[-1]
			
			if ext in self.EXTENSIONS:
				if ext == self.EXTENSION_MP3:
					format = self.EXTENSION_MP3
					path = root + '/' + f
					audio = MP3(path)
					#print audio.pprint()
					for key, value in audio.items():
						if key.startswith(self.KEY_MUSICBRAINZ_ALBUMID):
							id = value
		return id, format

	def scanLastFM(self):
		pass

							
	# Metadata functionality.
							
	def getReleaseId(self, folder):
		pass
	
	# Datastore interface.
	
	def storeId(self, id):
		pass
	
if __name__ == '__main__':
	scanner = Scanner()
	scanner.main()

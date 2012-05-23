# -*- coding: UTF-8 -*-

import os
import boto
import pylast
from mutagen.mp3 import MP3
import musicbrainz2

from musichastherighttochildren.globals import Globals

class Scanner(Globals):
	u"""
	Scans local music collection and stores found metadata in the database.
	"""

	years = []

	def main(self):
		self.scanCollection()
		if self.HAS_LASTFM:
			self.scanLastFM()

	# Setup.
			
	def scanCollection(self):
		u"""
		Walks through iTunes folders, prints metadata.
		TODO: run in a separate process.
		"""
		FOUND = False
		for root, dirs, files in os.walk(self.COLLECTION):
			if FOUND:
				break

			for f in files:
				if FOUND:
					break

				if '.' in f:
					parts = f.split('.')
					ext = parts[-1]
					if ext in self.EXTENSIONS:
						if ext == self.EXTENSION_MP3:
		
							path = root + '/' + f
							audio = MP3(path)
							try:
								year = audio['TDRC']
								track = audio['TIT2']
							except:
								print path
							print track
					
							#print audio.pprint()
							#for key, value in audio.items():
							#	print key#, value
							#FOUND = True
							#break

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

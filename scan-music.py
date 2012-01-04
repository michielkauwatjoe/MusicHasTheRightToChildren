#!/usr/bin/env python

import os
import boto
import pylast
from mutagen.mp3 import MP3

class Converter(object):

	MUSIC = '/Users/michiel/Music/iTunes/iTunes Music/Music'
	EXTENSION_MP3 = 'mp3'
	EXTENSION_M4A = 'm4a'
	EXTENSIONS = [EXTENSION_MP3, EXTENSION_M4A]
	years = []

	def main(self):
		u"""
		Walks through iTunes folders, prints metadata.
		"""
		FOUND = False
		for root, dirs, files in os.walk(self.MUSIC):
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

if __name__ == '__main__':
	converter = Converter()
	converter.main()

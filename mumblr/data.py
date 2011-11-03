# -*- tab-width: 4; use-tabs: 1; coding: utf-8 -*-
# vim:tabstop=4:noexpandtab:
"""
Handles the basic data storage
"""
from __future__ import division, absolute_import, with_statement
from random import SystemRandom
__all__ = 'WordDB',

class WordDB(object):
	"""
	Stores statistical markov chain patterns.
	"""
	
	learnfile = None
	
	def __init__(self):
		self.words = {}
		self.rnd = SystemRandom()
	
	def add_link(self, first, second):
		"""
		Adds a new link in the chain
		"""
		self.words.setdefault(first, list()).append(second)
	
	def get_next(self, first):
		"""
		Given the current node, pick the next one at random
		"""
		return self.rnd.choice(self.words[first])
	
	def generate(self, start=True, stop=False):
		word = self.get_next(start)
		while word != stop:
			yield word
			word = self.get_next(word)
	
	def genline(self, *p, **kw):
		return ' '.join(self.generate(*p, **kw))
	
	def add_line(self, line):
		prev = True # Start 
		#TODO: parse out puncuation as seperate nodes
		for w in line.split():
			self.add_link(prev, w)
			prev = w
		self.add_link(prev, False) #Finish
		
		if self.learnfile is not None:
			print repr(line)
			if line[-1] != '\n':
				line += '\n'
			self.learnfile.write(line)
	
	def load_linefile(self, file):
		for line in file:
			self.add_line(line)

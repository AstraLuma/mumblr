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

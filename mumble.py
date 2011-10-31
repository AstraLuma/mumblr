#!/usr/bin/python
# -*- tab-width: 4; use-tabs: 1; coding: utf-8 -*-
# vim:tabstop=4:noexpandtab:
"""
A basic test program to help flesh out markov chains.
"""
from __future__ import division
from random import SystemRandom

rnd = SystemRandom()

class WordDB(object):
	def __init__(self):
		self.words = {}
	
	def add_link(self, first, second):
		self.words.setdefault(first, list()).append(second)
	
	def process_data(self):
		pass
	
	def get_next(self, first):
		return rnd.choice(self.words[first])
		

words = WordDB()

# Load data
for line in open('data.mumble'):
	#TODO: parse out puncuation as seperate nodes
	Ws = line.split()
	prev = True # Start 
	for w in Ws:
		words.add_link(prev, w)
		prev = w
	words.add_link(prev, False) #Finish

# Process data
words.process_data()

# Generate a sentence
for _ in range(10):
	sentence = []
	word = words.get_next(True)
	while word is not False:
		sentence.append(word)
		word = words.get_next(word)

	print " ".join(sentence)

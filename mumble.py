#!/usr/bin/python
# -*- tab-width: 4; use-tabs: 1; coding: utf-8 -*-
# vim:tabstop=4:noexpandtab:
"""
A basic test program to help flesh out markov chains.
"""
from __future__ import division
from random import SystemRandom
from mumblr.data import WordDB

words = WordDB()

# Load data
words.load_linefile(open('data.mumble'))

# Generate a sentence
for _ in range(10):
	sentence = words.genline()
	while len(sentence.split()) < 5:
		sentence = words.genline()
	print sentence

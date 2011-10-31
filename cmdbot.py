#!/usr/bin/python
# -*- tab-width: 4; use-tabs: 1; coding: utf-8 -*-
# vim:tabstop=4:noexpandtab:
"""
A Basic bot that mumbles on command
"""
from twisted.words.protocols import irc
from twisted.internet import reactor, protocol
from mumblr.data import WordDB

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

def mumble():
	return ' '.join(words.generate(True, False))

class CommandBot(irc.IRCClient):
	"""
	A bot the mumbles on command.
	"""
	
	nickname = "astro73|mumble"
	
	def signedOn(self):
		"""Called when bot has succesfully signed on to server."""
		for c in self.factory.channels:
			self.join(c)

	def joined(self, channel):
		"""This will get called when the bot joins the channel."""
		pass

	def privmsg(self, user, channel, msg):
		"""This will get called when the bot receives a message."""
		user = user.split('!', 1)[0]
	
		# Check to see if they're sending me a private message
		if channel == self.nickname:
			msg = mumble()
			self.msg(user, msg)
			return

		# Otherwise check to see if it is a message directed at me
		if msg.startswith(self.nickname):
			msg = "%s: %s" % (user, mumble())
			self.msg(channel, msg)

class CommandBotFactory(protocol.ClientFactory):
	"""A factory for CommandBots.

	A new protocol instance will be created each time we connect to the server.
	"""
	
	# the class of the protocol to build when new connection is made
	protocol = CommandBot
	
	def __init__(self, channels):
		self.channels = channels
	
	def clientConnectionLost(self, connector, reason):
		"""If we get disconnected, reconnect to server."""
		connector.connect()
	
	def clientConnectionFailed(self, connector, reason):
		print "connection failed:", reason
		reactor.stop()


if __name__ == '__main__':
	# create factory protocol and application
	f = CommandBotFactory(['#firstchat', '#tgg-bots'])
	
	# connect factory to this host and port
	reactor.connectTCP("irc.freenode.net", 6667, f)
	
	# run bot
	reactor.run()


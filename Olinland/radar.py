from mobile import *
from room import *

class Radar (MobileThing):

	def __init__ (self,name,loc,description):
		MobileThing.__init__(self,name,loc,description)

	def use (self,actor):
		actor.say('I fiddle with the buttons on ' + self.name())

		for room in Room.rooms:
			loc = room
			cont = room.contents()
			for item in cont:
				actor.say("I detect " + item.name() + " in " + room.name())

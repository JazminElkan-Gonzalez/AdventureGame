from player import *
from mobile import *
from room import *
import random

class Butterfly (MobileThing):

	def __init__ (self,name,loc,restlessness,description):
		MobileThing.__init__(self,name,loc,description)
		self._countdown = random.randint(4,10)
		self._changeState = random.randint(5,9)
		self._state = "caterpillar"
		self._restlessness = restlessness

		Player.clock.register(self.change, 6)

	def change(self, time):
		self._countdown = self._countdown - 1
		if self._countdown == self._changeState:
			print self.name() + " became a cocoon!"
			self._state = "cocoon"
			self._description = self._description.replace("caterpillar", "cocoon")
		elif self._countdown == 0:
			print self.name() + " became a butterfly!"
			self._state = "butterfly"
			self._description = self._description.replace("cocoon", "butterfly")
			Player.clock.register(self.move_somewhere, 5)
			if not isinstance(self.location(), Room):
				print self.name() + " flew away from " + self.location().name() + "!"
				self.drop(self.location())

	def take (self,actor):
		if self._state != "butterfly":
			self.move(actor)
			actor.say("I take " + self.name())
		else:	
			actor.say("I can't catch " + self.name() + "!")

	def move_somewhere (self,time):
		if self._restlessness != 0:
			if random.randrange(self._restlessness) == 0:
				exits = self.location().exits()
				if exits:
					dir = random.choice(exits.keys())
					self.go(dir)

	def go (self,direction):
		loc = self.location()
		exits = loc.exits()
		if direction in exits:
			t = exits[direction]
			loc.report(self.name()+' moves from '+ loc.name()+' to '+t.name())
			self.move(t)
			return True
		else:
			print 'No exit in direction', direction
			return False
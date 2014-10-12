from mobile import *
from room import *


class Radar (MobileThing):

	def __init__ (self,name,loc,description):
		MobileThing.__init__(self,name,loc,description)
		self._roomArray = []

	def getRoom(self,room,direction):
		# print "thing: ", room.exits()
		# if direction in room.exits():
		return room.exits()[direction]

	def roomCheck(self,room):
		directionList = ['north',
						 'south',
						 'east',
						 'west',
						 'up',
						 'down'
						]
		
		for direction in directionList:
			if direction in room.exits():
				newRoom = self.getRoom(room, direction)
				if newRoom not in self._roomArray:
					self._roomArray.append(newRoom)
					self.roomCheck(newRoom)


	def use (self,actor):

		actor.say('I fiddle with the buttons on ' + self.name())
		# roomArray = [actor.location()]
		self._roomArray.append(actor.location())
		self.roomCheck(actor.location())

		for room in self._roomArray:
			loc = room
			cont = room.contents()
			for item in cont:
				actor.say("I detect " + item.name() + " in " + room.name())

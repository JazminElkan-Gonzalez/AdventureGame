from player import *
from npc import *
import random

class TrollHunter (NPC):

	def __init__ (self,name,loc,restlessness,power, description):
		NPC.__init__(self,name,loc,restlessness,20,description)
		self._power = power
		Player.clock.register(self.attack, 3)

	def trolls_around(self):
		return [x for x in self.location().contents() if x.is_troll()]

	def attack(self, time):
		trolls = self.trolls_around()
		if trolls:
			victim = random.choice(trolls)
			self.location().report(self.name() + ' smites ' + victim.name())
			victim.suffer(random.randint(1,self._power))
		else:
			self.location().report(self.name() + "'s sword wimpers.")

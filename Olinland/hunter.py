from player import *
from npc import *
import random

class TrollHunter (NPC):

    def __init__ (self,name,loc,restlessness,power, description):
        NPC.__init__(self,name,loc,restlessness,20,description)
        self._power = power
        Player.clock.register(self.attack, 3)

    def attack(self, time):
        trolls = self.trolls_around()
        if trolls:
            victim = random.choice(trolls)
            self.location().report(self.name() + ' smites ' + victim.name())
            victim.suffer(random.randint(1,self._power))
        else:
            self.location().report(self.name() + "'s sword wimpers.")

    def deregister(self):
        Player.clock.unregister((self.attack, 3))        

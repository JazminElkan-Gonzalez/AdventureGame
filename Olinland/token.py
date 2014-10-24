from mobile import *
from room import *
import random

class Token (MobileThing):

    def __init__ (self,name,loc,description):
        MobileThing.__init__(self,name,loc,description)

    def give (self,actor,target):
        if self in actor.inventory():
            self.drop(actor)
            target.accept(self, actor)
            if target != Player.me:
                target.deregister()
                target.become_follower(actor)
        else:
            actor.say("I don't have " + self.name())

    def take (self,actor):
        if actor == Player.me:
                self.move(actor)
                actor.say("I take " + self._name)
        else:
            self.location().report(actor.name() + " reaches for the Token but before be can reach it it mysteriously disappears")
            exits = self.location().exits()
            if exits:
                dire = random.choice(exits.keys())
                self.move(exits[dire])
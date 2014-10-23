from mobile import *
from room import *

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


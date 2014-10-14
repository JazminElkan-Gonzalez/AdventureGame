from wobject import *
from player import *

class Thing (WObject):

    def __init__ (self,name,loc, description):
        WObject.__init__(self,name)
        self._location = loc
        loc.add_thing(self)
        self._description = description

    def use (self,actor):
        actor.say('I try to use '+self.name()+' but nothing happens')

    def take (self,actor):
        actor.say("I cant take that")

    def drop (self,actor):
        actor.say("I dont have that")

    def give (self,actor,target):
        print actor.name(),'is not carrying',self.name()

    def location (self):
        return self._location
        
    def description (self):
        return self._description

    def is_in_limbo (self):
        return self.location() is None

    def destroy (self):
        self._location.del_thing(self)
        self._location = None

    def is_thing (self):
        return True

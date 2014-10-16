from thing import *

class MobileThing (Thing):

    def __init__ (self,name,loc,description):
        Thing.__init__(self,name,loc,description)
        self._original_location = loc

    def move (self,loc):
        self.location().del_thing(self)
        loc.add_thing(self)
        self._location = loc

    def take (self,actor):
        self.move(actor)
        actor.say("I take " + self._name)

    def give (self,actor,target):
        if self in actor.inventory():
            self.drop(actor)
            # self.take(target)
            target.accept(self, actor)
        else:
            actor.say("I dont have " + self.name())

    def drop (self,actor):
        if self in actor.inventory():
            actor.inventory().remove(self)
            self.move(actor)
            actor.say("I drop " + self._name)
        else:
            actor.say("I don't have a" + self.name())

    def creation_site (self):
        return self._original_location

    def is_mobile_thing (self):
        return True


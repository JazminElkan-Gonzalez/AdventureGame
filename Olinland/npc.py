from person import *
from player import *
from follower import *
import random

class NPC (Person):

    def __init__ (self,name,loc,restlessness,miserly,description):
        Person.__init__(self,name,loc,description)
        self._restlessness = restlessness
        self._miserly = miserly
        Player.clock.register(self.move_and_take_stuff, 5)
        
    def move_and_take_stuff (self,time):
        if not self.is_in_limbo() and self._restlessness != 0:
            if random.randrange(self._restlessness) == 0:
                self.move_somewhere()
            if random.randrange(self._miserly) == 0:
                self.take_something()

    def move_somewhere (self):
        exits = self.location().exits()
        if exits:
            dir = random.choice(exits.keys())
            self.go(dir)

    def take_something (self):
        everything = []
        everything.extend(self.stuff_around())
        everything.extend(self.peek_around())
        if everything:
            something = random.choice(everything)
            something.take(self)

    def become_follower(self, leader):
        Player.clock.unregister((self.move_and_take_stuff, 5))
        Follower(self.name(), self.location(), self._restlessness, self._miserly, 
            leader, self.health(), self.inventory(), self.description())
        leader.say(self.name() + " has become my follower!")
        self.say("Yay... I'm " + leader.name() + "'s follower.")
        
        self._location.del_thing(self)
        self._location = None

    def die (self):
        self.say('SHREEEEEK! I, uh, suddenly feel very faint...')
        Person.die(self)

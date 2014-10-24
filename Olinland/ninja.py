from player import *
from npc import *

class BadNinja (NPC):

    def __init__ (self,name,loc, restlessness, description):
        NPC.__init__(self,name,loc,restlessness,10,description)
        Player.clock.register(self.take_homework, 3)

    def take_homework(self, time):
        everything = []
        everything.extend(self.stuff_around())
        everything.extend(self.peek_around())
        if everything:
            for item in everything:
                if "done-hw" in item.name():
                    item.take(self)
                    item.destroy()
                    self.say("No, no, no! It's all wrong, WRONG!")
                    self.say("Burn, baby, burn!")

    def deregister(self):
        Player.clock.unregister((self.take_homework, 3))  
        Player.clock.unregister((self.move_and_take_stuff, 5))
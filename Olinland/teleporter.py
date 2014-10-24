from thing import *

class Teleporter (Thing):
    #A class that will teleport the user to their chosen location.
    #functionality: "use [teleporter.name()] [location.name()]"

    def __init__ (self,name,loc,description):
        Thing.__init__(self,name,loc,description)

    def say (self, location, msg):
        location.report(self.name() + ' says -- ' + msg)

    def use (self, actor, location):
        actor.say('I fiddle with the buttons on ' + self.name())
        actor.say("Oh no. What's That Rumbling Sound???")
        print "POOF"
        actor.say("AAAAAAHHHHHHHHHHHHHH")
        actor.location().del_thing(actor)   #similar functionality to mobileThing.move()
        location.add_thing(actor)
        actor._location = location
        self.say(location, "Thank you for using " + self.name() + ". Have a nice day! If you experience any discomfort, such as missing atoms, please contact Olin Corp.")
        self.say(location, "You are now in " + actor._location.name())
from thing import *


class Computer (Thing):
    def __init__ (self,name,loc,description):
        Thing.__init__(self,name,loc,description)

    def use(self, actor):
    	actor.say("Start up the ol' computer.")
    	for item in actor.inventory():
    		if "hw" in item.name():
		    	if "done" not in item.name():
		    		actor.say("I work on " + item.name())
		    		item.finish_homework()
		    	else:
		 			actor.say("This homework is already done.")
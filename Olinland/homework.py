from mobile import *


class Homework (MobileThing):

    def __init__ (self,name,loc,description):
        MobileThing.__init__(self,name,loc,description)

    def is_homework (self):
        return True

    def finish_homework (self):
    	self._name = "done-" + self._name
    	self._description = "A homework. This homework is done."


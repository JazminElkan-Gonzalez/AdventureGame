from mobile import *


class Homework (MobileThing):

    def __init__ (self,name,loc,description):
        MobileThing.__init__(self,name,loc,description)

    def is_homework (self):
        return True

    # FIX ME

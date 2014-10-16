from player import *
from npc import *
import random

class Professor (NPC):

			def __init__ (self,name,loc,restlessness,professorial,description):
					NPC.__init__(self,name,loc,restlessness,100,description)
					self._professorial = professorial

			_topics = ['Turing machines',
								 'the lambda calculus',
								 'Godel']

			def lecture (self,time):
				if not self.is_in_limbo():
					if random.randrange(self._professorial) == 0:
							if self.people_around():
									self.location().report(self.name()+' starts lecturing about '+random.choice(self._topics))
							else:
									self.location().report(self.name()+' mutters to himself about '+random.choice(self._topics))

			def accept (self,obj,source):
				obj.move(self)
				if "hw" in obj.name():
					if "done" in obj.name():
						self.say("Ah, a homework to be graded! Let's see here...")
						self.say("Good, good... Excellent...")
						self.say("Mmm, could have used some more comments.")
						self.say("All in all, well done. Top work.")
						self.give(obj, source)
						source.say("Thanks!")
						self.say('Thanks, ' + source.name() + "!")
						self.say("Looks like that's enough to pass the class. Congrats.")
						print "You win. Yay."
						self.say("Have fun exploring!")
					else:
						self.say("This isn't done you fool!")
						self.say("Finish it then turn it in!")
						self.give(obj, source)

class Clock (object):

    def __init__ (self,time):
        self._time = time
        self._regi = []

    def time(self):
    	return self._time

    def regi(self):
    	self._regi

	def tick(self):
		self._time = self._time + 1
		print "The clock ticks " + self_time

    # FIX ME
	def register(self, function, priority):
		if self.regi() == []:
			self._regi.append((function, priority))
		else:
			for i in range(len(self._regi)):
				fun, pri = self._regi[i]
				if priority <= pri:
					self._regi.insert(i, (function,priority))
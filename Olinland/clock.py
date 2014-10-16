class Clock (object):

    def __init__ (self,time):
        self._time = time
        self._regi = []

    def tick(self):
        self._time = self._time + 1
        if self._regi:
            for fun, pri in self._regi:
                fun(self._time)

    def time(self):
        return self._time

    def regi(self):
        self._regi

    def register(self, function, priority):
        if self._regi:
            for i in range(len(self._regi)):
                fun, pri = self._regi[i]
                if priority <= pri:
                    self._regi.insert(i, (function,priority))
        else:
            print "resiakdfja;lskdfj;alskdfj"
            self._regi.append((function, priority))
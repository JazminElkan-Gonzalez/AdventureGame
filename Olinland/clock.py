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
        return self._regi

    def register(self, function, priority):
        if self._regi:
            for i in range(len(self._regi)):
                fun, pri = self._regi[i]
                if priority <= pri:
                    self._regi.insert(i, (function,priority))
                    break
                elif i == len(self._regi) -1 and priority > pri:
                    self._regi.append((function, priority))
                    break
        else:
            self._regi.append((function, priority))

    def unregister(self, function):
        if function in self._regi:
            self._regi.remove(function)
import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))

class LoggableList(list, Loggable):
    def append(self, x):
        self.log(x)
        super().append(x)

def test():
    t = LoggableList()
    t.append(1)
    t.append(2)

    assert len(t) == 2

test()

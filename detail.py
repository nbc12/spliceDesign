import pprint

global fiberCounter
fiberCounter = 0

class Fiber:
    def __init__(self, fiberID):
        self.ID = fiberID


class Cable:
    
    def __init__(self, fibers):
        self.fibers = []
        for i in range(fibers):
            self.fibers.append(Fiber(fiberCounter))
            fiberCounter = fiberCounter + 1

a = Cable(144)


pp = pprint.PrettyPrinter(indent=4)
pp.pprint(a.fibers[5].ID)
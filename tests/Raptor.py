from . import Classes

class Raptor:
    def __init__(self):
        self.round = range(10)
        self.eap = None # Earliest Arrival Problem
        self.markedStops = list()
        self.activeRoutes = {}
        self.rjourneys = None
        self.q={}


    def execraptor(self, dstop, astop, dtime):
            self.markedStops.append(dstop)
            for  i in self.round:
                self.q.clear()
                for j  in self.markedStops:
                    for l in self.markedStops(j).sroutes:
                        if self.markedStops(j).sroutes(l) in q && if markedstops(j).index() < markedstop(j).index()
                            self.q.update()













class Raptor:
    def __init__(self):
        self.round = range(10)
        self.eap = None  # Earliest Arrival Problem
        self.markedStops = list()
        self.activeRoutes = {}
        self.rjourneys = None
        self.q = {}

    def execraptor(self, dstop, astop, dtime):
        #
        #    for h in data.stops:   -- Goal is to set every departure time as infinite for every round of every stop
        #       data.stops[h] = 'inf'
        #   data.stops[dstops]. = dtime
        #   self.markedstops.append(dstop)
            self.markedStops.append(dstop)
            for i in self.round:
                self.q.clear()
                for j in self.markedStops:
                    for l in self.markedStops[i].sroutes:
                        if (self.markedStops[j].sroutes[l] in self.q) and (self.markedStops[j].index() < self.markedStops[j].index()):
                            self.q.update(sroutes[l]:self.markedStops[j]))
                        else:
                            self.q.update()

# Definition of the class stops which a represent a bus,tram,metro,train stop
class Stop:

    def __init__(self, idstop, nomstop, latstop, longstop):
        self.idstop = idstop    # GTFS stop ID
        self.nomstop = nomstop  # Stop name
        self.latstop = latstop  # Latitude stop
        self.longstop = longstop    # Longitude stop
        self.sroutes = []   # Routes serving the stop
        self.nbsroutes = [] # Order of the stop in the Route use "{}" ?
        self.stransferts = []


class Trip:
    def __init__(self, tdepart, thdepart, tarrive, tharrive, troute):
        self.route = troute
        self.depart = tdepart
        self.arrivee = tarrive
        self.hdepart = thdepart
        self.harrivee = tharrive
        self.tstops = []
        self.jtrips = []


class Rounds:
    def __init__(self):
        pass


class Journey:
    def __init__(self, jdepart, jhdepart):
        self.jtrips = []
        self.depart = jdepart
        self.arrivee = float("inf")
        self.depart = jhdepart
        self.transferts = []
        self.PickUpS = {}
        self.DropOffS = {}

    def addtrip(self, trip):
        self.jtrips.append(trip)

    def addtransfert(self, transfert):
        self.transferts.append(transfert)


class Route:
    def __init__(self, idroute, rname, rshortname):
        self.id = idroute
        self. rstops = []
        self.rtrips = []
        self.rname = rname
        self.rshortname = rshortname

    def addstop(self, stop):
        self.rstops.append(stop)

    def addtrip(self, trip):
        self.rtrips.append(trip)


class Transfert:
    def __init__(self, ttime, tdepart, tarrive):
        self.time = ttime
        self.depart = tdepart
        self.arrive = tarrive














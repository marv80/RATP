# Definition of the class stops which a represent a bus,tram,metro,train stop
import pandas as pd

class Stop:

    def __init__(self, idstop, nomstop, latstop, longstop):
        self.idstop = idstop    # GTFS stop ID
        self.nomstop = nomstop  # Stop name
        self.latstop = latstop  # Latitude stop
        self.longstop = longstop    # Longitude stop
        self.sroutes = list()   # Routes serving the stop
     #  self.nbsroutes = list()  # Order of the stop in the Route use "{}" ?
        self.stransferts = list()


class Trip:
    def __init__(self, tdepart, thdepart, tarrive, tharrive, troute):
        self.route = troute
        self.depart = tdepart
        self.arrivee = tarrive
        self.hdepart = thdepart
        self.harrivee = tharrive
        self.tstops = list()
        self.jtrips = list()


class Rounds:
    def __init__(self):
        pass


class Journey:
    def __init__(self, jdepart, jhdepart):
        self.jtrips = list()
        self.depart = jdepart
        self.arrivee = float("inf")
        self.depart = jhdepart
        self.transferts = list()
        self.PickUpS = {}
        self.DropOffS = {}

    def addtrip(self, trip):
        self.jtrips.append(trip)

    def addtransfert(self, transfert):
        self.transferts.append(transfert)


class Route:
    def __init__(self, idroute, rname, rshortname):
        self.id = idroute
        self. rstops = list()
        self.rtrips = list()
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

class Timetable:
    def __init__(self, ttdtime):
        self.ttdtime = ttdtime
        self.ttroute = {}
        self.ttstops = ()

    def liststops(self, data_stops, data_routes):
        for index, row in data_stops.iterrows():
            stop = None
            stop.idstop = row[0]
            stop.latstop = row[4]
            stop.longstop = row[5]
            stop.nomstop = row[2]
            self.ttstops.append(stop)


#class earliestarrivalproblem:
 #   def __init__(self):
    #self.eapraptor =  None
    #self.timetable = None
    #results = list()
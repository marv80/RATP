class Timetable:
    def __init__(self, ttdtime):
        self.ttdtime = ttdtime
        self.ttroute = {}
        self.ttstops = list()

    def liststops(self, data_stops, data_routes):
        for index, row in data_stops.iterrows():
            id = row[0]
            name = row[2]
            adr = row[3]
            lat = row[4]
            long = row[5]
            stop = Stop(id, name, adr, lat, long)
            self.ttstops.append(stop)

# def listroutes(self, data_routes, data_stops):


class Stop:

    def __init__(self, idstop, nomstop, sadr, latstop, longstop):
        self.idstop = idstop    # GTFS stop ID
        self.nomstop = nomstop  # Stop name
        self.sadr = sadr        # Stop adress
        self.latstop = latstop  # Latitude stop
        self.longstop = longstop    # Longitude stop
        self.sroutes = list()   # Routes serving the stop
        self.stransferts = list()
        self.eaa = {} # earliest arrival at the stop for a round k


class Route:
    def __init__(self, idroute, agencyid,rshortname, rname, rtype, rcolor, rtextcolor):
        self.id = idroute
        self.agencyid = agencyid
        self.rshortname = rshortname
        self.rname = rname
        self.rtype = rtype
        self.rcolor = rcolor
        self.rtextcolor = rtextcolor
        self.rstops = list()
        self.rtrips = list()
        self.data_trips = 0

   # def Getstops(self):


class Trip:
    def __init__(self, routeid , serviceid, id, tshortname, directionid):
        self.routeid = routeid
        self.serviceid = serviceid
        self.id = id
        self.tshortname = tshortname
        self.directionid = directionid
        # self.depart = tdepart
        # self.arrivee = tarrive
        # self.hdepart = thdepart
        # self.harrivee = tharrive
        self.tstops = list()
        self.jtrips = list()

class Stoptimes:
    def __init__(self, tripid, arrtime, deptime, stopid):
        self.tripid = tripid
        self.arrtime = arrtime
        self.deptime = deptime
        self.stopid = stopid


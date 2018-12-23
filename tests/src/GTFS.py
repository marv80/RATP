import pandas as pd
import Class


class GTFS:
    def __init__(self):
        self.data_routes = pd.read_csv('data/routes.txt', sep=",", header=0)
        self.data_stops = pd.read_csv('data/stops.txt', sep=",", header=0)
        self.data_agency = pd.read_csv('data/agency.txt', sep=",", header=0)
        self.data_calendar_dates = pd.read_csv('data/calendar_dates.txt', sep=",", header=0)
        self.data_calendar = pd.read_csv('data/calendar.txt', sep=",", header=0)
        self.data_stops_times = pd.read_csv('data/stop_times.txt', sep=",", header=0)
#        self.data_transfers = pd.read_csv('data/transfers.txt', sep=",", header=0)
        self.data_trips = pd.read_csv('data/trips.txt', sep=",", header=0)
        self.data_stops_times['departure_time'] = pd.to_datetime(self.data_stops_times['departure_time'], format='%H:%M:%S')
        self.data_stops_times['arrival_time'] = pd.to_datetime(self.data_stops_times['arrival_time'], format='%H:%M:%S')
        self.gtfs_stops = list()
        self.gtfs_routes = list()
        self.gtfs_trips = list()
        self.gtfs_stopstimes = list()

    def read_stops(self):
        for index, row in self.data_stops.iterrows():
            sid = row[0]
            sname = row[2]
            sadr = row[3]
            slat = row[4]
            slong = row[5]
            stop = Class.Stop(sid, sname, sadr, slat, slong)
            self.gtfs_stops.append(stop)

    def read_routes(self):
        for index, row in self.data_routes.iterrows():
            rid = row[0]
            agencyid = row[1]
            rshortname = row[2]
            rlongname = row[3]
            rtype = row[5]
            rcolor = row[6]
            rtcolor = row[7]
            route = Class.Route(rid, agencyid, rshortname, rlongname, rtype, rcolor, rtcolor)
            self.gtfs_routes.append(route)


# add the trips in different routes
    def get_trips(self):
        for i in self.gtfs_routes:
            df = self.data_trips.loc[self.data_trips['route_id'] == i.id]
            for index, row in df.iterrows():
                r_id = row[0]
                serviceid = row[1]
                tid = row[2]
                tshortname = row[4]
                directionid = row[5]
                trip = Class.Trip(r_id, serviceid, tid, tshortname, directionid)
                i.rtrips.append(trip)

    def get_stops(self):
        listestops = list()
        for i in self.gtfs_routes:
                dfst = self.data_stops_times.loc[self.data_stops_times['trip_id'] == i.rtrips[0].id]
                dfst = dfst.sort_values(by='departure_time')
                for index, row in dfst.iterrows():
                    listestops.append(row[3])
                for j in listestops:
                    for index, row in self.data_stops.iterrows():
                        if j == row[0]:
                            sid = row[0]
                            sname = row[2]
                            sadr = row[3]
                            slat = row[4]
                            slong = row[5]
                            stop = Class.Stop(sid, sname, sadr, slat, slong)
                            i.rstops.append(stop)

    def read_trips(self):
        for index, row in self.data_trips.iterrows():
            r_id = row[0]
            serviceid = row[1]
            tid = row[2]
            tshortname = row[4]
            directionid = row[5]
            trip = Class.Trip(r_id, serviceid, tid, tshortname, directionid)
            self.gtfs_trips.append(trip)

    def read_stopstimes(self):
        for index, row in self.data_stops_times.iterrows():
            tid = row[0]
            arrtime = row[1]
            deptime = row[2]
            stopid = row[3]
            stoptime = Class.Stoptimes(tid, arrtime, deptime, stopid)
            self.gtfs_stopstimes.append(stoptime)

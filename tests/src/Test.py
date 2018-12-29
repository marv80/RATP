import GTFS
import GPS
import pandas as pd


def main():
    gtfs = GTFS.GTFS()
    for s in gtfs.gtfs_stops:
        print("Pour l'arrêt : " + s.nomstop + ", les transferts possible sont :")
        for t in s.stransfers:
            print(t.nomstop)

"""""
    for r in gtfs.gtfs_routes:
        print(r.rname)
        for g in r.rstops:
            print(g.nomstop)

    gtfs = GTFS.GTFS()
    ndepart = "Vavin"
    narrive = "Samplon"
    depart = []
    dist = 'inf'
    for s in gtfs.gtfs_stops:
        if (s.nomstop == ndepart) & ((not s.sroutes) == False):
            depart.append(s)

    for s in gtfs.gtfs_stops:
        if (s.nomstop == narrive) & ((not s.sroutes) == False):
            sstop = s

    for s in depart:
        if(GPS.distanceGPS(s.latstop, s.longstop, sstop.latstop, sstop.longstop) < dist):
            sstart = s

    for r in sstart.sroutes:
            print("La route est :" + r.rname)
            for d in r.rstops:
                print(r.rstops.index(depart))
    """""






if __name__ == "__main__":
    # execute only if run as a script
    main()


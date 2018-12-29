import GTFS
import GPS

def calcdist(stopa, stopb):
    dist = GPS.distanceGPS(stopa.latstop, stopa.longstop, stopb.latstop, stopb.longstop)
    return dist

def main():

    gtfs = GTFS.GTFS()
    start = input("Enter your departure station: ")
    depart = []
    arrive = []
    dist = float("inf")
    for s in gtfs.gtfs_stops:
        if s.nomstop == start:  # & ((not s.sroutes) == False):
            depart.append(s)

    sstop = None
    end = input("enter your arrival station: ")
    for g in gtfs.gtfs_stops:
        if g.nomstop == end:
            sstop = g
            arrive.append(g)

    for s in depart:
        for r in s.sroutes:
            ind = r.rstops.index(s)
            print("L'arret est :" + r.rstops[ind+1].nomstop + "Et sa distance a l'arrivee est de :")
            testdist = calcdist(r.rstops[ind+1],sstop)
            # testdist = (GPS.distanceGPS(r.rstops[ind+1].latstop, r.rstops[ind+1].longstop, sstop.latstop, sstop.longstop))
            if testdist < dist:
                dist = testdist
                sstart = s


    print("the departure station is: " + sstart.nomstop + " and the arrival station is: "+sstop.nomstop)
    distarr = GPS.distanceGPS(sstart.latstop, sstart.longstop, sstop.latstop, sstop.longstop)
    print("La distance actuelle est de : ")
    print(distarr)

    curr = sstart
    ccand = sstart
    it = 0
    nxt = 0
    # for h in ccand.sroutes:
    #    print(h.rname)

    while curr.nomstop != end:
        if curr == ccand:
            nxt = 1
            it = it + 1
        else:
            it = 0
            nxt = 0
            curr = ccand
        if it == 4:
            break
        print("l'arret actuel est :"+curr.nomstop)
        for h in curr.sroutes:
          #  print(h.rstops.index(curr) + 1)
            ind = h.rstops.index(curr)
            comp = h.rstops[ind + 1 + nxt]
            distcomp = calcdist(curr, comp)
            if distcomp < distarr:
                distarr = distcomp
                ccand = comp

    print("Arrivé à : "+curr.nomstop)
    for g in curr.sroutes:
        print(g.rname)

    '''
    gtfs = GTFS.GTFS()
    for i in gtfs.gtfs_stops:
        print("/T/T" + i.nomstop)
        for j in i.sroutes:
            print(j.rname)
    '''
if __name__ == "__main__":
    # execute only if run as a script
    main()

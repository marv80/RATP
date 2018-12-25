import GTFS
import GPS

def main():

    """""
        data_routes = pd.read_csv('data/routes.txt', sep=",", header=0)
        data_trips = pd.read_csv('data/trips.txt', sep=",", header=0)
        # print(data_routes)
        lroute = list()
        for index, row in data_routes.iterrows():
            var = row[0]
            lroute.append(var)

        print(lroute[0])
        df = data_trips.loc[data_trips['route_id'] == lroute[1]]
        print(df)
    
    """


gtfs = GTFS.GTFS()

sstart = None
start = input("Enter your departure station: ")
for s in gtfs.gtfs_stops:
    if(s.nomstop == start) & ((not s.sroutes) == False):
        sstart =s

sstop = None
end = input("enter your arrival station: ")
for g in gtfs.gtfs_stops:
    if g.nomstop == end:
        sstop = g

print("the departure station is: "+ sstart.nomstop+ " and the arrival station is: "+sstop.nomstop)
distarr = GPS.distanceGPS(sstart.latstop, sstart.longstop, sstop.latstop, sstop.longstop)
# print(distarr)
curr = None
ccand = sstart
it = 0
#for h in ccand.sroutes:
#    print(h.rname)

while ((curr != sstop) or (it == 4)):
    nxt = 1
    it = 4
    if curr == ccand:
        nxt = nxt + 1
        it = it + 1
    else:
        it = 4
        curr = ccand
    print("l'arret actuel est :"+curr.nomstop)
    for h in curr.sroutes:
        ind = h.rstops.index(curr) + nxt
        comp =h.rstops[ind]
        distcomp = GPS.distanceGPS(curr.latstop, curr.longstop, comp.latstop, comp.longstop)
        if distcomp < distarr:
            distarr = distcomp
            ccand = comp
            it = 4

print("Arrivé à : "+curr.nomstop)

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

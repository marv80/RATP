import GTFS
import Go
## Text menu in Python



gtfs = GTFS.GTFS()

loop = True

while loop:  ## While loop which will keep going until loop = False

        stop = input("Select a stop : ")
        for s in gtfs.gtfs_stops:
            if s.nomstop == stop:
                print(s.nomstop)
                for r in s.sroutes:
                    print("Ligne : " + r.rshortname + r.rname )

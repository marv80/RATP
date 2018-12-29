import GTFS
import Go
## Text menu in Python



gtfs = GTFS.GTFS()

loop = True

while loop:  ## While loop which will keep going until loop = False

        line = input("Select a line : ")
        for r in gtfs.gtfs_routes:
            if r.rshortname == line:
                print(r.rname)
                for s in r.rstops:
                    print(s.nomstop)

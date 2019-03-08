import GTFS
import Go
## Text menu in Python



gtfs = GTFS.GTFS()

loop = True

while loop:  ## While loop which will keep going until loop = False

        path = Go.astar(gtfs,source,destination)
        print("Your path start at : " + path[0].sadr)
        for s in path:
            print(s.nomstop)
            if s.actual_route:
                print("On line : ")
                print(s.actual_route.rshortname)
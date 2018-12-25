import GTFS
import pandas as pd


def main():
    depart = "19NOVEMBRE"

    gtfs = GTFS.GTFS()
    for i in gtfs.gtfs_stops:
            if i.nomstop == depart:
                curr = i
    for k in curr.sroutes:
        print(k.rname)






if __name__ == "__main__":
    # execute only if run as a script
    main()


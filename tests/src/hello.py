import GTFS


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
    for i in gtfs.gtfs_stops:
        if i.idstop == 7:
            for j in i.sroutes:
                print(j.rname)

if __name__ == "__main__":
    # execute only if run as a script
    main()

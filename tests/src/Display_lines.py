def display_tram():

 data_routes = pd.read_csv('data/routes.txt', sep=",", header=0)
 #data_trips = pd.read_csv('data/trips.txt', sep=",", header=0)
 data_routes.rename(columns={'route_id':'Line', 'route_long_name':'Direction'}, inplace=True)
 print(data_routes.loc[data_routes['route_short_name'].isin(['T1','T2','T3A','T3B','T5','T6','T7','T8']),['Line','Direction']])

def display_metro():

 data_routes = pd.read_csv('data/routes.txt', sep=",", header=0)
 #data_trips = pd.read_csv('data/trips.txt', sep=",", header=0)
 data_routes.rename(columns={'route_id':'Line', 'route_long_name':'Direction'}, inplace=True)
 print(data_routes.loc[data_routes['route_short_name'].isin(['1','2','3','4','5','6','7','8','9','10','11','12','13','14']),['Line','Direction']])

def display_rer():

 data_routes = pd.read_csv('data/routes.txt', sep=",", header=0)
 #data_trips = pd.read_csv('data/trips.txt', sep=",", header=0)
 data_routes.rename(columns={'route_id':'Line', 'route_long_name':'Direction'}, inplace=True)
 print(data_routes.loc[data_routes['route_short_name'].isin(['A','B']),['Line','Direction']])
 #print(data_routes)


def display_bus():

 data_routes = pd.read_csv('data/routes.txt', sep=",", header=0)
 #data_trips = pd.read_csv('data/trips.txt', sep=",", header=0)
 data_routes.rename(columns={'route_id':'Line', 'route_long_name':'Direction'}, inplace=True)
 print(data_routes.loc[~data_routes['route_short_name'].isin(['A','B','1','2','3','4','5','6','7','8','9','10','11','12','13','14','T1','T2','T3A','T3B','T5','T6','T7','T8']),['Line','Direction']])

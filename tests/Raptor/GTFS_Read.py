import pandas as pd
data_routes = pd.read_csv('data/routes.txt', sep=",", header=0)
data_agency = pd.read_csv('data/agency.txt', sep=",", header=0)
data_calendar_dates = pd.read_csv('data/calendar_dates.txt', sep=",", header=0)
data_calendar = pd.read_csv('data/calendar.txt', sep=",", header=0)
data_stop_times = pd.read_csv('data/stop_times.txt', sep=",", header=0)
data_stops = pd.read_csv('data/stops.txt', sep=",", header=0)
data_transfers = pd.read_csv('data/transfers.txt', sep=",", header=0)
data_trips = pd.read_csv('data/trips.txt', sep=",", header=0)
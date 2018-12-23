import pandas as pd
data = pd.read_csv('data/stops.txt', sep=",", header=0)
print(data)
data.columns = ["stop_id", "stop_code", "stop_name", "stop_desc", "stop_lat", "stop_lon", "location_type", "parent_station"]
print(data)

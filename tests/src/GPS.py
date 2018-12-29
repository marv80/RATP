from math import sin, cos, acos, pi

# Convert an angle "degrees minutes seconds" to "decimal degrees"
def convert_dms_dd(d, m, s):
    return d + m / 60 + s / 3600


# Convert an angle "decimal degrees" to "degrees minutes seconds"
def convert_dd_dms(dd):
    d = int(dd)
    x = (dd - d) * 60
    m = int(x)
    s = (x - m) * 60
    return d, m, s


# Convert an angle "decimal degrees" to "radians"
def convert_dd_rad(dd):
    return dd / 180 * pi


# Convert an angle "radians" to "decimal degrees"
def convert_rad_dd(rd):
    return rd / pi * 180


# function to define the distance between two points (with their GPS coordinates)
def distanceGPS(latA, longA, latB, longB):
    # radius of the earth in meter
    RT = 6378137
    # angle in radians between the 2 points
    S = acos(sin(latA) * sin(latB) + cos(latA) * cos(latB) * cos(abs(longB - longA)))
    return S * RT


#############################################################################
if __name__ == "__main__":
    latA = convert_dd_rad(47.390668)  # North
    longA = convert_dd_rad(0.689319)  # East

    latB = convert_dd_rad(45.826516)  # North
    longB = convert_dd_rad(1.260290)  # East

    dist = distanceGPS(latA, longA, latB, longB)
    print ( "The distance is around", int(dist), "meters.")

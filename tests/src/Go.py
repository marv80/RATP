import GTFS
import GPS
import Class

def calcdist(stopa, stopb):
    dist = GPS.distanceGPS(stopa.latstop, stopa.longstop, stopb.latstop, stopb.longstop)
    return dist

def astar():

    gtfs = GTFS.GTFS()
    start = input("Enter your departure station: ")
    depart = []
    arrive = []
    dist = float("inf")
    for s in gtfs.gtfs_stops:
        if s.nomstop == start:  # & ((not s.sroutes) == False):
            depart.append(s)

    sstop=0
    end = input("enter your arrival station: ")
    for g in gtfs.gtfs_stops:
        if g.nomstop == end:
            sstop = g
            arrive.append(g)

    for s in depart:
        for r in s.sroutes:
            ind = r.rstops.index(s)
            testdist = calcdist(r.rstops[ind+1],sstop)
            if testdist < dist:
                dist = testdist
                sstart = s


    print("the departure station is: " + sstart.nomstop + " and the arrival station is: "+sstop.nomstop)
    distarr = GPS.distanceGPS(sstart.latstop, sstart.longstop, sstop.latstop, sstop.longstop)
    print("La distance actuelle est de : ")
    print(distarr)

    start_node = Class.Node(None, sstart)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Class.Node(None, sstop)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    # Loop until you find the end
    while len(open_list) > 0:

        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            print("the current node in open list is: " + open_list[index].position.nomstop)
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        if current_node.position.nomstop == end_node.position.nomstop:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]  # Return reversed path

        # Generate children
        children = []

        for h in current_node.position.sroutes:
            print(h.rshortname)
            ind = h.rstops.index(current_node.position)
            nn = h.rstops[ind + 1]
            new_node = Class.Node(current_node, nn)
            new_node.g = calcdist(new_node.position, current_node.position)
            new_node.h = calcdist(new_node.position, end_node.position)
            new_node.f = new_node.h + new_node.g
            children.append(new_node)

        for child in children:

            #child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    continue



            # Child already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            open_list.append(child)

def main():
    path = astar()
    print(path)

if __name__ == '__main__':
    main()





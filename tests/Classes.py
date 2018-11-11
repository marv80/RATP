# Definition of the class stops which a represent a bus,tram,metro,train stop
class Stop:

    def __init__(self, tchangement):
        # tchangement might replace F footpath when in the same station
        self.tchangement = tchangement


class Trajet:
    def __init__(self, tdepart, thdepart, tarrivee, tharrivee):
        self.depart = tdepart
        self.arrivee = tarrivee
        self.hdepart = thdepart
        self.harrivee = tharrivee
        self.stops = []


class Rounds:
    def __init__(self):
        pass


class Journey:
    def __init__(self, jdepart, jhdepart):
        self.trajet = []
        self.depart = jdepart
        self.arrivee = float("inf")
        self.depart = jhdepart


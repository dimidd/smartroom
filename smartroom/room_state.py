import copy
from room_item import ItemDescriptor, Bench
from smartroom.room_goal import GoalVerifier


class Segment:
    def __init__(self, lcorner, size):
        self.lcorner = lcorner
        self.size = size

    def __str__(self):
        return '(LC:' + str(self.lcorner) + ', SZ:' + str(self.size) + ')'

    def __repr__(self):
        return str(self)


class RoomState(object):
    def __init__(self, seats, bounds):
        self.seats = seats
        self.bounds = bounds
  
    def size(self):
        return len(self.seats)

    def __str__(self):
        return str(self.seats)
  

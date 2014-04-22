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
        res = ''
        if self.bounds[0] > 0:
                res += '|' * self.bounds[0]
                res += ' '
        for i, v in enumerate(self.seats):
            res += str(v)
            res += ' '
            if self.bounds[i + 1] > 0:
                res += '|' * self.bounds[i + 1]
                res += ' '
        return res

    #TODO: save this in state, rather than recomputing?
    def analyze(self, verf):
        i = 0
        spaces = []
        shapes = []
        unsatisfied = copy.deepcopy(verf.descriptors)
        seats = self.seats
        bounds = self.bounds
        item_sizes = dict()
        for i, desc in enumerate(unsatisfied):
            sz = desc.item.size()
            item_sizes[sz] = i

        while i < len(seats):
            if not seats[i]:
                cur_spaces = []
                while i < len(seats) and not seats[i]:
                    cur_spaces.append(Segment(i, -1))
                    i += 1
                for seg in cur_spaces:
                    seg.size = i - seg.lcorner
                spaces.extend(cur_spaces)

            else:
                # TODO: check consistency
                lcorner = i
                i = i + 1
                while i < len(seats) and 0 == bounds[i]:
                    i += 1
                sz = i - lcorner
                shapes.append(Segment(lcorner, sz))
                if sz in item_sizes:
                    unsatisfied[item_sizes[sz]].count -= 1

        return spaces, shapes, unsatisfied

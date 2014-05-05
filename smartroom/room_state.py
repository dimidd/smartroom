import copy
from room_item import ItemDescriptor, Bench
from smartroom.room_goal import GoalVerifier


class Segment:
    def __init__(self, lcorner, size):
        self.lcorner = lcorner
        self.sz = size

    def __str__(self):
        return '(LC:' + str(self.lcorner) + ', SZ:' + str(self.size) + ')'

    def __repr__(self):
        return str(self)


class RoomState(object):
    def __init__(self, seats):
        self.seats = seats

    def size(self):
        return len(self.seats)

    def __str__(self):
        res = ''
        for row in self.seats:
            for col in row:
                res += str(col)
                res += ' '
            res += '\n'
        return res

    #TODO: save this in state, rather than recomputing?
    def analyze(self, verf):
        spaces = []
        shapes = []
        unsatisfied = copy.deepcopy(verf.descriptors)
        seats = self.seats
        item_sizes = dict()
        for i, desc in enumerate(unsatisfied):
            sz = desc.item.size()
            item_sizes[sz] = i

        len_row = len(seats[0])
        for i_row in xrange(len(seats)):
            i_col = 0
            while i_col < len_row:
                if not seats[i_row][i_col]:
                    cur_spaces = []
                    while i_col < len_row and not seats[i_row][i_col]:
                        cur_spaces.append(Segment((i_row, i_col), -1))
                        i_col += 1
                    for seg in cur_spaces:
                        seg.size = i_col - seg.lcorner[1]
                    spaces.extend(cur_spaces)

                else:
                    # TODO: check consistency
                    lcorner = i_row, i_col
                    while i_col < len_row and seats[i_row][i_col]:
                        i_col += 1
                    sz = i_col - lcorner[1]
                    shapes.append(Segment(lcorner, sz))
                    if sz in item_sizes:
                        unsatisfied[item_sizes[sz]].count -= 1

        return spaces, shapes, unsatisfied

    def __eq__(self, other):
        if not (isinstance(other, RoomState)):
            return False
        return self.seats == other.seats

    def __ne__(self, other):
        return self.__eq__(other)

if __name__ == '__main__':
    seats = [[False, True, True, False, False], [False, False, False, False, False]]
    s1 = RoomState(seats)
    descs = [ItemDescriptor(Bench(2), 2)]
    verf = GoalVerifier([], descs)
    spaces, shapes, unsatisfied = s1.analyze(verf)

    print 'state:\n', s1
    print 'spaces:', spaces
    print 'shapes:', shapes
    print 'unsatisfied', unsatisfied

from aima.search import astar_search as astar
from smartroom.room_state import RoomState
from smartroom.room_goal import GoalVerifier
from smartroom.room_problem import RoomProblem
from smartroom.room_constraint import IsolatedItems, FacingItems
from smartroom.room_item import *


class InitialStateInputErr (Exception):
    def __init__(self, token):
        self.token = token

    def __str__(self):
        return 'Invalid token:' + self.token


# TODO: validate input
def read_descriptors(descs_filename):
    descs = []
    with open(descs_filename) as desc_file:
        for line in desc_file:
            splitted = line.split()
            class_name = splitted[0]
            params = splitted[1]
            n_items = splitted[2]
            # TODO: replace eval with something safer
            item = eval(class_name + params)
            item_desc = ItemDescriptor(item, int(n_items))
            descs.append(item_desc)
    return descs


def read_initial(initial_filename):
    initial = []
    # TODO: support also 0,1 instead of True,False
    with open(initial_filename) as initial_file:
        try:
            for i_line, line in enumerate(initial_file):
                splitted = line.split()
                row = []
                for bool_str in splitted:
                    if bool_str in ('False', 'True'):
                        row.append('True' == bool_str)
                    else:
                        raise InitialStateInputErr(bool_str)
                initial.append(row)

            return initial

        except Exception as e:
            print e

# TODO: get input from commandline
descs_filename = "input7.txt"
initial_filename = "initnb7_2d.txt"
descs = read_descriptors(descs_filename)
initial = read_initial(initial_filename)

initial_state = RoomState(initial)
verf_nocst = GoalVerifier([], descs)
verf_isolt = GoalVerifier([IsolatedItems(), FacingItems(1, 3, None)], descs)
verf_isolt.constarints[1].verf = verf_isolt
problem = RoomProblem(initial_state, verf_isolt)
sol = astar(problem)
for s in sol.path():
    print str(s.state)

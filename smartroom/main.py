from aima.search import astar_search as astar
from smartroom.room_item import ItemDescriptor
from smartroom.room_item import Bench
from smartroom.room_state import RoomState
from smartroom.room_goal import GoalVerifier
from smartroom.room_problem import RoomProblem
from smartroom.room_constraint import IsolatedItems

#TODO: get input from commandline


descs_filename="input1.txt"
initial_filename="initial2.txt"

descs = []
#TODO: validate input
with open(descs_filename) as desc_file:
    for line in desc_file:
        splitted = line.split()
        class_name = splitted[0]
        params = splitted[1]
        n_items = splitted[2]
        #TODO: replace eval with something safer 
        item = eval (class_name+params)
        item_desc = ItemDescriptor(item, int(n_items))
        descs.append(item_desc)

initial=[]
#TODO: support also 0,1 instead of True,False
with open(initial_filename) as initial_file:
    for line in initial_file:
        splitted = line.split(', ')
        for bool_str in splitted:
            initial.append('True' == bool_str)

initial_state = RoomState(initial)
verf_nocst = GoalVerifier([], descs)
verf_isolt = GoalVerifier([IsolatedItems()], descs)
problem = RoomProblem (initial_state, verf_isolt)
sol = astar(problem)
for s in sol.path():
    print str(s.state)
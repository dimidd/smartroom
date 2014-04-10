from aima.search import astar_search as astar, Node
from smartroom.room_item import ItemDescriptor
from smartroom.room_item import Bench
from smartroom.room_state import RoomState
from smartroom.room_goal import GoalVerifier
from smartroom.room_problem import RoomProblem
from smartroom.room_constraint import IsolatedItems


#TODO: get input from commandline
bench = Bench(1)
desc = ItemDescriptor(bench,3)
initial = RoomState([False] * 5)
verf_nocst = GoalVerifier([], [desc])
verf_isolt = GoalVerifier([IsolatedItems()], [desc])
problem = RoomProblem (initial, verf_isolt)
sol = astar(problem)
for s in sol.path():
    print str(s.state)
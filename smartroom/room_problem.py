'''
Created on 10/04/2014

@author: dimid
'''

from aima.search import Problem
from smartroom.room_action import RemoveItem, PlaceItem
from smartroom.room_constraint import IsolatedItems


def isol_cond(state, lcorner, item_sz):
    """Return whether an item of size @sz in @lcorner"""
    if lcorner[1] > 0 and state.seats[lcorner[0]][lcorner[1] - 1]:
        return False
    rcorner = lcorner[0], lcorner[1] + item_sz - 1
    if  rcorner[1] + 1 < state.size() and  state.seats[rcorner[1] + 1]:
        return False

    return True


class RoomProblem(Problem):
    '''
    Room search problem.
    '''

    def isol_actions(self, state):
        """Return actions for isolated items"""
        actions = []

        spaces, shapes, unsatisfied = state.analyze(self.goalverf)
        for shp in shapes:
            actions.append(RemoveItem(shp.sz, shp.lcorner))

        # TODO: make this more efficient
        dscs = [dsc for dsc in unsatisfied if dsc.count > 0]
        for spc in spaces:
            for dsc in dscs:
                it_sz = dsc.item.size()
                if spc.size >= it_sz and isol_cond(state, spc.lcorner, it_sz):
                    actions.append(PlaceItem(dsc.item, spc.lcorner))

        # TODO: add MoveItem actions
        return actions

    def __init__(self, initial, goalverf):
        """The constructor specifies the initial state, and possibly a goal
        state, if there is a unique goal.  Your subclass's constructor can add
        other arguments."""
        self.initial = initial
        self.goalverf = goalverf
        if any(isinstance(x, IsolatedItems) for x in goalverf.constarints):
            self.actions_gen = self.isol_actions
        else:
            self.actions_gen = self.isol_actions  # TODO: use packing

    def actions(self, state):
        """Return the actions that can be executed in the given
        state. The result would typically be a list, but if there are
        many actions, consider yielding them one at a time in an
        iterator, rather than building them all at once."""

        return self.actions_gen(state)

    def result(self, state, action):
        """Return the state that results from executing the given
        action in the given state. The action must be one of
        self.actions(state)."""
        return action.apply(state)

    def goal_test(self, state):
        """Return True if the state is a goal. The default method compares the
        state to self.goal, as specified in the constructor. Override this
        method if checking against a single self.goal is not enough."""
        return self.goalverf.is_goal(state)

    def path_cost(self, c, state1, action, state2):
        """Return the cost of a solution path that arrives at state2 from
        state1 via action, assuming cost c to get up to state1. If the problem
        is such that the path doesn't matter, this function will only look at
        state2.  If the path does matter, it will consider c and maybe state1
        and action. The default method costs 1 for every step in the path."""
        return action.path_cost(c, state1, state2)

    def value(self, _state):
        """For optimization problems, each state has a value.  Hill-climbing
        and related algorithms try to maximize this value."""
        return None

    def h(self, node):
        ''' Heuristic: use number of remaining items to be positioned '''
        remaining = 0
        state = node.state
        _spaces, _shapes, unsatisfied = state.analyze(self.goalverf)
        for desc in unsatisfied:
            if desc.count > 0:
                remaining += desc.count * desc.item.size()

        return  remaining

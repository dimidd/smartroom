'''
Created on 10/04/2014

@author: dimid
'''

from aima.search import Problem
from room_action import FlipChair

class RoomProblem(Problem):
    '''
    Room search problem.
    '''

    def __init__(self, initial, goal_verifier):
        """The constructor specifies the initial state, and possibly a goal
        state, if there is a unique goal.  Your subclass's constructor can add
        other arguments."""
        self.initial = initial
        self.goalverf = goal_verifier

    def actions(self, state):
        """Return the actions that can be executed in the given
        state. The result would typically be a list, but if there are
        many actions, consider yielding them one at a time in an
        iterator, rather than building them all at once."""
        actions=[]
        for i in xrange(state.size()):
            actions.append(FlipChair(i))
            
        return actions

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

    def value(self, state):
        """For optimization problems, each state has a value.  Hill-climbing
        and related algorithms try to maximize this value."""
        return None
    
    def h(self, node):
        ''' Heuristic: use number of remaining items to be positioned '''
        remaining = 0
        state = node.state        
        for desc in self.goalverf.descriptors:
            remaining += desc.count - self.goalverf.count_items(state, desc.item)            
        
        return  remaining
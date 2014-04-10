import abc
import copy

'''
Created on 10/04/2014

@author: dimid
'''

class RoomAction(object):
    '''
    classdocs
    '''
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def apply(self, state):
        return
    
    def path_cost(self, c, state1, state2):
        """Return the cost of a solution path that arrives at state2 from
        state1 via action, assuming cost c to get up to state1. If the problem
        is such that the path doesn't matter, this function will only look at
        state2.  If the path does matter, it will consider c and maybe state1
        and action. The default method costs 1 for every step in the path."""

        return
        
class FlipChair (RoomAction):
    ''' Flip the @k-th chair
    '''
    def __init__ (self, k):
        self.index = k
        
    def apply (self, orig_state):
	state = copy.deepcopy(orig_state)
	state.seats[self.index] = not state.seats[self.index]
	return state;
    
    def path_cost(self, c, state1, state2):
        return c + 1

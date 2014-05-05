import abc
import copy

'''
Created on 10/04/2014

@author: dimid
'''


class RoomAction(object):
    '''
    Abstract room action
    '''
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def apply(self, _orig_state):
        return

    @abc.abstractmethod
    def path_cost(self, _c, _state1, _state2):
        """Return the cost of a solution path that arrives at state2 from
        state1 via action, assuming cost c to get up to state1. If the problem
        is such that the path doesn't matter, this function will only look at
        state2.  If the path does matter, it will consider c and maybe state1
        and action. The default method costs 1 for every step in the path."""

        return


class FlipChair (RoomAction):
    ''' Flip the @k-th chair
    '''
    def __init__(self, k):
        self.index = k

    def apply(self, orig_state):
        state = copy.deepcopy(orig_state)
        state.seats[self.index] = not state.seats[self.index]
        return state

    def path_cost(self, c, _state1, _state2):
        return c + 1


class PlaceItem (RoomAction):
    '''
    Place @param item such that its left corner is at index @param lcorner
    '''
    def __init__(self, item, lcorner):
        self.item = item
        self.lcorner = lcorner

    def apply(self, orig_state):
        state = copy.deepcopy(orig_state)
        row, col = self.lcorner
        sz = 0

        while sz < self.item.size():
            state.seats[row][col] = True
            col += 1
            sz += 1

        return state

    def path_cost(self, c, _state1, _state2):
        return c + self.item.size()


class RemoveItem (RoomAction):
    '''
    Remove @param item such that it's left corner is at index @param lcorner
    '''
    def __init__(self, size, lcorner):
        self.size = size
        self.lcorner = lcorner

    def apply(self, orig_state):
        state = copy.deepcopy(orig_state)
        row, col = self.lcorner
        sz = 0
        while sz < self.size:
            state.seats[row][col] = False
            sz = col - self.lcorner[1] + 1
            col += 1

        return state

    def path_cost(self, c, _state1, _state2):
        return c + self.size

'''
Created on 10/04/2014

@author: dimid
'''

import abc
from _pyio import __metaclass__
from abc import ABCMeta


class RoomConstraint(object):
    __metaclass__ = ABCMeta

    @abc.abstractmethod
    def count_violations(self, _state):
        return

    def is_valid(self, state):
        return 0 == self.count_violations(state)


class NullConstraint(RoomConstraint):

    def count_violations(self, _state):
        return 0


class IsolatedItems(RoomConstraint):
    # TODO: assume we have just 1xN items. How to count arbitrary shapes?
    def count_violations(self, _state):
        # all states are now guaranteed to be isolated by PlaceItem
        return 0


class FacingItems(RoomConstraint):

    def __init__(self, sz_a, sz_b, verf):
        self.sz_a = sz_a
        self.sz_b = sz_b
        self.verf = verf

    def count_violations(self, state):
        _spaces, shapes, _unsatisfied = state.analyze(self.verf)
        sizes = [self.sz_a, self.sz_b]
        cands = [s for s in shapes if s.sz in sizes]
        for c in cands:
                ind_c = sizes.index(c.sz)
                ind2 = (ind_c + 1) % 2
                for c2 in [s for s in shapes if s.sz == sizes[ind2]]:
                    if c == c2:
                        continue
                    if c2.lcorner[1] == c.lcorner[1]:
                        return 0
        return 1

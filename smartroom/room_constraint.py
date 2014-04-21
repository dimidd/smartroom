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
    def count_violations(self, state):
        count = 0
        seats = state.seats
        for i in xrange (0, len(seats) - 1):
            if seats[i] and seats[i+1]:
                count += 1

        return count

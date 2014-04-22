import abc
'''
Created on 10/04/2014

@author: dimid
'''
from abc import ABCMeta


class ItemDescriptor(object):
    def __init__(self, item, count):
        self.item = item
        self.count = count

    def __repr__(self):
        return '(IT:' + repr(self.item) + ', CO:' + str(self.count) + ')'


class RoomItem(object):
    __metaclass__ = ABCMeta
    '''
    classdocs
    '''

    @abc.abstractmethod
    def binary(self):
        '''
        Representation of this item as a binary image. i.e a 2d list of bools
        '''
        return


class Bench(RoomItem):

    def __init__(self, n_seats):
        '''
        Constructor
        '''
        self.n_seats = n_seats

    def binary(self):
        return [[True] * self.n_seats]

    def __repr__(self):
        return self.__class__.__name__ + '(' + str(self.n_seats) + ')'

    def size(self):
        return self.n_seats

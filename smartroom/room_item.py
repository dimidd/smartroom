import abc
'''
Created on 10/04/2014

@author: dimid
'''
from abc import ABCMeta

class ItemDescriptor(object):
    def __init__(self, item, count):
        self.item=item
        self.count=count

class RoomItem(object):
    __metaclass__ = ABCMeta
    '''
    classdocs
    '''
    
    @abc.abstractmethod
    def binary(self):
        '''
        Return representation of this item as a binary image. i.e a 2d list of booleans
        '''
        return

class Bench(RoomItem):    

    def __init__(self, n_seats):
        '''
        Constructor
        '''
        self.ns_seats = n_seats
        
    
    def binary(self):
        return [[True] * self.ns_seats]   
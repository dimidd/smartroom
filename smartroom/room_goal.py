'''
Created on 10/04/2014

@author: dimid
'''

class GoalVerifier(object):
    '''
    classdocs
    '''

    def __init__(self, constraints, item_descriptors):
        self.constarints = constraints
        self.descriptors = item_descriptors              
        
    # TODO: for the meantime assume we have just 1x1 items. How to count arbitrary shapes?
    def count_items(self, state, item):
        count = 0
        for s in state.seats:
            if s:
                count += 1 
        return count
         
    def is_goal (self, state):
        for c in self.constarints:
            if not c.is_valid(state):
                return False
            
        for d in self.descriptors:
            if d.count != self.count_items(state, d.item):
                return False
        
        return True         
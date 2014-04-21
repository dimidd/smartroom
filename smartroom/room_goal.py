'''
Created on 10/04/2014

@author: dimid
'''


class GoalVerifier(object):
    '''
    Verifies all constraints item requirements are met
    '''

    def __init__(self, constraints, item_descriptors):
        self.constarints = constraints
        self.descriptors = item_descriptors

    # TODO: assume we have just 1xN items. How to count arbitrary shapes?
    def count_items(self, state, _item):
        _spaces, shapes, _unsatisfied = state.analyze(self)
        return len(shapes)

    def is_goal(self, state):
        for c in self.constarints:
            if not c.is_valid(state):
                return False

        _spaces, _shapes, unsatisfied = state.analyze(self)
        for us in unsatisfied:
            if us.count > 0:
                return False

        return True

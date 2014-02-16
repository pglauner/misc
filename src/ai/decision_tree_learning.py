'''
Created on Feb 16, 2014

@author: pglauner
'''

import collections


EXAMPLE = {
    # (Alt, Bar, Fri, Hun, Pat, Price, Rain, Res, Type, Est): WillWait
    (True,  False,  False,  True,   'Some', '$$$',  False,  True,   'French',   '0-10'):    True,
    (True,  False,  False,  True,   'Full', '$',    False,  False,  'Thai',     '30-60'):   False,
    (False, True,   False,  False,  'Some', '$',    False,  False,  'Burger',   '0-10'):    True,
    (True,  False,  True,   True,   'Full', '$',    True,   False,  'Thai',     '30-60'):   True,
    (True,  False,  True,   False,  'Full', '$$$',  False,  True,   'French',   '>60'):     False,
    (False, True,   False,  True,   'Some', '$$',   True,   True,   'Italian',  '0-10'):    True,
    (False, True,   False,  False,  'None', '$',    True,   False,  'Burger',   '0-10'):    False,
    (False, False,  False,  True,   'Some', '$$',   True,   True,   'Thai',     '0-10'):    True,
    (False, True,   True,   False,  'Full', '$',    True,   False,  'Burger',   '>60'):     False,
    (True,  True,   True,   True,   'Full', '$$$',  False,  True,   'Italian',  '10-30'):   False,
    (False, False,  False,  False,  'None', '$',    False,  False,  'Thai',     '0-10'):    False,
    (True,  True,   True,   True,   'Full', '$',    False,  False,  'Burger',   '30-60'):   True,
}


def Tree():
    return collections.defaultdict(Tree)


def decision_tree_learning(examples, attributes, parent_examples):
    if len(examples) == 0:
        pass
    #elif:
    #    pass
    elif len(attributes) == 0:
        pass
    else:
        pass


if __name__ == '__main__':
    t = Tree()
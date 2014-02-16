'''
Created on Feb 16, 2014

@author: pglauner

Implementation of decision tree learning. Algorithm and examples based on
Artificial Intelligence: A Modern Approach, Chapter 18.

'''

import collections

ATTRIBUTES = {
    'Alt': 0,
    'Bar': 1,
    'Fri': 2,
    'Hun': 3,
    'Pat': 4,
    'Price': 5,
    'Rain': 6,
    'Res': 7,
    'Type': 8,
    'Est': 9,
    }


EXAMPLES = {
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
        return plurality_value(parent_examples)
    # All examples have the same classification
    elif len(set(examples.values())) == 1:
        return examples.values()[0]
    elif len(attributes) == 0:
        return plurality_value(examples)
    else:
        attribute = None
        tree = Tree()
        for vk in attributes:
            # TODO
            exs = None
            subtree = decision_tree_learning(exs, attributes - attribute, examples)
            tree[attribute] = subtree
        return tree


def plurality_value(examples):
    return collections.Counter(examples.values()).most_common()[0]


def importance(attribute, examples):
    pass


if __name__ == '__main__':
    tree = decision_tree_learning(EXAMPLES, set(ATTRIBUTES.keys()), [])
    print tree

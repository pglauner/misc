'''
Created on Feb 16, 2014

@author: pglauner

Implementation of decision tree learning. Algorithm and examples based on
Artificial Intelligence: A Modern Approach, Chapter 18.

'''

import collections
import operator
import math

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
        attribute = choose_most_relevant_attribute(examples, attributes)
        tree = Tree()
        for attribute_value in get_attribute_values(examples, attribute):
            exs = get_similiar_examples(examples, attribute, attribute_value)
            subtree = decision_tree_learning(exs, attributes - set([attribute]), examples)
            tree[attribute][attribute_value] = subtree
        return tree


def choose_most_relevant_attribute(examples, attributes):
    attribute = max([(attribute, importance(attribute, examples))
                                for attribute in attributes], key=operator.itemgetter(1))[0]

    return attribute


def get_attribute_values(examples, attribute):
    attribute_id = ATTRIBUTES[attribute]
    return [e[attribute_id] for e in examples]


def get_similiar_examples(examples, attribute, attribute_value):
    attribute_id = ATTRIBUTES[attribute]
    return dict((k, v) for (k, v) in examples.iteritems() if k[attribute_id] == attribute_value)


def plurality_value(examples):
    return collections.Counter(examples.values()).most_common()[0]


def importance(attribute, examples):
    def log2(v):
        return math.log(v) / math.log(2)

    def b(q):
        return -(q * log2(2) + (1 - q) * log2(1 - q))

    # TODO
    remainder = None
    gain = None

    return gain


if __name__ == '__main__':
    tree = decision_tree_learning(EXAMPLES, set(ATTRIBUTES.keys()), [])
    print tree

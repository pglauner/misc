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


def get_attribute_id(attribute):
    return ATTRIBUTES[attribute]


def choose_most_relevant_attribute(examples, attributes):
    attribute = max([(attribute, importance(examples, attribute))
                                for attribute in attributes], key=operator.itemgetter(1))[0]

    return attribute


def get_attribute_values(examples, attribute):
    attribute_id = get_attribute_id(attribute)
    return [e[attribute_id] for e in examples]


def get_similiar_examples(examples, attribute, attribute_value):
    attribute_id = get_attribute_id(attribute)
    return dict((k, v) for (k, v) in examples.iteritems() if k[attribute_id] == attribute_value)


def plurality_value(examples):
    return collections.Counter(examples.values()).most_common()[0]


def importance(examples, attribute):
    def log2(v):
        return math.log(v) / math.log(2)

    def b(q):
        # Shortcut to avoid treatment of log(0)
        if q in (0, 1):
            return 0
        return -(q * log2(q) + (1 - q) * log2(1 - q))

    def pos_neg(exs):
        pos = float(sum([1 for (k, v) in exs.iteritems() if v == True]))
        neg = float(sum([1 for (k, v) in exs.iteritems() if v == False]))
        return pos, neg

    def remainder_part(exs):
        pos, neg = pos_neg(exs)
        return (pos / (pos + neg)) * b(pos / (pos + neg))

    attribute_id = get_attribute_id(attribute)
    distinct_attribute_values = set([example[attribute_id] for example in examples.keys()])
    distinct_examples = [get_similiar_examples(examples, attribute, attribute_value) for attribute_value in distinct_attribute_values]
    remainder = sum([remainder_part(exs) for exs in distinct_examples])

    pos, neg = pos_neg(examples)
    gain = b(pos / (pos + neg)) - remainder

    return gain


if __name__ == '__main__':
    tree = decision_tree_learning(EXAMPLES, set(ATTRIBUTES.keys()), [])
    print tree

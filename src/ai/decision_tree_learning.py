'''
Created on Feb 16, 2014

@author: pglauner

Implementation of decision tree learning. Algorithm and examples based on
Artificial Intelligence: A Modern Approach, Chapter 18.

Notes: code can be further improved to be completely independent from global
ATTRIBUTES variable.

'''

import collections
import operator
import math

ATTRIBUTES = {
    'Alternate?': 0,
    'Bar?': 1,
    'Fri/Sat?': 2,
    'Hungry?': 3,
    'Patrons?': 4,
    'Price?': 5,
    'Raining?': 6,
    'Reservation?': 7,
    'Type?': 8,
    'WaitEstimate?': 9,
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
    attributes = set(attributes)
    if len(examples) == 0:
        return plurality_value(parent_examples)
    # All examples have the same classification
    elif len(set(examples.values())) == 1:
        return examples.values()[0]
    elif len(attributes) == 0:
        return plurality_value(examples)
    else:
        attribute = choose_most_relevant_attribute(examples, attributes)
        attribute_id = get_attribute_id(attribute)
        tree = Tree()
        for attribute_value in get_attribute_values(examples, attribute_id):
            exs = get_similiar_examples(examples, attribute_id, attribute_value)
            subtree = decision_tree_learning(exs, attributes - set([attribute]), examples)
            tree[attribute][attribute_value] = subtree
        return tree


def get_attribute_id(attribute):
    return ATTRIBUTES[attribute]


def choose_most_relevant_attribute(examples, attributes):
    attribute = max([(attribute, importance(examples, attribute, get_attribute_id(attribute))) for attribute in attributes],
                        key=operator.itemgetter(1))[0]

    return attribute


def get_attribute_values(examples, attribute_id):
    return set([e[attribute_id] for e in examples])


def get_similiar_examples(examples, attribute_id, attribute_value):
    return dict((k, v) for (k, v) in examples.iteritems() if k[attribute_id] == attribute_value)


def plurality_value(examples):
    # Deterministic tie breaker
    return collections.Counter(examples.values()).most_common()[0]


def get_distinct_examples(examples, attribute_id):
    return [get_similiar_examples(examples, attribute_id, attribute_value)
                for attribute_value in get_attribute_values(examples, attribute_id)]


def importance(examples, attribute, attribute_id):
    def log2(v):
        return math.log(v) / math.log(2)

    def b(p, n):
        # Shortcut to avoid treatment of log(0)
        q = p / (p + n)
        if q in (0, 1):
            return 0
        return -(q * log2(q) + (1 - q) * log2(1 - q))

    def pos_neg(exs):
        pos = float(exs.values().count(True))
        neg = float(exs.values().count(False))
        return pos, neg

    def remainder_part(exs):
        pos_k, neg_k = pos_neg(exs)
        return ((pos_k + neg_k) / (pos + neg)) * b(pos_k, neg_k)

    pos, neg = pos_neg(examples)
    remainder = sum([remainder_part(exs) for exs in get_distinct_examples(examples, attribute_id)])
    gain = b(pos, neg) - remainder

    return gain


if __name__ == '__main__':
    tree = decision_tree_learning(EXAMPLES, ATTRIBUTES.keys(), [])
    print tree

'''
Created on Aug 29, 2013

@author: pglauner
'''

# Original phrase: "This wa a graet test"
# wa -> was, war, man
# graet -> great, greet
simple_phrase = {}
simple_phrase[0] = {'This': 0}
simple_phrase['This'] = {'was': 0.1, 'war': 0.4, 'man': 0.5}
simple_phrase['was'] = {'a': 0.2}
simple_phrase['war'] = {'a': 0.9}
simple_phrase['man'] = {'a': 0.9}
simple_phrase['a'] = {'great': 0.1, 'greet': 0.3}
simple_phrase['great'] = {'test': 0.3}
simple_phrase['greet'] = {'test': 0.2}
simple_phrase['test'] = {1: 0}

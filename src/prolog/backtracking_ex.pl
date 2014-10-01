p(1).
p(2) :- !.
p(3).

class(Number, positive) :- Number > 0.
class(0, zero).
class(Number, negative) :- Number < 0.

class1(Number, negative) :- Number < 0, !.
class1(Number, positive) :- Number > 0, !.
class1(0, zero).
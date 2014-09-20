family(
person(tom, fox, date(7, may, 1950), works(bbc, 15200)),
person(ann, fox, date(9, may, 1951), unemployed),
[person(pat, fox, date(5, may, 1973), unemployed),
 person(jim, fox, date(5, may, 1973), unemployed)]).

husband(X) :- family(X, _, _).

wife(X) :- family(_, X, _).

child(X) :- family(_, _, Children), my_member(X, Children).

my_del(X, [X|Tail], Tail).
my_del(X, [Y|Tail], [Y|Tail1]) :- my_del(X, Tail, Tail1).

exists(Person) :- husband(Person); wife(Person); child(Person).

dateofbirth(person(_, _, Date, _), Date).

salary(person(_, _, _, unemployed), 0).
salary(person(_, _, _, works(_, S)), S).

total([], 0).
total([Person|T], Sum) :- salary(Person, S), total(T, Rest), Sum is S + Rest.

twins(Child1, Child2) :-
 family(_, _, Children),
 member(Child1, Children),
 member(Child2, Children),
 dateofbirth(Child1, Date),
 dateofbirth(Child2, Date),
 not(Child1 = Child2).

twins1(Child1, Child2) :-
 family(_, _, Children),
 my_del(Child1, Children, OtherChildren),
 member(Child2, OtherChildren),
 dateofbirth(Child1, Date),
 dateofbirth(Child2, Date).
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

nth_member(1, [H|_], H).
nth_member(N, [_|T], X) :- N1 is N - 1, nth_member(N1, T, X).

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

husband(family(Husband, _, _), Husband).
wife(family(_, Wife, _), Wife).
children(family(_, _, ChildList), ChildList).
firstchild(Family, First) :- children(Family, [First|_]).
secondchild(Family, Second) :- children(Family, [_, Second|_]).
nthchild(N, Family, Child) :- children(Family, ChildList), nth_member(N, ChildList, Child).
firstname(person(Name, _, _), Name).
surname(person(_, Surname, _), Surname).
born(person(_, _, Date, _), Date).
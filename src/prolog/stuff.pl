mymember(X, [X|_]).
mymember(X, [_|Tail]) :- mymember(X, Tail).

mymember2(X, L) :- mydel(X, L, _).

myconcat([], L, L).
myconcat([X|L1], L2, [X|L3]) :- myconcat(L1, L2, L3).

mydellast3(X, Res) :- myconcat(Res, [_, _, _], X).

mydelfirstlast3(X, Res) :- myconcat(ResTemp, [_, _, _], X), myconcat([_, _, _], Res, ResTemp).


mylast1(Item, List) :- myconcat(_, [Item], List).

mylast2(Item, [Item]).
mylast2(Item, [_|Tail]) :- mylast2(Item, Tail).

myadd(X, L, [X, L]).

mydel(X, [X|T], T).
mydel(X, [Y|T], [Y|T1]) :- mydel(X, T, T1).

myinsert(X, L, Res) :- mydel(X, Res, L).

mysublist(S, L) :-
  myconcat(_, L2, L),
  myconcat(S, _, L2).

mypermutation([], []).
mypermutation([X|L], Res) :-
  mypermutation(L, L1),
  myinsert(X, L1, Res).

mypermutation2([], []).
mypermutation2(L, [X|P]) :-
  mydel(X, L, L1),
  mypermutation(L1, P).

myevenlength([]).
myevenlength([_|T]) :- myoddlength(T).
myoddlength([_]).
myoddlength([_|T]) :- myevenlength(T).

myreverse([], []).
myreverse([H|T], Res) :-
  myreverse(T, TRes),
  myconcat(TRes, [H], Res).

mypalindrome(L, Res) :- myreverse(L, Res).
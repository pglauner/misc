f(X, 0) :- X < 3.
f(X, 2) :- 3 =< X, X < 6.
f(X, 4) :- 6 =< X.

f1(X, 0) :- X < 3, !.
f1(X, 2) :- 3 =< X, X < 6, !.
f1(X, 4) :- 6 =< X.

f2(X, 0) :- X < 3, !.
f2(X, 2) :- X < 6, !.
f2(X, 4).

max(X, Y, X) :- X >= Y.
max(X, Y, Y) :- X < Y.

max1(X, Y, X) :- X >= Y, !.
max1(X, Y, Y).

mymember(X, [X|L]).
mymember(X, [X|L]) :- mymember(X, L).

mymember1(X, [X|L]) :- !.
mymember1(X, [X|L]) :- mymember(X, L).

myadd(X, L, L) :- mymember1(X, L), !.
myadd(X, L, [X|L]).